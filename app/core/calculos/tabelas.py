# ============================================
# TABELAS DO RECON-BT 2026 - FASCÍCULO 06
# ============================================

# --------------------------------------------
# Tabela 6.1 - Potências médias de aparelhos eletrodomésticos (VA)
# --------------------------------------------
TABELA_61 = [
    {"aparelho": "Aparelho de blu ray", "potencia_va": 13},
    {"aparelho": "Aparelho de DVD", "potencia_va": 16},
    {"aparelho": "Aparelho de som", "potencia_va": 120},
    {"aparelho": "Aquecedor de ambiente", "potencia_va": 1752},
    {"aparelho": "Ar-condicionado tipo janela ≤ 9.000 BTU/h", "potencia_va": 584},
    {"aparelho": "Ar-condicionado tipo janela 9.001-14.000 BTU/h", "potencia_va": 823},
    {"aparelho": "Ar-condicionado tipo janela > 14.000 BTU/h", "potencia_va": 1693},
    {"aparelho": "Ar-condicionado tipo split ≤ 10.000 BTU/h", "potencia_va": 645},
    {"aparelho": "Ar-condicionado tipo split 10.001-15.000 BTU/h", "potencia_va": 877},
    {"aparelho": "Ar-condicionado tipo split 15.001-20.000 BTU/h", "potencia_va": 1222},
    {"aparelho": "Ar-condicionado tipo split 20.001-30.000 BTU/h", "potencia_va": 1989},
    {"aparelho": "Ar-condicionado tipo split > 30.000 BTU/h", "potencia_va": 3076},
    {"aparelho": "Aspirador de pó", "potencia_va": 779},
    {"aparelho": "Batedeira", "potencia_va": 163},
    {"aparelho": "Boiler elétrico 200L - 2000W", "potencia_va": 2000},
    {"aparelho": "Boiler elétrico 200L - 2500W", "potencia_va": 2500},
    {"aparelho": "Boiler elétrico 200L - 3000W", "potencia_va": 3000},
    {"aparelho": "Cafeteira elétrica", "potencia_va": 219},
    {"aparelho": "Cafeteira expresso", "potencia_va": 794},
    {"aparelho": "Chaleira elétrica", "potencia_va": 941},
    {"aparelho": "Churrasqueira elétrica", "potencia_va": 3800},
    {"aparelho": "Chuveiro elétrico - 3200W", "potencia_va": 3200},
    {"aparelho": "Chuveiro elétrico - 4400W", "potencia_va": 4400},
    {"aparelho": "Chuveiro elétrico - 5500W", "potencia_va": 5500},
    {"aparelho": "Chuveiro elétrico - 6800W", "potencia_va": 6800},
    {"aparelho": "Chuveiro elétrico - 7500W", "potencia_va": 7500},
    {"aparelho": "Chuveiro elétrico - 7800W", "potencia_va": 7800},
    {"aparelho": "Computador", "potencia_va": 68},
    {"aparelho": "Enceradeira", "potencia_va": 489},
    {"aparelho": "Espremedor de frutas", "potencia_va": 59},
    {"aparelho": "Exaustor fogão", "potencia_va": 180},
    {"aparelho": "Ferro elétrico automático a seco - 1050W", "potencia_va": 1050},
    {"aparelho": "Ferro elétrico automático a vapor - 1200W", "potencia_va": 1200},
    {"aparelho": "Fogão elétrico - cook top (por queimador)", "potencia_va": 2484},
    {"aparelho": "Forno elétrico", "potencia_va": 543},
    {"aparelho": "Forno micro-ondas - 25L", "potencia_va": 1520},
    {"aparelho": "Freezer vertical frost free", "potencia_va": 82},
    {"aparelho": "Freezer vertical/horizontal", "potencia_va": 72},
    {"aparelho": "Frigobar", "potencia_va": 28},
    {"aparelho": "Fritadeira elétrica", "potencia_va": 908},
    {"aparelho": "Furadeira", "potencia_va": 255},
    {"aparelho": "Geladeira 1 porta", "potencia_va": 38},
    {"aparelho": "Geladeira 1 porta frost free", "potencia_va": 60},
    {"aparelho": "Geladeira 2 portas", "potencia_va": 73},
    {"aparelho": "Geladeira 2 portas frost free", "potencia_va": 86},
    {"aparelho": "Grill", "potencia_va": 640},
    {"aparelho": "Home theater", "potencia_va": 380},
    {"aparelho": "Impressora", "potencia_va": 16},
    {"aparelho": "Lavadora de louças", "potencia_va": 1677},
    {"aparelho": "Lavadora de roupas", "potencia_va": 160},
    {"aparelho": "Liquidificador", "potencia_va": 232},
    {"aparelho": "Máquina de costura", "potencia_va": 109},
    {"aparelho": "Monitor LCD", "potencia_va": 37},
    {"aparelho": "Multiprocessador", "potencia_va": 465},
    {"aparelho": "Notebook", "potencia_va": 22},
    {"aparelho": "Panela elétrica", "potencia_va": 1196},
    {"aparelho": "Prancha (chapinha)", "potencia_va": 36},
    {"aparelho": "Projetor", "potencia_va": 260},
    {"aparelho": "Sanduicheira", "potencia_va": 728},
    {"aparelho": "Secador de cabelo", "potencia_va": 1042},
    {"aparelho": "Secadora de roupa", "potencia_va": 2027},
    {"aparelho": "Tanquinho", "potencia_va": 76},
    {"aparelho": "Torneira elétrica - 3250W", "potencia_va": 3250},
    {"aparelho": "Torradeira", "potencia_va": 800},
    {"aparelho": "TV em cores - 14\" (tubo)", "potencia_va": 46},
    {"aparelho": "TV em cores - 29\" (tubo)", "potencia_va": 110},
    {"aparelho": "TV em cores - 32\" (LCD)", "potencia_va": 103},
    {"aparelho": "TV em cores - 40\" (LED)", "potencia_va": 90},
    {"aparelho": "TV em cores - 42\" (LED)", "potencia_va": 221},
    {"aparelho": "Ventilador de mesa", "potencia_va": 78},
    {"aparelho": "Ventilador de teto", "potencia_va": 79},
    {"aparelho": "Videogame", "potencia_va": 26},
]

