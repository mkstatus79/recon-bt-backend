# ============================================
# TABELAS DE DIMENSIONAMENTO - RECON-BT 2026
# ============================================

# --------------------------------------------
# Tabela 7.3 - Medição direta individual (Fascículo 07)
# --------------------------------------------
TABELA_73 = [
    # Tensão 127V
    {"categoria": "UM1", "tensao": "127V", "fases": 1, "demanda_min": 0, "demanda_max": 5, 
     "disjuntor": 40, "eletroduto_aereo": "1\"", "eletroduto_sub": "2\"", 
     "condutor": "2x10", "protecao": "1x10", "aterramento": "1x10"},
    {"categoria": "UM2", "tensao": "127V", "fases": 1, "demanda_min": 5, "demanda_max": 8, 
     "disjuntor": 63, "eletroduto_aereo": "1\"", "eletroduto_sub": "2\"", 
     "condutor": "2x16", "protecao": "1x16", "aterramento": "1x16"},
    
    # Tensão 220/127V bifásico
    {"categoria": "UB1", "tensao": "220/127V", "fases": 2, "demanda_min": 0, "demanda_max": 8, 
     "disjuntor": 40, "eletroduto_aereo": "2\"", "eletroduto_sub": "2\"", 
     "condutor": "3x10", "protecao": "1x10", "aterramento": "1x10"},
    {"categoria": "UB2", "tensao": "220/127V", "fases": 2, "demanda_min": 8, "demanda_max": 13, 
     "disjuntor": 63, "eletroduto_aereo": "2\"", "eletroduto_sub": "2\"", 
     "condutor": "3x16", "protecao": "1x16", "aterramento": "1x16"},
    
    # Tensão 220/127V trifásico
    {"categoria": "T1", "tensao": "220/127V", "fases": 3, "demanda_min": 0, "demanda_max": 15, 
     "disjuntor": 40, "eletroduto_aereo": "2\"", "eletroduto_sub": "2\"", 
     "condutor": "4x10", "protecao": "1x10", "aterramento": "1x10"},
    {"categoria": "T2", "tensao": "220/127V", "fases": 3, "demanda_min": 15, "demanda_max": 24, 
     "disjuntor": 63, "eletroduto_aereo": "2\"", "eletroduto_sub": "2\"", 
     "condutor": "4x16", "protecao": "1x16", "aterramento": "1x16"},
    {"categoria": "T3", "tensao": "220/127V", "fases": 3, "demanda_min": 24, "demanda_max": 30, 
     "disjuntor": 80, "eletroduto_aereo": "2x2\"", "eletroduto_sub": "2\"", 
     "condutor": "4x25", "protecao": "1x16", "aterramento": "1x16"},
    {"categoria": "T4", "tensao": "220/127V", "fases": 3, "demanda_min": 30, "demanda_max": 38, 
     "disjuntor": 100, "eletroduto_aereo": "2x2\"", "eletroduto_sub": "2\"", 
     "condutor": "4x35", "protecao": "1x16", "aterramento": "1x16"},
    {"categoria": "T5", "tensao": "220/127V", "fases": 3, "demanda_min": 38, "demanda_max": 47, 
     "disjuntor": 125, "eletroduto_aereo": "3\"", "eletroduto_sub": "2x4\"", 
     "condutor": "4x50", "protecao": "1x25", "aterramento": "1x25"},
    {"categoria": "T6", "tensao": "220/127V", "fases": 3, "demanda_min": 47, "demanda_max": 57, 
     "disjuntor": 150, "eletroduto_aereo": "3\"", "eletroduto_sub": "2x4\"", 
     "condutor": "4x70", "protecao": "1x35", "aterramento": "1x35"},
    {"categoria": "T7", "tensao": "220/127V", "fases": 3, "demanda_min": 57, "demanda_max": 66, 
     "disjuntor": 175, "eletroduto_aereo": "3\"", "eletroduto_sub": "2x4\"", 
     "condutor": "4x95", "protecao": "1x50", "aterramento": "1x50"},
    {"categoria": "T8", "tensao": "220/127V", "fases": 3, "demanda_min": 66, "demanda_max": 76, 
     "disjuntor": 200, "eletroduto_aereo": "3\"", "eletroduto_sub": "2x4\"", 
     "condutor": "4x95", "protecao": "1x50", "aterramento": "1x50"},
]

