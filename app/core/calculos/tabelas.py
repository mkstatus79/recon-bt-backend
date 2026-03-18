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
# Tabela 6.5 - Fatores de demanda para ar condicionado (residencial)
# --------------------------------------------
TABELA_65 = [
    {"faixa": "1 a 4", "num_min": 1, "num_max": 4, "fator": 100},
    {"faixa": "5 a 10", "num_min": 5, "num_max": 10, "fator": 70},
    {"faixa": "11 a 20", "num_min": 11, "num_max": 20, "fator": 60},
    {"faixa": "21 a 30", "num_min": 21, "num_max": 30, "fator": 55},
    {"faixa": "31 a 40", "num_min": 31, "num_max": 40, "fator": 53},
    {"faixa": "41 a 50", "num_min": 41, "num_max": 50, "fator": 52},
    {"faixa": "acima de 50", "num_min": 51, "num_max": 999, "fator": 50},
]

# --------------------------------------------
# Tabela 6.6 - Fatores de demanda para ar condicionado (não residencial)
# --------------------------------------------
TABELA_66 = [
    {"faixa": "1 a 10", "num_min": 1, "num_max": 10, "fator": 100},
    {"faixa": "11 a 20", "num_min": 11, "num_max": 20, "fator": 75},
    {"faixa": "21 a 30", "num_min": 21, "num_max": 30, "fator": 70},
    {"faixa": "31 a 40", "num_min": 31, "num_max": 40, "fator": 65},
    {"faixa": "41 a 50", "num_min": 41, "num_max": 50, "fator": 60},
    {"faixa": "51 a 80", "num_min": 51, "num_max": 80, "fator": 55},
    {"faixa": "acima de 80", "num_min": 81, "num_max": 999, "fator": 50},
]

# --------------------------------------------
# Tabela 6.7 - Fatores de demanda para ar condicionado central
# --------------------------------------------
TABELA_67 = [
    {"faixa": "1 a 10", "num_min": 1, "num_max": 10, "fator": 100},
    {"faixa": "11 a 20", "num_min": 11, "num_max": 20, "fator": 75},
    {"faixa": "21 a 30", "num_min": 21, "num_max": 30, "fator": 70},
    {"faixa": "31 a 40", "num_min": 31, "num_max": 40, "fator": 65},
    {"faixa": "41 a 50", "num_min": 41, "num_max": 50, "fator": 60},
    {"faixa": "51 a 80", "num_min": 51, "num_max": 80, "fator": 55},
    {"faixa": "acima de 80", "num_min": 81, "num_max": 999, "fator": 50},
]

# --------------------------------------------
# Tabela 6.8 - Fatores de demanda para motores elétricos
# --------------------------------------------
TABELA_68 = [
    {"num_motores": 1, "fator": 100.0},
    {"num_motores": 2, "fator": 75.0},
    {"num_motores": 3, "fator": 63.33},
    {"num_motores": 4, "fator": 57.5},
    {"num_motores": 5, "fator": 54.0},
    {"num_motores": 6, "fator": 50.0},
    {"num_motores": 7, "fator": 47.14},
    {"num_motores": 8, "fator": 45.0},
    {"num_motores": 9, "fator": 43.33},
    {"num_motores": 10, "fator": 42.0},
]

# --------------------------------------------
# Tabela 6.9 - Fatores de demanda para equipamentos especiais
# --------------------------------------------
TABELA_69 = {
    "solda": [
        {"faixa": "1", "num_min": 1, "num_max": 1, "fator": 100},
        {"faixa": "2 a 3", "num_min": 2, "num_max": 3, "fator": 70},
        {"faixa": "4 a 7", "num_min": 4, "num_max": 7, "fator": 60},
        {"faixa": "mais de 7", "num_min": 8, "num_max": 999, "fator": 50},
    ],
    "raio_x": [
        {"faixa": "1", "num_min": 1, "num_max": 1, "fator": 100},
        {"faixa": "2 a 5", "num_min": 2, "num_max": 5, "fator": 60},
        {"faixa": "6 a 10", "num_min": 6, "num_max": 10, "fator": 50},
        {"faixa": "mais de 10", "num_min": 11, "num_max": 999, "fator": 40},
    ],
}

