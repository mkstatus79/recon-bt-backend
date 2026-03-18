from app.core.calculos.tabelas import (
    TABELA_61, TABELA_62, TABELA_63, TABELA_64,
    get_potencia, get_conversao_cv_kva, get_fator_aquecimento,
    get_fator_iluminacao, mostrar_estatisticas
)

print("=" * 50)
print("TESTE DAS TABELAS RECON-BT")
print("=" * 50)

print("\n📊 ESTATÍSTICAS DAS TABELAS:")
mostrar_estatisticas()

print(f"\n📊 TABELA 6.1 - TESTE DE BUSCA:")
print(f"  • Chuveiro 4400W: {get_potencia('chuveiro 4400')} VA")
print(f"  • Chuveiro 5500W: {get_potencia('chuveiro 5500')} VA")
print(f"  • Geladeira 2 portas: {get_potencia('geladeira 2 portas')} VA")
print(f"  • Primeiro item: {TABELA_61[0]['aparelho']} - {TABELA_61[0]['potencia_va']} VA")

print(f"\n📊 TABELA 6.2 - CONVERSÃO CV → kVA:")
print(f"  • 5 CV = {get_conversao_cv_kva(5)} kVA")
print(f"  • 10 CV = {get_conversao_cv_kva(10)} kVA")
print(f"  • 20 CV = {get_conversao_cv_kva(20)} kVA")

print(f"\n📊 TABELA 6.3 - FATORES ILUMINAÇÃO:")
print(f"  • Escolas: {TABELA_63[4]['carga_minima_kva_m2']} kVA/m²")
print(f"  • Residencial 3 kVA: {get_fator_iluminacao('Residencial', 3)}%")
print(f"  • Residencial 8 kVA: {get_fator_iluminacao('Residencial', 8)}%")
print(f"  • Escritório (padrão): {get_fator_iluminacao('Escritório', 10)}%")

print(f"\n📊 TABELA 6.4 - FATORES AQUECIMENTO:")
print(f"  • 1 chuveiro: {get_fator_aquecimento(1)}%")
print(f"  • 8 chuveiros: {get_fator_aquecimento(8)}%")
print(f"  • 25 chuveiros: {get_fator_aquecimento(25)}%")

print("\n✅ Teste concluído com sucesso!")

