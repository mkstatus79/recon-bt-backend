# ============================================
# CÁLCULO DA SEÇÃO B - RECON-BT 2026
# Cálculo para conjuntos residenciais (4 a 300 unidades)
# ============================================

from .tabelas import TABELA_611, TABELA_612, TABELA_613

# --------------------------------------------
# TABELAS 6.11 e 6.12 - Demanda por área
# (já devem estar no arquivo tabelas.py)
# --------------------------------------------

def get_demanda_por_area(area_m2, com_aquecimento=True):
    """
    Retorna demanda em kVA por unidade consumidora baseado na área
    Tabela 6.11 (com aquecimento) ou 6.12 (sem aquecimento)
    """
    from .tabelas import TABELA_611, TABELA_612
    
    tabela = TABELA_611 if com_aquecimento else TABELA_612
    
    # Procura área exata
    for item in tabela:
        if item["area"] == area_m2:
            return item["demanda"]
    
    # Se não encontrar, faz interpolação linear
    areas = [item["area"] for item in tabela]
    demandas = [item["demanda"] for item in tabela]
    
    if area_m2 < areas[0]:
        return demandas[0]
    if area_m2 > areas[-1]:
        return demandas[-1]
    
    for i in range(len(areas) - 1):
        if areas[i] <= area_m2 <= areas[i + 1]:
            # Interpolação linear
            x1, y1 = areas[i], demandas[i]
            x2, y2 = areas[i + 1], demandas[i + 1]
            demanda = y1 + (y2 - y1) * (area_m2 - x1) / (x2 - x1)
            return round(demanda, 2)
    
    return None


def get_fator_diversificacao(num_ucs):
    """
    Retorna fator de diversificação da Tabela 6.13
    """
    from .tabelas import TABELA_613
    
    for item in TABELA_613:
        if item["num_apartamentos"] == num_ucs:
            return item["fator"]
    
    # Se não encontrar, usa o último valor
    if num_ucs > 300:
        return 83.00
    return None


def calcular_area_equivalente(areas, quantidades):
    """
    Calcula área equivalente para conjunto com áreas diferentes
    Aeq = Σ(n × S) / Σ(n)
    
    Args:
        areas: lista de áreas (m²)
        quantidades: lista de quantidades correspondentes
    
    Returns:
        área equivalente (m²)
    """
    total_area = 0
    total_ucs = 0
    
    for area, qtd in zip(areas, quantidades):
        total_area += area * qtd
        total_ucs += qtd
    
    if total_ucs == 0:
        return 0
    
    return total_area / total_ucs


def calcular_potencia_equivalente(potencias, quantidades):
    """
    Calcula potência equivalente para chuveiros de diferentes potências
    Peq = Σ(Q × P) / Σ(Q)
    
    Args:
        potencias: lista de potências dos chuveiros (kVA)
        quantidades: lista de quantidades correspondentes
    
    Returns:
        potência equivalente (kVA)
    """
    total_potencia = 0
    total_aparelhos = 0
    
    for pot, qtd in zip(potencias, quantidades):
        total_potencia += pot * qtd
        total_aparelhos += qtd
    
    if total_aparelhos == 0:
        return 0
    
    return total_potencia / total_aparelhos


def get_fator_seguranca(potencia_eq):
    """
    Retorna fator de segurança conforme Tabela 6.10
    """
    if potencia_eq <= 4.40:
        return 1.00  # 0%
    elif potencia_eq <= 6.00:
        return 1.10  # 10%
    elif potencia_eq <= 10.00:
        return 1.20  # 20%
    else:
        return 1.30  # 30% (acima de 10 kVA)