# --------------------------------------------
# Tabela 6.2 - Conversão de CV para kVA
# --------------------------------------------
TABELA_62 = [
    {"cv": 0.25, "kva": 0.66},
    {"cv": 0.5, "kva": 0.87},
    {"cv": 0.75, "kva": 1.26},
    {"cv": 1, "kva": 1.52},
    {"cv": 1.5, "kva": 2.13},
    {"cv": 2, "kva": 2.70},
    {"cv": 3, "kva": 4.04},
    {"cv": 4, "kva": 5.03},
    {"cv": 5, "kva": 6.02},
    {"cv": 6, "kva": 7.06},
    {"cv": 7.5, "kva": 8.65},
    {"cv": 10, "kva": 11.54},
    {"cv": 12.5, "kva": 14.27},
    {"cv": 15, "kva": 17.12},
    {"cv": 20, "kva": 22.72},
    {"cv": 25, "kva": 28.32},
    {"cv": 30, "kva": 33.92},
    {"cv": 40, "kva": 44.30},
    {"cv": 50, "kva": 48.73},
    {"cv": 60, "kva": 57.78},
    {"cv": 75, "kva": 71.95},
    {"cv": 100, "kva": 95.54},
    {"cv": 125, "kva": 119.12},
    {"cv": 150, "kva": 142.70},
    {"cv": 175, "kva": 166.20},
    {"cv": 200, "kva": 189.60},
    {"cv": 250, "kva": 235.00},
]

# --------------------------------------------
# Tabela 6.3 - Fatores de demanda para iluminação e tomadas
# --------------------------------------------
TABELA_63 = [
    {"tipo": "Auditórios, salões para exposições", "carga_minima_kva_m2": 0.015, "faixa": "80% para todos"},
    {"tipo": "Bancos, postos de serviços públicos", "carga_minima_kva_m2": 0.050, "faixa": "80% para todos"},
    {"tipo": "Barbearias, salões de beleza", "carga_minima_kva_m2": 0.020, "faixa": "80% para todos"},
    {"tipo": "Clubes", "carga_minima_kva_m2": 0.020, "faixa": "80% para todos"},
    {"tipo": "Escolas", "carga_minima_kva_m2": 0.030, "faixa": "80% primeiros 12 kVA, 50% excedente"},
    {"tipo": "Escritórios", "carga_minima_kva_m2": 0.050, "faixa": "80% primeiros 20 kVA, 60% excedente"},
    {"tipo": "Garagens, áreas de serviço", "carga_minima_kva_m2": 0.005, "faixa": "80% primeiros 10 kVA, 25% excedente"},
    {"tipo": "Hospitais", "carga_minima_kva_m2": 0.020, "faixa": "40% primeiros 50 kVA, 20% excedente"},
    {"tipo": "Hotéis, motéis", "carga_minima_kva_m2": 0.020, "faixa": "50% primeiros 20 kVA, 40% seg 80 kVA, 30% excedente"},
    {"tipo": "Igrejas", "carga_minima_kva_m2": 0.015, "faixa": "80% para todos"},
    {"tipo": "Lojas", "carga_minima_kva_m2": 0.020, "faixa": "80% para todos"},
    {"tipo": "Residencial", "carga_minima_kva_m2": 0.030, "faixa": "tabela progressiva de 80% a 24%"},
    {"tipo": "Restaurantes, bares", "carga_minima_kva_m2": 0.020, "faixa": "80% para todos"},
]

