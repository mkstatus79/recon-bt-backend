# ============================================
# DIMENSIONAMENTO DE ATERRAMENTO - RECON-BT 2026
# ============================================

# Tabela 10.1 - Fator k para condutor de proteção
TABELA_101 = [
    {"material": "cobre", "isolacao": "PVC", "k": 115},
    {"material": "cobre", "isolacao": "PVC_maior_300", "k": 103},
    {"material": "cobre", "isolacao": "XLPE_EPR_HEPR", "k": 143},
]

# Tabela 10.2 - Seção mínima do condutor de proteção
TABELA_102 = [
    {"secao_fase_min": 0, "secao_fase_max": 16, "secao_protecao": "S"},
    {"secao_fase_min": 16, "secao_fase_max": 35, "secao_protecao": 16},
    {"secao_fase_min": 35, "secao_fase_max": 999, "secao_protecao": "S/2"},
]

# Tabela 10.3 - Capacidade de interrupção de disjuntores (kA)
TABELA_103 = [
    {"bitola": 6, "aereo": 5, "sub_radial": 15, "sub_reticulado": 15},
    {"bitola": 10, "aereo": 5, "sub_radial": 15, "sub_reticulado": 15},
    {"bitola": 16, "aereo": 5, "sub_radial": 15, "sub_reticulado": 15},
    {"bitola": 25, "aereo": 10, "sub_radial": 15, "sub_reticulado": 15},
    {"bitola": 35, "aereo": 10, "sub_radial": 15, "sub_reticulado": 15},
    {"bitola": 50, "aereo": 15, "sub_radial": 25, "sub_reticulado": 25},
    {"bitola": 70, "aereo": 15, "sub_radial": 25, "sub_reticulado": 25},
    {"bitola": 95, "aereo": 20, "sub_radial": 30, "sub_reticulado": 40},
    {"bitola": 120, "aereo": 20, "sub_radial": 30, "sub_reticulado": 40},
    {"bitola": 150, "aereo": 40, "sub_radial": 50, "sub_reticulado": 50},
    {"bitola": 185, "aereo": 40, "sub_radial": 50, "sub_reticulado": 50},
    {"bitola": 240, "aereo": 40, "sub_radial": 50, "sub_reticulado": 50},
]

def num_hastes_aterramento(tipo_entrada, num_ucs=1, demanda_kva=0):
    """
    Calcula número mínimo de hastes conforme item 2.5 do Fascículo 10
    """
    if tipo_entrada == "INDIVIDUAL":
        if demanda_kva <= 24:
            return 1
        elif demanda_kva <= 150:
            return 3
        else:
            return 6
    else:  # COLETIVA
        if num_ucs <= 6:
            # 1 haste por UC, respeitando mínimo de 3
            return max(3, num_ucs)
        else:
            return 6

def secao_condutor_protecao(secao_fase):
    """
    Retorna seção mínima do condutor de proteção (Tabela 10.2)
    """
    if secao_fase <= 16:
        return secao_fase
    elif secao_fase <= 35:
        return 16
    else:
        return secao_fase // 2

def capacidade_interrupcao(bitola, tipo_rede="aereo"):
    """
    Retorna capacidade mínima de interrupção do disjuntor (Tabela 10.3)
    """
    for item in TABELA_103:
        if item["bitola"] == bitola:
            return item[tipo_rede]
    return None

def dimensionar_aterramento_completo(dados):
    """
    Dimensiona todo o sistema de aterramento
    """
    resultado = {
        "num_hastes": num_hastes_aterramento(
            dados.get("tipo_entrada", "INDIVIDUAL"),
            dados.get("num_ucs", 1),
            dados.get("demanda_kva", 0)
        ),
        "tipo_haste": "aço cobreado 5/8\" x 2,40m",
        "condutor_interligacao": 50,  # mínimo 50mm² conforme item 2.5
        "secao_fase": dados.get("secao_fase", 95),
        "condutor_protecao": secao_condutor_protecao(dados.get("secao_fase", 95)),
        "capacidade_disjuntor_ka": capacidade_interrupcao(
            dados.get("secao_fase", 95),
            dados.get("tipo_rede", "aereo")
        ),
        "observacoes": []
    }
    
    # Observações importantes
    if resultado["num_hastes"] == 1:
        resultado["observacoes"].append("Resistência de aterramento deve ser ≤ 25Ω")
    else:
        resultado["observacoes"].append("Hastes interligadas com espaçamento ≥ 2,40m")
    
    return resultado