def calcular_secao_b(dados_ucs, servico_kva=0):
    """
    Calcula demanda conforme Seção B do RECON-BT
    
    Args:
        dados_ucs: lista de dicionários com:
            - area: área em m²
            - quantidade: número de UCs com essa área
            - com_aquecimento: True/False
            - potencias_chuveiros: lista de potências (opcional)
        servico_kva: demanda do serviço (condomínio) em kVA
    
    Returns:
        dict com resultados
    """
    
    resultados = {}
    
    # ----------------------------------------
    # 1. Área equivalente
    # ----------------------------------------
    areas = [item["area"] for item in dados_ucs]
    quantidades = [item["quantidade"] for item in dados_ucs]
    area_eq = calcular_area_equivalente(areas, quantidades)
    resultados["area_equivalente"] = round(area_eq, 2)
    
    # ----------------------------------------
    # 2. Total de unidades
    # ----------------------------------------
    total_ucs = sum(quantidades)
    resultados["total_ucs"] = total_ucs
    
    # ----------------------------------------
    # 3. Demanda por UC (com ou sem aquecimento)
    # ----------------------------------------
    # Usa o primeiro item como referência para tipo de aquecimento
    # (assumimos que todas são iguais - se não, precisa tratar separadamente)
    com_aquecimento = dados_ucs[0].get("com_aquecimento", True)
    demanda_uc = get_demanda_por_area(area_eq, com_aquecimento)
    resultados["demanda_por_uc"] = demanda_uc
    
    # ----------------------------------------
    # 4. Fator de diversificação
    # ----------------------------------------
    fator_div = get_fator_diversificacao(total_ucs)
    resultados["fator_diversificacao"] = fator_div
    
    # ----------------------------------------
    # 5. Demanda do agrupamento (antes do fator de segurança)
    # ----------------------------------------
    demanda_agrupamento = demanda_uc * fator_div
    resultados["demanda_agrupamento_base"] = round(demanda_agrupamento, 2)
    
    # ----------------------------------------
    # 6. Fator de segurança para chuveiros >4,4 kVA
    # ----------------------------------------
    fator_seguranca = 1.0
    
    # Se houver informações de potências de chuveiros
    if dados_ucs[0].get("potencias_chuveiros"):
        potencias = []
        qtds = []
        for item in dados_ucs:
            if item.get("potencias_chuveiros"):
                for pot in item["potencias_chuveiros"]:
                    potencias.append(pot)
                    qtds.append(item["quantidade"])
        
        if potencias:
            potencia_eq = calcular_potencia_equivalente(potencias, qtds)
            fator_seguranca = get_fator_seguranca(potencia_eq)
            resultados["potencia_equivalente"] = round(potencia_eq, 2)
    
    resultados["fator_seguranca"] = fator_seguranca
    
    # ----------------------------------------
    # 7. Demanda final do agrupamento
    # ----------------------------------------
    demanda_final = demanda_agrupamento * fator_seguranca
    resultados["demanda_agrupamento_final"] = round(demanda_final, 2)
    
    # ----------------------------------------
    # 8. Demanda da proteção geral
    # ----------------------------------------
    # DPG = demanda do agrupamento (se serviço antes da proteção)
    resultados["demanda_protecao_geral"] = round(demanda_final, 2)
    
    # ----------------------------------------
    # 9. Demanda do ramal
    # ----------------------------------------
    # DR = (DPG + DS) × 0,90
    demanda_ramal = (demanda_final + servico_kva) * 0.90
    if demanda_ramal < demanda_final:
        demanda_ramal = demanda_final
    resultados["demanda_ramal"] = round(demanda_ramal, 2)
    resultados["demanda_servico"] = servico_kva
    
    return resultados


def exemplo_secao_b():
    """Exemplo do Fascículo 06 - Caso 01 (24 aptos de 70m²)"""
    
    dados = [
        {
            "area": 70,
            "quantidade": 24,
            "com_aquecimento": True,
            "potencias_chuveiros": [4.4]  # todos com chuveiro 4.4 kVA
        }
    ]
    
    servico = 18.71  # demanda do condomínio
    
    resultado = calcular_secao_b(dados, servico)
    
    return resultado


def exemplo_secao_b_com_areas_diferentes():
    """Exemplo com áreas diferentes (20 aptos 70m² + 20 aptos 82m²)"""
    
    dados = [
        {
            "area": 70,
            "quantidade": 20,
            "com_aquecimento": True,
            "potencias_chuveiros": [4.4]
        },
        {
            "area": 82,
            "quantidade": 20,
            "com_aquecimento": True,
            "potencias_chuveiros": [4.4]
        }
    ]
    
    servico = 16.38
    
    resultado = calcular_secao_b(dados, servico)
    
    return resultado


def exemplo_secao_b_com_chuveiros_maiores():
    """Exemplo com chuveiros >4,4 kVA (fator de segurança)"""
    
    dados = [
        {
            "area": 60,
            "quantidade": 18,
            "com_aquecimento": True,
            "potencias_chuveiros": [5.5]  # chuveiro 5.5 kVA
        },
        {
            "area": 85,
            "quantidade": 18,
            "com_aquecimento": True,
            "potencias_chuveiros": [5.5, 7.5]  # alguns com 5.5, outros com 7.5
        }
    ]
    
    servico = 16.30
    
    resultado = calcular_secao_b(dados, servico)
    
    return resultado
