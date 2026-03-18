from app.core.dimensionamento.tabelas_dim import (
    dimensionar_individual, dimensionar_individual_indireta,
    dimensionar_coletivo, eletroduto_aereo, eletroduto_subterraneo
)

print("=" * 60)
print("TESTE DE DIMENSIONAMENTO - RECON-BT 2026")
print("=" * 60)

# Teste 1: Dimensionamento individual
print("\n📋 TESTE 1 - Entrada Individual")
print("-" * 40)
demandas = [10, 20, 35, 50, 70]
for d in demandas:
    resultado = dimensionar_individual(d)
    if resultado:
        print(f"Demanda {d:2d} kVA → Cat: {resultado['categoria']:3s} | Disj: {resultado['disjuntor']:3d}A | Cond: {resultado['condutor']}")

# Teste 2: Dimensionamento indireto
print("\n📋 TESTE 2 - Entrada Individual (Medição Indireta)")
print("-" * 40)
demandas_ind = [80, 100, 150, 200]
for d in demandas_ind:
    resultado = dimensionar_individual_indireta(d)
    if resultado:
        print(f"Demanda {d:3d} kVA → Cat: {resultado['categoria']:3s} | Disj: {resultado['disjuntor']:3d}A | Cond: {resultado['condutor']}")

# Teste 3: Dimensionamento coletivo
print("\n📋 TESTE 3 - Circuito Coletivo (PVC)")
print("-" * 40)
demandas_col = [30, 60, 90, 120, 180]
for d in demandas_col:
    resultado = dimensionar_coletivo(d, "PVC")
    if resultado:
        print(f"Demanda {d:3d} kVA → Disj: {resultado['disjuntor']:3d}A | Circuito: {resultado['circuito_eletroduto']}")

# Teste 4: Eletrodutos
print("\n📋 TESTE 4 - Eletrodutos")
print("-" * 40)
for d in [40, 70, 100, 150, 200]:
    aereo = eletroduto_aereo(d)
    sub = eletroduto_subterraneo(d)
    print(f"Demanda {d:3d} kVA → Aéreo: {aereo:6s} | Subterrâneo: {sub}")

print("\n✅ Teste concluído!")