# --------------------------------------------
# Tabela 6.11 - Demandas (kVA) por área (COM aquecimento elétrico)
# --------------------------------------------
TABELA_611 = [
    {"area": 10, "demanda": 0.93}, {"area": 11, "demanda": 0.93}, {"area": 12, "demanda": 0.93},
    {"area": 13, "demanda": 0.93}, {"area": 14, "demanda": 0.93}, {"area": 15, "demanda": 0.93},
    {"area": 16, "demanda": 0.93}, {"area": 17, "demanda": 0.93}, {"area": 18, "demanda": 0.93},
    {"area": 19, "demanda": 0.93}, {"area": 20, "demanda": 0.93}, {"area": 21, "demanda": 1.62},
    {"area": 22, "demanda": 1.62}, {"area": 23, "demanda": 1.62}, {"area": 24, "demanda": 1.62},
    {"area": 25, "demanda": 1.62}, {"area": 26, "demanda": 1.62}, {"area": 27, "demanda": 1.62},
    {"area": 28, "demanda": 1.62}, {"area": 29, "demanda": 1.62}, {"area": 30, "demanda": 1.62},
    {"area": 31, "demanda": 1.62}, {"area": 32, "demanda": 1.62}, {"area": 33, "demanda": 1.62},
    {"area": 34, "demanda": 1.62}, {"area": 35, "demanda": 1.62}, {"area": 36, "demanda": 1.62},
    {"area": 37, "demanda": 1.62}, {"area": 38, "demanda": 1.62}, {"area": 39, "demanda": 1.62},
    {"area": 40, "demanda": 1.62}, {"area": 41, "demanda": 1.62}, {"area": 42, "demanda": 1.62},
    {"area": 43, "demanda": 1.62}, {"area": 44, "demanda": 1.62}, {"area": 45, "demanda": 1.62},
    {"area": 46, "demanda": 1.62}, {"area": 47, "demanda": 1.62}, {"area": 48, "demanda": 1.62},
    {"area": 49, "demanda": 1.64}, {"area": 50, "demanda": 1.67}, {"area": 51, "demanda": 1.70},
    {"area": 52, "demanda": 1.73}, {"area": 53, "demanda": 1.76}, {"area": 54, "demanda": 1.79},
    {"area": 55, "demanda": 1.81}, {"area": 56, "demanda": 1.85}, {"area": 57, "demanda": 1.87},
    {"area": 58, "demanda": 1.91}, {"area": 59, "demanda": 1.93}, {"area": 60, "demanda": 1.97},
    {"area": 61, "demanda": 1.99}, {"area": 62, "demanda": 2.03}, {"area": 63, "demanda": 2.05},
    {"area": 64, "demanda": 2.08}, {"area": 65, "demanda": 2.11}, {"area": 66, "demanda": 2.14},
    {"area": 67, "demanda": 2.17}, {"area": 68, "demanda": 2.20}, {"area": 69, "demanda": 2.23},
    {"area": 70, "demanda": 2.26}, {"area": 71, "demanda": 2.28}, {"area": 72, "demanda": 2.32},
    {"area": 73, "demanda": 2.34}, {"area": 74, "demanda": 2.38}, {"area": 75, "demanda": 2.40},
    {"area": 76, "demanda": 2.42}, {"area": 77, "demanda": 2.46}, {"area": 78, "demanda": 2.48},
    {"area": 79, "demanda": 2.51}, {"area": 80, "demanda": 2.54}, {"area": 81, "demanda": 2.57},
    {"area": 82, "demanda": 2.60}, {"area": 83, "demanda": 2.63}, {"area": 84, "demanda": 2.65},
    {"area": 85, "demanda": 2.69}, {"area": 86, "demanda": 2.71}, {"area": 87, "demanda": 2.74},
    {"area": 88, "demanda": 2.77}, {"area": 89, "demanda": 2.80}, {"area": 90, "demanda": 2.82},
    {"area": 91, "demanda": 2.86}, {"area": 92, "demanda": 2.88}, {"area": 93, "demanda": 2.90},
    {"area": 94, "demanda": 2.94}, {"area": 95, "demanda": 2.96}, {"area": 96, "demanda": 2.99},
    {"area": 97, "demanda": 3.02}, {"area": 98, "demanda": 3.05}, {"area": 99, "demanda": 3.07},
    {"area": 100, "demanda": 3.11}, {"area": 101, "demanda": 3.13}, {"area": 102, "demanda": 3.16},
    {"area": 103, "demanda": 3.19}, {"area": 104, "demanda": 3.22}, {"area": 105, "demanda": 3.24},
    {"area": 106, "demanda": 3.26}, {"area": 107, "demanda": 3.30}, {"area": 108, "demanda": 3.32},
    {"area": 109, "demanda": 3.35}, {"area": 110, "demanda": 3.38}, {"area": 111, "demanda": 3.41},
    {"area": 112, "demanda": 3.43}, {"area": 113, "demanda": 3.47}, {"area": 114, "demanda": 3.49},
    {"area": 115, "demanda": 3.52}, {"area": 116, "demanda": 3.54}, {"area": 117, "demanda": 3.58},
    {"area": 118, "demanda": 3.60}, {"area": 119, "demanda": 3.62}, {"area": 120, "demanda": 3.65},
    {"area": 121, "demanda": 3.68}, {"area": 122, "demanda": 3.71}, {"area": 123, "demanda": 3.73},
    {"area": 124, "demanda": 3.77}, {"area": 125, "demanda": 3.79}, {"area": 126, "demanda": 3.82},
    {"area": 127, "demanda": 3.84}, {"area": 128, "demanda": 3.88}, {"area": 129, "demanda": 3.90},
    {"area": 130, "demanda": 3.92}, {"area": 131, "demanda": 3.95}, {"area": 132, "demanda": 3.98},
    {"area": 133, "demanda": 4.01}, {"area": 134, "demanda": 4.03}, {"area": 135, "demanda": 4.06},
    {"area": 136, "demanda": 4.09}, {"area": 137, "demanda": 4.12}, {"area": 138, "demanda": 4.14},
    {"area": 139, "demanda": 4.16}, {"area": 140, "demanda": 4.19}, {"area": 141, "demanda": 4.22},
    {"area": 142, "demanda": 4.25}, {"area": 143, "demanda": 4.27}, {"area": 144, "demanda": 4.30},
    {"area": 145, "demanda": 4.33}, {"area": 146, "demanda": 4.36}, {"area": 147, "demanda": 4.38},
    {"area": 148, "demanda": 4.40}, {"area": 149, "demanda": 4.44}, {"area": 150, "demanda": 4.46},
    {"area": 151, "demanda": 4.49}, {"area": 152, "demanda": 4.51}, {"area": 153, "demanda": 4.54},
    {"area": 154, "demanda": 4.57}, {"area": 155, "demanda": 4.60}, {"area": 156, "demanda": 4.62},
    {"area": 157, "demanda": 4.64}, {"area": 158, "demanda": 4.67}, {"area": 159, "demanda": 4.70},
    {"area": 160, "demanda": 4.73}, {"area": 161, "demanda": 4.75}, {"area": 162, "demanda": 4.78},
    {"area": 163, "demanda": 4.80}, {"area": 164, "demanda": 4.84}, {"area": 165, "demanda": 4.86},
    {"area": 166, "demanda": 4.88}, {"area": 167, "demanda": 4.91}, {"area": 168, "demanda": 4.93},
    {"area": 169, "demanda": 4.97}, {"area": 170, "demanda": 4.99}, {"area": 171, "demanda": 5.02},
    {"area": 172, "demanda": 5.04}, {"area": 173, "demanda": 5.06}, {"area": 174, "demanda": 5.10},
    {"area": 175, "demanda": 5.12}, {"area": 176, "demanda": 5.15}, {"area": 177, "demanda": 5.17},
    {"area": 178, "demanda": 5.20}, {"area": 179, "demanda": 5.22}, {"area": 180, "demanda": 5.26},
    {"area": 181, "demanda": 5.28}, {"area": 182, "demanda": 5.30}, {"area": 183, "demanda": 5.33},
    {"area": 184, "demanda": 5.35}, {"area": 185, "demanda": 5.39}, {"area": 186, "demanda": 5.41},
    {"area": 187, "demanda": 5.44}, {"area": 188, "demanda": 5.46}, {"area": 189, "demanda": 5.48},
    {"area": 190, "demanda": 5.51}, {"area": 191, "demanda": 5.54}, {"area": 192, "demanda": 5.57},
    {"area": 193, "demanda": 5.59}, {"area": 194, "demanda": 5.62}, {"area": 195, "demanda": 5.64},
    {"area": 196, "demanda": 5.66}, {"area": 197, "demanda": 5.69}, {"area": 198, "demanda": 5.72},
    {"area": 199, "demanda": 5.75}, {"area": 200, "demanda": 5.77},
]

