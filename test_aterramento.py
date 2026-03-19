from app.core.dimensionamento.aterramento import (
    num_hastes_aterramento, secao_condutor_protecao,
    capacidade_interrupcao, dimensionar_aterramento_completo
)

print("=" * 60)
print("TESTE DE DIMENSIONAMENTO DE ATERRAMENTO")
print("=" * 60)

# Teste 1: Número de hastes
print("\n📋 TESTE 1 - Número de hastes")
print("-" * 40)
casos = [
    ("INDIVIDUAL", 1, 20, "Casa pequena"),
    ("INDIVIDUAL", 1, 100, "Casa grande"),
    ("INDIVIDUAL", 1, 200, "Comércio"),
    ("COLETIVA", 4, 50, "4 aptos"),
    ("COLETIVA", 10, 150, "10 aptos"),
    ("COLETIVA", 20, 300, "20 aptos"),
]

for tipo, ucs, demanda, desc in casos:
    hastes = num_hastes_aterramento(tipo, ucs, demanda)
    print(f"{desc:15} → {hastes} hastes")

# Teste 2: Condutor de proteção
print("\n📋 TESTE 2 - Condutor de proteção")
print("-" * 40)
for fase in [10, 25, 50, 95, 185, 240]:
    prot = secao_condutor_protecao(fase)
    print(f"Fase {fase:3} mm² → Proteção: {prot} mm²")

# Teste 3: Capacidade de interrupção
print("\n📋 TESTE 3 - Capacidade de interrupção (kA)")
print("-" * 40)
print("Bitola | Aéreo | Sub Radial | Sub Reticulado")
print("-" * 40)
for bitola in [25, 50, 95, 120, 185]:
    a = capacidade_interrupcao(bitola, "aereo")
    r = capacidade_interrupcao(bitola, "sub_radial")
    g = capacidade_interrupcao(bitola, "sub_reticulado")
    print(f"{bitola:5}  | {a:5} | {r:9} | {g:13}")

# Teste 4: Dimensionamento completo
print("\n📋 TESTE 4 - Dimensionamento completo")
print("-" * 40)
dados = {
    "tipo_entrada": "COLETIVA",
    "num_ucs": 24,
    "demanda_kva": 150,
    "secao_fase": 95,
    "tipo_rede": "aereo"
}

resultado = dimensionar_aterramento_completo(dados)
print(f"Número de hastes: {resultado['num_hastes']}")
print(f"Tipo de haste: {resultado['tipo_haste']}")
print(f"Condutor interligação: {resultado['condutor_interligacao']} mm²")
print(f"Condutor proteção: {resultado['condutor_protecao']} mm²")
print(f"Capacidade disjuntor: {resultado['capacidade_disjuntor_ka']} kA")
for obs in resultado['observacoes']:
    print(f"→ {obs}")

print("\n✅ Teste concluído!")
