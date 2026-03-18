from app.core.calculos.tabelas import (
    TABELA_61, TABELA_62, TABELA_63, TABELA_64,
    get_potencia, get_conversao_cv_kva, get_fator_aquecimento
)

print("=" * 50)
print("TESTE DAS TABELAS RECON-BT")
print("=" * 50)

print(f"\n📊 TABELA 6.1: {len(TABELA_61)} aparelhos")
print(f"  • Chuveiro 4400W: {get_potencia('chuveiro 4400')} VA")
print(f"  • Primeiro: {TABELA_61[0]['aparelho']} - {TABELA_61[0]['potencia_va']} VA")

print(f"\n📊 TABELA 6.2: {len(TABELA_62)} conversões")
print(f"  • 5 CV = {get_conversao_cv_kva(5)} kVA")
print(f"  • 10 CV = {get_conversao_cv_kva(10)} kVA")

print(f"\n📊 TABELA 6.3: {len(TABELA_63)} tipos")
print(f"  • Escolas: {TABELA_63[4]['carga_minima_kva_m2']} kVA/m²")

print(f"\n📊 TABELA 6.4: {len(TABELA_64)} faixas")
print(f"  • 8 chuveiros: {get_fator_aquecimento(8)}%")
print(f"  • 25 chuveiros: {get_fator_aquecimento(25)}%")

print("\n✅ Teste concluído!")