# --------------------------------------------
# Tabela 6.12 - Demandas (kVA) por área (SEM aquecimento elétrico)
# --------------------------------------------
TABELA_612 = [
    {"area": 20, "demanda": 1.62}, {"area": 21, "demanda": 1.62}, {"area": 22, "demanda": 1.62},
    {"area": 23, "demanda": 1.62}, {"area": 24, "demanda": 1.62}, {"area": 25, "demanda": 1.62},
    {"area": 26, "demanda": 1.62}, {"area": 27, "demanda": 1.62}, {"area": 28, "demanda": 1.62},
    {"area": 29, "demanda": 1.62}, {"area": 30, "demanda": 1.62}, {"area": 31, "demanda": 1.62},
    {"area": 32, "demanda": 1.62}, {"area": 33, "demanda": 1.62}, {"area": 34, "demanda": 1.62},
    {"area": 35, "demanda": 1.62}, {"area": 36, "demanda": 1.62}, {"area": 37, "demanda": 1.62},
    {"area": 38, "demanda": 1.62}, {"area": 39, "demanda": 1.62}, {"area": 40, "demanda": 1.62},
    {"area": 41, "demanda": 1.62}, {"area": 42, "demanda": 1.62}, {"area": 43, "demanda": 1.62},
    {"area": 44, "demanda": 1.62}, {"area": 45, "demanda": 1.62}, {"area": 46, "demanda": 1.62},
    {"area": 47, "demanda": 1.62}, {"area": 48, "demanda": 1.62}, {"area": 49, "demanda": 1.64},
    {"area": 50, "demanda": 1.67}, {"area": 51, "demanda": 1.70}, {"area": 52, "demanda": 1.73},
    {"area": 53, "demanda": 1.76}, {"area": 54, "demanda": 1.79}, {"area": 55, "demanda": 1.81},
    {"area": 56, "demanda": 1.85}, {"area": 57, "demanda": 1.87}, {"area": 58, "demanda": 1.91},
    {"area": 59, "demanda": 1.93}, {"area": 60, "demanda": 1.97}, {"area": 61, "demanda": 1.99},
    {"area": 62, "demanda": 2.03}, {"area": 63, "demanda": 2.05}, {"area": 64, "demanda": 2.08},
    {"area": 65, "demanda": 2.11}, {"area": 66, "demanda": 2.14}, {"area": 67, "demanda": 2.17},
    {"area": 68, "demanda": 2.20}, {"area": 69, "demanda": 2.23}, {"area": 70, "demanda": 2.26},
    {"area": 71, "demanda": 2.28}, {"area": 72, "demanda": 2.32}, {"area": 73, "demanda": 2.34},
    {"area": 74, "demanda": 2.38}, {"area": 75, "demanda": 2.40}, {"area": 76, "demanda": 2.42},
    {"area": 77, "demanda": 2.46}, {"area": 78, "demanda": 2.48}, {"area": 79, "demanda": 2.51},
    {"area": 80, "demanda": 2.54}, {"area": 81, "demanda": 2.57}, {"area": 82, "demanda": 2.60},
    {"area": 83, "demanda": 2.63}, {"area": 84, "demanda": 2.65}, {"area": 85, "demanda": 2.69},
    {"area": 86, "demanda": 2.71}, {"area": 87, "demanda": 2.74}, {"area": 88, "demanda": 2.77},
    {"area": 89, "demanda": 2.80}, {"area": 90, "demanda": 2.82}, {"area": 91, "demanda": 2.86},
    {"area": 92, "demanda": 2.88}, {"area": 93, "demanda": 2.90}, {"area": 94, "demanda": 2.94},
    {"area": 95, "demanda": 2.96}, {"area": 96, "demanda": 2.99}, {"area": 97, "demanda": 3.02},
    {"area": 98, "demanda": 3.05}, {"area": 99, "demanda": 3.07}, {"area": 100, "demanda": 3.11},
    {"area": 101, "demanda": 3.13}, {"area": 102, "demanda": 3.16}, {"area": 103, "demanda": 3.19},
    {"area": 104, "demanda": 3.22}, {"area": 105, "demanda": 3.24}, {"area": 106, "demanda": 3.26},
    {"area": 107, "demanda": 3.30}, {"area": 108, "demanda": 3.32}, {"area": 109, "demanda": 3.35},
    {"area": 110, "demanda": 3.38}, {"area": 111, "demanda": 3.41}, {"area": 112, "demanda": 3.43},
    {"area": 113, "demanda": 3.47}, {"area": 114, "demanda": 3.49}, {"area": 115, "demanda": 3.52},
    {"area": 116, "demanda": 3.54}, {"area": 117, "demanda": 3.58}, {"area": 118, "demanda": 3.60},
    {"area": 119, "demanda": 3.62}, {"area": 120, "demanda": 3.65}, {"area": 121, "demanda": 3.68},
    {"area": 122, "demanda": 3.71}, {"area": 123, "demanda": 3.73}, {"area": 124, "demanda": 3.77},
    {"area": 125, "demanda": 3.79}, {"area": 126, "demanda": 3.82}, {"area": 127, "demanda": 3.84},
    {"area": 128, "demanda": 3.88}, {"area": 129, "demanda": 3.90}, {"area": 130, "demanda": 3.92},
    {"area": 131, "demanda": 3.95}, {"area": 132, "demanda": 3.98}, {"area": 133, "demanda": 4.01},
    {"area": 134, "demanda": 4.03}, {"area": 135, "demanda": 4.06}, {"area": 136, "demanda": 4.09},
    {"area": 137, "demanda": 4.12}, {"area": 138, "demanda": 4.14}, {"area": 139, "demanda": 4.16},
    {"area": 140, "demanda": 4.19}, {"area": 141, "demanda": 4.22}, {"area": 142, "demanda": 4.25},
    {"area": 143, "demanda": 4.27}, {"area": 144, "demanda": 4.30}, {"area": 145, "demanda": 4.33},
    {"area": 146, "demanda": 4.36}, {"area": 147, "demanda": 4.38}, {"area": 148, "demanda": 4.40},
    {"area": 149, "demanda": 4.44}, {"area": 150, "demanda": 4.46},
]

