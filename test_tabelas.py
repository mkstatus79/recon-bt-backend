from app.core.calculos.tabelas import (
    TABELA_61, TABELA_62, TABELA_63, TABELA_64, TABELA_65, TABELA_66, TABELA_67, TABELA_68, TABELA_69,
    get_potencia, get_conversao_cv_kva, get_fator_aquecimento, get_fator_iluminacao,
    get_fator_ar_residencial, get_fator_ar_nao_residencial, get_fator_ar_central,
    get_fator_motores, get_fator_especial, mostrar_estatisticas
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

print(f"\n📊 TABELA 6.5 - AR CONDICIONADO RESIDENCIAL:")
print(f"  • 3 aparelhos: {get_fator_ar_residencial(3)}%")
print(f"  • 8 aparelhos: {get_fator_ar_residencial(8)}%")
print(f"  • 15 aparelhos: {get_fator_ar_residencial(15)}%")

print(f"\n📊 TABELA 6.6 - AR CONDICIONADO NÃO RESIDENCIAL:")
print(f"  • 5 aparelhos: {get_fator_ar_nao_residencial(5)}%")
print(f"  • 15 aparelhos: {get_fator_ar_nao_residencial(15)}%")
print(f"  • 25 aparelhos: {get_fator_ar_nao_residencial(25)}%")

print(f"\n📊 TABELA 6.7 - AR CENTRAL:")
print(f"  • 2 aparelhos: {get_fator_ar_central(2)}%")
print(f"  • 12 aparelhos: {get_fator_ar_central(12)}%")

print(f"\n📊 TABELA 6.8 - MOTORES:")
print(f"  • 1 motor: {get_fator_motores(1)}%")
print(f"  • 3 motores: {get_fator_motores(3)}%")
print(f"  • 5 motores: {get_fator_motores(5)}%")
print(f"  • 8 motores: {get_fator_motores(8)}%")

print(f"\n📊 TABELA 6.9 - EQUIPAMENTOS ESPECIAIS:")
print(f"  • 1 máquina de solda: {get_fator_especial('solda', 1)}%")
print(f"  • 4 máquinas de solda: {get_fator_especial('solda', 4)}%")
print(f"  • 1 aparelho de raio-x: {get_fator_especial('raio_x', 1)}%")
print(f"  • 3 aparelhos de raio-x: {get_fator_especial('raio_x', 3)}%")

print("\n✅ Teste concluído com sucesso!")
