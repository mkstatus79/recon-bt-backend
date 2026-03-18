# ============================================
# CÁLCULO DA SEÇÃO A - RECON-BT 2026
# ============================================

from .tabelas import (
    get_potencia, get_conversao_cv_kva, get_fator_aquecimento,
    get_fator_iluminacao, get_fator_ar_residencial, get_fator_ar_nao_residencial,
    get_fator_ar_central, get_fator_motores, get_fator_especial
)

# --------------------------------------------
# CLASSE PARA ARMAZENAR CARGAS
# --------------------------------------------
class Cargas:
    def __init__(self):
        self.iluminacao_tomadas_kva = 0      # C1
        self.aquecimento = []                 # C2 - lista de (tipo, potencia_kva)
        self.ar_condicionado = []              # C3 - lista de (tipo, potencia_kva, residencial)
        self.ar_central = []                   # C4 - lista de potencias_kva
        self.motores = []                      # C5 - lista de potencias_cv
        self.especiais = []                    # C6 - lista de (tipo, potencia_kva)
    
    def adicionar_iluminacao(self, valor):
        self.iluminacao_tomadas_kva = valor
    
    def adicionar_aquecimento(self, tipo, potencia_kva):
        self.aquecimento.append((tipo, potencia_kva))
    
    def adicionar_ar(self, tipo, potencia_kva, residencial=True):
        self.ar_condicionado.append((tipo, potencia_kva, residencial))
    
    def adicionar_ar_central(self, potencia_kva):
        self.ar_central.append(potencia_kva)
    
    def adicionar_motor(self, potencia_cv):
        self.motores.append(potencia_cv)
    
    def adicionar_especial(self, tipo, potencia_kva):
        self.especiais.append((tipo, potencia_kva))

# --------------------------------------------
# FUNÇÃO PRINCIPAL DE CÁLCULO DA SEÇÃO A
# --------------------------------------------
def calcular_secao_a(cargas, tipo_ocupacao="Residencial"):
    """
    Calcula a demanda total conforme Seção A do RECON-BT
    D = D1 + D2 + D3 + D4 + D5 + D6
    
    Args:
        cargas: objeto da classe Cargas
        tipo_ocupacao: "Residencial", "Comercial", etc.
    
    Returns:
        dict com resultados parciais e total
    """
    
    resultados = {}
    
    # ----------------------------------------
    # D1 - Iluminação e tomadas
    # ----------------------------------------
    carga_d1 = cargas.iluminacao_tomadas_kva
    fator_d1 = get_fator_iluminacao(tipo_ocupacao, carga_d1)
    d1 = carga_d1 * fator_d1 / 100
    resultados['d1'] = {
        'carga': carga_d1,
        'fator': fator_d1,
        'demanda': d1
    }
    
    # ----------------------------------------
    # D2 - Aquecimento
    # ----------------------------------------
    d2_total = 0
    if cargas.aquecimento:
        # Agrupa por tipo
        tipos = {}
        for tipo, pot in cargas.aquecimento:
            if tipo not in tipos:
                tipos[tipo] = []
            tipos[tipo].append(pot)
        
        for tipo, potencias in tipos.items():
            qtd = len(potencias)
            fator = get_fator_aquecimento(qtd)
            soma = sum(potencias)
            demanda_parcial = soma * fator / 100
            d2_total += demanda_parcial
    
    resultados['d2'] = {
        'total_aparelhos': len(cargas.aquecimento),
        'demanda': d2_total
    }
    
    # ----------------------------------------
    # D3 - Ar condicionado tipo janela/split
    # ----------------------------------------
    d3_total = 0
    if cargas.ar_condicionado:
        # Separa residencial e não residencial
        residenciais = [p for t, p, r in cargas.ar_condicionado if r]
        nao_residenciais = [p for t, p, r in cargas.ar_condicionado if not r]
        
        if residenciais:
            qtd = len(residenciais)
            fator = get_fator_ar_residencial(qtd)
            soma = sum(residenciais)
            d3_total += soma * fator / 100
        
        if nao_residenciais:
            qtd = len(nao_residenciais)
            fator = get_fator_ar_nao_residencial(qtd)
            soma = sum(nao_residenciais)
            d3_total += soma * fator / 100
    
    resultados['d3'] = {
        'total_aparelhos': len(cargas.ar_condicionado),
        'demanda': d3_total
    }
    
    # ----------------------------------------
    # D4 - Ar condicionado central
    # ----------------------------------------
    d4_total = 0
    if cargas.ar_central:
        qtd = len(cargas.ar_central)
        fator = get_fator_ar_central(qtd)
        soma = sum(cargas.ar_central)
        d4_total = soma * fator / 100
    
    resultados['d4'] = {
        'total_aparelhos': len(cargas.ar_central),
        'demanda': d4_total
    }
    
    # ----------------------------------------
    # D5 - Motores elétricos
    # ----------------------------------------
    d5_total = 0
    if cargas.motores:
        # Converte CV para kVA
        potencias_kva = []
        for cv in cargas.motores:
            kva = get_conversao_cv_kva(cv)
            if kva:
                potencias_kva.append(kva)
        
        qtd = len(potencias_kva)
        fator = get_fator_motores(qtd)
        soma = sum(potencias_kva)
        
        # Verifica condição especial (maior motor)
        if potencias_kva:
            maior_motor = max(potencias_kva)
            demanda_calculada = soma * fator / 100
            if maior_motor > demanda_calculada:
                d5_total = maior_motor
            else:
                d5_total = demanda_calculada
    
    resultados['d5'] = {
        'total_motores': len(cargas.motores),
        'demanda': d5_total
    }
    
    # ----------------------------------------
    # D6 - Equipamentos especiais
    # ----------------------------------------
    d6_total = 0
    if cargas.especiais:
        # Agrupa por tipo
        tipos = {}
        for tipo, pot in cargas.especiais:
            if tipo not in tipos:
                tipos[tipo] = []
            tipos[tipo].append(pot)
        
        for tipo, potencias in tipos.items():
            qtd = len(potencias)
            fator = get_fator_especial(tipo, qtd)
            soma = sum(potencias)
            demanda_parcial = soma * fator / 100
            d6_total += demanda_parcial
    
    resultados['d6'] = {
        'total_equipamentos': len(cargas.especiais),
        'demanda': d6_total
    }
    
    # ----------------------------------------
    # Demanda total
    # ----------------------------------------
    demanda_total = d1 + d2_total + d3_total + d4_total + d5_total + d6_total
    
    resultados['demanda_total_kva'] = demanda_total
    resultados['demanda_total_kw'] = demanda_total * 0.92  # fator de potência médio
    
    return resultados

# --------------------------------------------
# FUNÇÃO PARA EXEMPLO PRÁTICO
# --------------------------------------------
def exemplo_calculo():
    """Exemplo de cálculo baseado no Fascículo 06 - Caso 01"""
    
    cargas = Cargas()
    
    # C1 - Iluminação e tomadas
    cargas.adicionar_iluminacao(2.50)
    
    # C2 - Aquecimento
    cargas.adicionar_aquecimento("chuveiro", 4.40)
    cargas.adicionar_aquecimento("torneira", 3.25)
    
    # C3 - Ar condicionado
    cargas.adicionar_ar("janela", 0.584, residencial=True)
    cargas.adicionar_ar("janela", 0.584, residencial=True)
    
    # C5 - Motores
    cargas.adicionar_motor(1)  # 1 CV
    
    # Calcular
    resultado = calcular_secao_a(cargas)
    
    return resultado