# --------------------------------------------
# Tabela 6.13 - Fatores de diversificação
# --------------------------------------------
TABELA_613 = [
    {"num_apartamentos": 4, "fator": 3.88}, {"num_apartamentos": 5, "fator": 4.84},
    {"num_apartamentos": 6, "fator": 5.80}, {"num_apartamentos": 7, "fator": 6.76},
    {"num_apartamentos": 8, "fator": 7.72}, {"num_apartamentos": 9, "fator": 8.68},
    {"num_apartamentos": 10, "fator": 9.64}, {"num_apartamentos": 11, "fator": 10.42},
    {"num_apartamentos": 12, "fator": 11.20}, {"num_apartamentos": 13, "fator": 11.98},
    {"num_apartamentos": 14, "fator": 12.76}, {"num_apartamentos": 15, "fator": 13.54},
    {"num_apartamentos": 16, "fator": 14.32}, {"num_apartamentos": 17, "fator": 15.10},
    {"num_apartamentos": 18, "fator": 15.88}, {"num_apartamentos": 19, "fator": 16.66},
    {"num_apartamentos": 20, "fator": 17.44}, {"num_apartamentos": 21, "fator": 18.05},
    {"num_apartamentos": 22, "fator": 18.66}, {"num_apartamentos": 23, "fator": 19.27},
    {"num_apartamentos": 24, "fator": 19.88}, {"num_apartamentos": 25, "fator": 20.49},
    {"num_apartamentos": 26, "fator": 21.10}, {"num_apartamentos": 27, "fator": 21.71},
    {"num_apartamentos": 28, "fator": 22.32}, {"num_apartamentos": 29, "fator": 22.93},
    {"num_apartamentos": 30, "fator": 23.54}, {"num_apartamentos": 31, "fator": 24.14},
    {"num_apartamentos": 32, "fator": 24.74}, {"num_apartamentos": 33, "fator": 25.34},
    {"num_apartamentos": 34, "fator": 25.94}, {"num_apartamentos": 35, "fator": 26.54},
    {"num_apartamentos": 36, "fator": 27.14}, {"num_apartamentos": 37, "fator": 27.74},
    {"num_apartamentos": 38, "fator": 28.34}, {"num_apartamentos": 39, "fator": 28.94},
    {"num_apartamentos": 40, "fator": 29.54}, {"num_apartamentos": 41, "fator": 30.14},
    {"num_apartamentos": 42, "fator": 30.74}, {"num_apartamentos": 43, "fator": 31.34},
    {"num_apartamentos": 44, "fator": 31.94}, {"num_apartamentos": 45, "fator": 32.54},
    {"num_apartamentos": 46, "fator": 33.10}, {"num_apartamentos": 47, "fator": 33.66},
    {"num_apartamentos": 48, "fator": 34.22}, {"num_apartamentos": 49, "fator": 34.78},
    {"num_apartamentos": 50, "fator": 35.34}, {"num_apartamentos": 51, "fator": 35.90},
    {"num_apartamentos": 52, "fator": 36.46}, {"num_apartamentos": 53, "fator": 37.02},
    {"num_apartamentos": 54, "fator": 37.58}, {"num_apartamentos": 55, "fator": 38.14},
    {"num_apartamentos": 56, "fator": 38.70}, {"num_apartamentos": 57, "fator": 39.26},
    {"num_apartamentos": 58, "fator": 39.82}, {"num_apartamentos": 59, "fator": 40.38},
    {"num_apartamentos": 60, "fator": 40.94}, {"num_apartamentos": 61, "fator": 41.50},
    {"num_apartamentos": 62, "fator": 42.06}, {"num_apartamentos": 63, "fator": 42.62},
    {"num_apartamentos": 64, "fator": 43.18}, {"num_apartamentos": 65, "fator": 43.74},
    {"num_apartamentos": 66, "fator": 44.30}, {"num_apartamentos": 67, "fator": 44.86},
    {"num_apartamentos": 68, "fator": 45.42}, {"num_apartamentos": 69, "fator": 45.98},
    {"num_apartamentos": 70, "fator": 46.54}, {"num_apartamentos": 71, "fator": 47.10},
    {"num_apartamentos": 72, "fator": 47.66}, {"num_apartamentos": 73, "fator": 48.22},
    {"num_apartamentos": 74, "fator": 48.78}, {"num_apartamentos": 75, "fator": 49.34},
    {"num_apartamentos": 76, "fator": 49.90}, {"num_apartamentos": 77, "fator": 50.46},
    {"num_apartamentos": 78, "fator": 51.02}, {"num_apartamentos": 79, "fator": 51.58},
    {"num_apartamentos": 80, "fator": 52.14}, {"num_apartamentos": 81, "fator": 52.70},
    {"num_apartamentos": 82, "fator": 53.26}, {"num_apartamentos": 83, "fator": 53.82},
    {"num_apartamentos": 84, "fator": 54.38}, {"num_apartamentos": 85, "fator": 54.94},
    {"num_apartamentos": 86, "fator": 55.50}, {"num_apartamentos": 87, "fator": 56.06},
    {"num_apartamentos": 88, "fator": 56.62}, {"num_apartamentos": 89, "fator": 57.18},
    {"num_apartamentos": 90, "fator": 57.74}, {"num_apartamentos": 91, "fator": 58.30},
    {"num_apartamentos": 92, "fator": 58.86}, {"num_apartamentos": 93, "fator": 59.42},
    {"num_apartamentos": 94, "fator": 59.98}, {"num_apartamentos": 95, "fator": 60.54},
    {"num_apartamentos": 96, "fator": 61.10}, {"num_apartamentos": 97, "fator": 61.66},
    {"num_apartamentos": 98, "fator": 62.22}, {"num_apartamentos": 99, "fator": 62.78},
    {"num_apartamentos": 100, "fator": 63.34},
]