# --------------------------------------------
# Tabela 6.4 - Fatores de demanda para aquecimento
# --------------------------------------------
TABELA_64 = [
    {"num_aparelhos": 1, "fator": 100},
    {"num_aparelhos": 2, "fator": 75},
    {"num_aparelhos": 3, "fator": 70},
    {"num_aparelhos": 4, "fator": 66},
    {"num_aparelhos": 5, "fator": 62},
    {"num_aparelhos": 6, "fator": 59},
    {"num_aparelhos": 7, "fator": 56},
    {"num_aparelhos": 8, "fator": 53},
    {"num_aparelhos": 9, "fator": 51},
    {"num_aparelhos": 10, "fator": 49},
    {"num_aparelhos": 11, "fator": 47},
    {"num_aparelhos": 12, "fator": 45},
    {"num_aparelhos": 13, "fator": 43},
    {"num_aparelhos": 14, "fator": 41},
    {"num_aparelhos": 15, "fator": 40},
    {"num_aparelhos": 16, "fator": 39},
    {"num_aparelhos": 17, "fator": 38},
    {"num_aparelhos": 18, "fator": 37},
    {"num_aparelhos": 19, "fator": 36},
    {"num_aparelhos": 20, "fator": 35},
    {"num_aparelhos": 21, "fator": 34},
    {"num_aparelhos": 22, "fator": 33},
    {"num_aparelhos": 23, "fator": 32},
    {"num_aparelhos": 24, "fator": 32},
    {"num_aparelhos": 25, "fator": 30},
]

# --------------------------------------------
# FUNÇÕES AUXILIARES - CORRIGIDAS
# --------------------------------------------

def get_potencia(aparelho_nome):
    """Busca potência na Tabela 6.1 por nome do aparelho"""
    for item in TABELA_61:
        # Verifica se o nome do aparelho contém a palavra-chave
        if aparelho_nome.lower() in item["aparelho"].lower():
            return item["potencia_va"]
        # Verifica também por números (ex: "4400" no caso do chuveiro)
        if str(aparelho_nome).replace("W", "") in item["aparelho"]:
            return item["potencia_va"]
    return None

def get_conversao_cv_kva(cv):
    """Retorna kVA para um dado CV (Tabela 6.2)"""
    for item in TABELA_62:
        if item["cv"] == cv:
            return item["kva"]
    return None

def get_fator_aquecimento(num_aparelhos):
    """Retorna fator de demanda para aquecimento (Tabela 6.4)"""
    for item in TABELA_64:
        if item["num_aparelhos"] == num_aparelhos:
            return item["fator"]
    # Se não encontrar (acima de 25), retorna 30%
    return 30

def get_fator_iluminacao(tipo, carga_kva):
    """Calcula fator de demanda para iluminação (Tabela 6.3)"""
    if tipo == "Residencial":
        if carga_kva <= 1:
            return 80
        elif carga_kva <= 2:
            return 75
        elif carga_kva <= 3:
            return 65
        elif carga_kva <= 4:
            return 60
        elif carga_kva <= 5:
            return 50
        elif carga_kva <= 6:
            return 45
        elif carga_kva <= 7:
            return 40
        elif carga_kva <= 8:
            return 35
        elif carga_kva <= 9:
            return 30
        elif carga_kva <= 10:
            return 27
        else:
            return 24
    else:
        # Para outros tipos, retorna 80% como padrão
        return 80

# --------------------------------------------
# FUNÇÃO PARA VERIFICAR CONTAGEM DAS TABELAS
# --------------------------------------------
def mostrar_estatisticas():
    """Mostra estatísticas das tabelas carregadas"""
    print(f"Tabela 6.1: {len(TABELA_61)} aparelhos")
    print(f"Tabela 6.2: {len(TABELA_62)} conversões")
    print(f"Tabela 6.3: {len(TABELA_63)} tipos")
    print(f"Tabela 6.4: {len(TABELA_64)} faixas")