# --------------------------------------------
# Tabela 7.4 - Medição indireta individual (Fascículo 07)
# --------------------------------------------
TABELA_74 = [
    {"categoria": "TI1", "demanda_min": 76, "demanda_max": 85, "disjuntor": 225,
     "eletroduto_sub": "2x4\"", "condutor": "4x120", "protecao": "1x70"},
    {"categoria": "TI2", "demanda_min": 85, "demanda_max": 95, "disjuntor": 250,
     "eletroduto_sub": "2x4\"", "condutor": "4x150", "protecao": "1x95"},
    {"categoria": "TI3", "demanda_min": 95, "demanda_max": 114, "disjuntor": 300,
     "eletroduto_sub": "2x4\"", "condutor": "4x185", "protecao": "1x95"},
    {"categoria": "TI4", "demanda_min": 114, "demanda_max": 133, "disjuntor": 350,
     "eletroduto_sub": "2x4\"", "condutor": "4x240", "protecao": "1x120"},
    {"categoria": "TI5", "demanda_min": 133, "demanda_max": 150, "disjuntor": 400,
     "eletroduto_sub": "2x4\"", "condutor": "8x150", "protecao": "1x150"},
    {"categoria": "TI6", "demanda_min": 150, "demanda_max": 190, "disjuntor": 500,
     "eletroduto_sub": "2x4\"", "condutor": "8x185", "protecao": "1x185"},
    {"categoria": "TI7", "demanda_min": 190, "demanda_max": 225, "disjuntor": 600,
     "eletroduto_sub": "2x4\"", "condutor": "8x240", "protecao": "1x240"},
]

# --------------------------------------------
# Tabela 8.4 - Dimensionamento coletivo 220/127V (PVC)
# --------------------------------------------
TABELA_84 = [
    {"demanda_min": 0, "demanda_max": 38, "disjuntor": 100, "circuito_eletroduto": "1x35", "circuito_bandeja": "1x25"},
    {"demanda_min": 38, "demanda_max": 47, "disjuntor": 125, "circuito_eletroduto": "1x50", "circuito_bandeja": "1x35"},
    {"demanda_min": 47, "demanda_max": 57, "disjuntor": 150, "circuito_eletroduto": "1x70", "circuito_bandeja": "1x50"},
    {"demanda_min": 57, "demanda_max": 66, "disjuntor": 175, "circuito_eletroduto": "1x95", "circuito_bandeja": "1x70"},
    {"demanda_min": 66, "demanda_max": 76, "disjuntor": 200, "circuito_eletroduto": "1x95", "circuito_bandeja": "1x70"},
    {"demanda_min": 76, "demanda_max": 85, "disjuntor": 225, "circuito_eletroduto": "1x120", "circuito_bandeja": "1x95"},
    {"demanda_min": 85, "demanda_max": 95, "disjuntor": 250, "circuito_eletroduto": "1x150", "circuito_bandeja": "1x95"},
    {"demanda_min": 95, "demanda_max": 114, "disjuntor": 300, "circuito_eletroduto": "1x185", "circuito_bandeja": "1x120"},
    {"demanda_min": 114, "demanda_max": 133, "disjuntor": 350, "circuito_eletroduto": "1x240", "circuito_bandeja": "1x150"},
    {"demanda_min": 133, "demanda_max": 150, "disjuntor": 400, "circuito_eletroduto": "2x150", "circuito_bandeja": "1x185"},
    {"demanda_min": 150, "demanda_max": 190, "disjuntor": 500, "circuito_eletroduto": "2x185", "circuito_bandeja": "1x240"},
    {"demanda_min": 190, "demanda_max": 225, "disjuntor": 600, "circuito_eletroduto": "2x240", "circuito_bandeja": "2x150"},
]