# --------------------------------------------
# FUNÇÕES AUXILIARES
# --------------------------------------------

def get_potencia(aparelho_nome):
    """Busca potência na Tabela 6.1 por nome do aparelho"""
    busca = aparelho_nome.lower()
    for item in TABELA_61:
        if busca in item["aparelho"].lower():
            return item["potencia_va"]
        if "chuveiro" in busca and "chuveiro" in item["aparelho"].lower():
            import re
            numeros_busca = re.findall(r'\d+', busca)
            numeros_item = re.findall(r'\d+', item["aparelho"].lower())
            if numeros_busca and numeros_item and numeros_busca[0] in numeros_item:
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
        return 80

def get_fator_ar_residencial(num_aparelhos):
    """Retorna fator de demanda para ar condicionado residencial (Tabela 6.5)"""
    for item in TABELA_65:
        if item["num_min"] <= num_aparelhos <= item["num_max"]:
            return item["fator"]
    return 50

def get_fator_ar_nao_residencial(num_aparelhos):
    """Retorna fator de demanda para ar condicionado não residencial (Tabela 6.6)"""
    for item in TABELA_66:
        if item["num_min"] <= num_aparelhos <= item["num_max"]:
            return item["fator"]
    return 50

def get_fator_ar_central(num_aparelhos):
    """Retorna fator de demanda para ar condicionado central (Tabela 6.7)"""
    for item in TABELA_67:
        if item["num_min"] <= num_aparelhos <= item["num_max"]:
            return item["fator"]
    return 50

