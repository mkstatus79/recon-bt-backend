from app.core.validacao.regras import (
    ValidadorLimiteCarga,
    ValidadorAprovacaoPrevia,
    ValidadorART,
    ValidadorProjetoSimplificado,
    GestorVistoria,
    ValidadorMateriais,
    ValidadorReconBT
)
import datetime

print("=" * 60)
print("TESTE DO MÓDULO DE VALIDAÇÃO DE REGRAS")
print("=" * 60)

# Teste REG-BT-001
print("\n📋 REG-BT-001 - Limite de Carga BT")
print("-" * 40)
casos = [
    ("INDIVIDUAL", 70, "RESIDENCIAL"),
    ("INDIVIDUAL", 80, "RESIDENCIAL"),
    ("COLETIVA", 250, "RESIDENCIAL"),
    ("COLETIVA", 250, "NAO_RESIDENCIAL"),
]

for tipo, carga, ocupacao in casos:
    resultado = ValidadorLimiteCarga.validar(tipo, carga, ocupacao)
    status = "✅" if resultado["valido"] else "❌"
    print(f"{status} {tipo} {carga}kVA ({ocupacao}): {resultado['mensagem']}")

# Teste REG-BT-004
print("\n📋 REG-BT-004 - Projeto Simplificado")
print("-" * 40)
casos = [
    (6, 1, 15, "Vila com 6 casas"),
    (8, 1, 15, "8 apartamentos"),
    (6, 2, 15, "6 aptos + 2 serviços"),
]

for ucs, servico, demanda, desc in casos:
    resultado = ValidadorProjetoSimplificado.validar(ucs, servico, demanda)
    tipo = "✅ SIMPLIFICADO" if resultado["elegivel"] else "❌ COMPLETO"
    print(f"{tipo} - {desc}")

# Teste REG-MAT-006
print("\n📋 REG-MAT-006 - Validação de Materiais")
print("-" * 40)
materiais = [
    {"tipo": "CAIXAS", "fabricante": "MULTIPOL"},
    {"tipo": "DISJUNTORES", "fabricante": "FABRICANTE_INEXISTENTE"},
    {"tipo": "POSTES", "fabricante": "PLASSON"},
]

resultado = ValidadorMateriais.validar_lista_materiais(materiais)
print(f"Validação geral: {'✅ OK' if resultado['valido'] else '❌ COM BLOQUEIOS'}")
for r in resultado['resultados']:
    status = "✅" if r['valido'] else "❌"
    print(f"  {status} {r['tipo']}: {r['fabricante']}")

print("\n✅ Teste concluído!")