# --------------------------------------------
# Tabela 8.5 - Dimensionamento coletivo 220/127V (XLPE)
# --------------------------------------------
TABELA_85 = [
    {"demanda_min": 0, "demanda_max": 38, "disjuntor": 100, "circuito_eletroduto": "1x25", "circuito_bandeja": "N/A"},
    {"demanda_min": 38, "demanda_max": 47, "disjuntor": 125, "circuito_eletroduto": "1x35", "circuito_bandeja": "N/A"},
    {"demanda_min": 47, "demanda_max": 57, "disjuntor": 150, "circuito_eletroduto": "1x50", "circuito_bandeja": "N/A"},
    {"demanda_min": 57, "demanda_max": 66, "disjuntor": 175, "circuito_eletroduto": "1x70", "circuito_bandeja": "N/A"},
    {"demanda_min": 66, "demanda_max": 76, "disjuntor": 200, "circuito_eletroduto": "1x70", "circuito_bandeja": "N/A"},
    {"demanda_min": 76, "demanda_max": 85, "disjuntor": 225, "circuito_eletroduto": "1x95", "circuito_bandeja": "N/A"},
    {"demanda_min": 85, "demanda_max": 95, "disjuntor": 250, "circuito_eletroduto": "1x95", "circuito_bandeja": "N/A"},
    {"demanda_min": 95, "demanda_max": 114, "disjuntor": 300, "circuito_eletroduto": "1x120", "circuito_bandeja": "N/A"},
    {"demanda_min": 114, "demanda_max": 133, "disjuntor": 350, "circuito_eletroduto": "1x150", "circuito_bandeja": "N/A"},
    {"demanda_min": 133, "demanda_max": 150, "disjuntor": 400, "circuito_eletroduto": "1x185", "circuito_bandeja": "N/A"},
    {"demanda_min": 150, "demanda_max": 190, "disjuntor": 500, "circuito_eletroduto": "2x120", "circuito_bandeja": "N/A"},
    {"demanda_min": 190, "demanda_max": 225, "disjuntor": 600, "circuito_eletroduto": "2x185", "circuito_bandeja": "N/A"},
]

# --------------------------------------------
# Tabela 8.8 - Eletrodutos ramal aéreo
# --------------------------------------------
TABELA_88 = [
    {"demanda_min": 0, "demanda_max": 57, "diametro": "2\""},
    {"demanda_min": 57, "demanda_max": 85, "diametro": "2.5\""},
    {"demanda_min": 85, "demanda_max": 114, "diametro": "3\""},
    {"demanda_min": 114, "demanda_max": 133, "diametro": "4\""},
    {"demanda_min": 133, "demanda_max": 190, "diametro": "2x3\""},
    {"demanda_min": 190, "demanda_max": 225, "diametro": "2x3\""},
]

# --------------------------------------------
# Tabela 8.9 - Eletrodutos ramal subterrâneo
# --------------------------------------------
TABELA_89 = [
    {"demanda_min": 0, "demanda_max": 114, "diametro": "2x4\""},
    {"demanda_min": 114, "demanda_max": 999, "diametro": "A Light informará"},
]

# --------------------------------------------
# FUNÇÕES DE DIMENSIONAMENTO
# --------------------------------------------
def dimensionar_individual(demanda_kva, tensao="220/127V", fases=3):
    """Dimensiona entrada individual conforme Tabela 7.3"""
    for item in TABELA_73:
        if item["tensao"] == tensao and item["fases"] == fases:
            if item["demanda_min"] < demanda_kva <= item["demanda_max"]:
                return item
    return None

def dimensionar_individual_indireta(demanda_kva):
    """Dimensiona entrada individual com medição indireta (Tabela 7.4)"""
    for item in TABELA_74:
        if item["demanda_min"] < demanda_kva <= item["demanda_max"]:
            return item
    return None

def dimensionar_coletivo(demanda_kva, isolacao="PVC"):
    """Dimensiona circuito coletivo (Tabela 8.4 ou 8.5)"""
    tabela = TABELA_84 if isolacao == "PVC" else TABELA_85
    for item in tabela:
        if item["demanda_min"] < demanda_kva <= item["demanda_max"]:
            return item
    return None

def eletroduto_aereo(demanda_kva):
    """Retorna diâmetro do eletroduto para ramal aéreo (Tabela 8.8)"""
    for item in TABELA_88:
        if item["demanda_min"] < demanda_kva <= item["demanda_max"]:
            return item["diametro"]
    return None

def eletroduto_subterraneo(demanda_kva):
    """Retorna diâmetro do eletroduto para ramal subterrâneo (Tabela 8.9)"""
    for item in TABELA_89:
        if item["demanda_min"] < demanda_kva <= item["demanda_max"]:
            return item["diametro"]
    return None