def get_fator_motores(num_motores):
    """Retorna fator de demanda para motores (Tabela 6.8)"""
    for item in TABELA_68:
        if item["num_motores"] == num_motores:
            return item["fator"]
    return 42.0

def get_fator_especial(tipo, quantidade):
    """Retorna fator de demanda para equipamentos especiais (Tabela 6.9)"""
    tabela = TABELA_69.get(tipo, TABELA_69["solda"])
    for item in tabela:
        if item["num_min"] <= quantidade <= item["num_max"]:
            return item["fator"]
    return 50

def mostrar_estatisticas():
    """Mostra estatísticas das tabelas carregadas"""
    print(f"Tabela 6.1: {len(TABELA_61)} aparelhos")
    print(f"Tabela 6.2: {len(TABELA_62)} conversões")
    print(f"Tabela 6.3: {len(TABELA_63)} tipos")
    print(f"Tabela 6.4: {len(TABELA_64)} faixas")
    print(f"Tabela 6.5: {len(TABELA_65)} faixas (ar residencial)")
    print(f"Tabela 6.6: {len(TABELA_66)} faixas (ar não residencial)")
    print(f"Tabela 6.7: {len(TABELA_67)} faixas (ar central)")
    print(f"Tabela 6.8: {len(TABELA_68)} faixas (motores)")
    print(f"Tabela 6.9: solda: {len(TABELA_69['solda'])} faixas, raio-x: {len(TABELA_69['raio_x'])} faixas")
    print(f"Tabela 6.11: {len(TABELA_611)} áreas (com aquecimento)")
    print(f"Tabela 6.12: {len(TABELA_612)} áreas (sem aquecimento)")
    print(f"Tabela 6.13: {len(TABELA_613)} fatores de diversificação")
