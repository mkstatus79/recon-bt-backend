from app.core.calculos.secao_b import (
    calcular_area_equivalente,
    calcular_potencia_equivalente,
    get_fator_seguranca,
    calcular_secao_b,
    exemplo_secao_b,
    exemplo_secao_b_com_areas_diferentes,
    exemplo_secao_b_com_chuveiros_maiores
)

print("=" * 60)
print("TESTE DO CÁLCULO DA SEÇÃO B - RECON-BT 2026")
print("=" * 60)

# Teste 1: Área equivalente
print("\n📋 TESTE 1 - Área equivalente")
print("-" * 40)
areas = [70, 82]
quantidades = [20, 20]
area_eq = calcular_area_equivalente(areas, quantidades)
print(f"Áreas: 20×70m² + 20×82m²")
print(f"Área equivalente: {area_eq:.2f} m² (esperado: 76 m²)")

# Teste 2: Potência equivalente
print("\n📋 TESTE 2 - Potência equivalente")
print("-" * 40)
potencias = [5.5, 7.5]
quantidades = [18, 18]
pot_eq = calcular_potencia_equivalente(potencias, quantidades)
print(f"Potencias: 18×5.5 kVA + 18×7.5 kVA")
print(f"Potência equivalente: {pot_eq:.2f} kVA (esperado: 6.5 kVA)")

# Teste 3: Fator de segurança
print("\n📋 TESTE 3 - Fator de segurança")
print("-" * 40)
print(f"4.4 kVA → {get_fator_seguranca(4.4)} (esperado: 1.00)")
print(f"5.5 kVA → {get_fator_seguranca(5.5)} (esperado: 1.10)")
print(f"6.5 kVA → {get_fator_seguranca(6.5)} (esperado: 1.20)")
print(f"8.0 kVA → {get_fator_seguranca(8.0)} (esperado: 1.20)")
print(f"11.0 kVA → {get_fator_seguranca(11.0)} (esperado: 1.30)")

# Teste 4: Exemplo 1 - 24 aptos 70m²
print("\n" + "=" * 60)
print("📋 EXEMPLO 1 - 24 apartamentos de 70m²")
print("=" * 60)
resultado1 = exemplo_secao_b()
print(f"Área equivalente: {resultado1['area_equivalente']} m²")
print(f"Total de UCs: {resultado1['total_ucs']}")
print(f"Demanda por UC: {resultado1['demanda_por_uc']} kVA")
print(f"Fator diversificação: {resultado1['fator_diversificacao']}")
print(f"Demanda base: {resultado1['demanda_agrupamento_base']} kVA")
print(f"Fator segurança: {resultado1['fator_seguranca']}")
print(f"Demanda final: {resultado1['demanda_agrupamento_final']} kVA")
print(f"Demanda serviço: {resultado1['demanda_servico']} kVA")
print(f"Demanda ramal: {resultado1['demanda_ramal']} kVA")

# Teste 5: Exemplo 2 - áreas diferentes
print("\n" + "=" * 60)
print("📋 EXEMPLO 2 - 20×70m² + 20×82m²")
print("=" * 60)
resultado2 = exemplo_secao_b_com_areas_diferentes()
print(f"Área equivalente: {resultado2['area_equivalente']} m²")
print(f"Total de UCs: {resultado2['total_ucs']}")
print(f"Demanda por UC: {resultado2['demanda_por_uc']} kVA")
print(f"Fator diversificação: {resultado2['fator_diversificacao']}")
print(f"Demanda base: {resultado2['demanda_agrupamento_base']} kVA")
print(f"Demanda final: {resultado2['demanda_agrupamento_final']} kVA")
print(f"Demanda ramal: {resultado2['demanda_ramal']} kVA")

# Teste 6: Exemplo 3 - chuveiros maiores
print("\n" + "=" * 60)
print("📋 EXEMPLO 3 - Chuveiros >4,4 kVA")
print("=" * 60)
resultado3 = exemplo_secao_b_com_chuveiros_maiores()
print(f"Área equivalente: {resultado3['area_equivalente']} m²")
print(f"Potência equivalente: {resultado3.get('potencia_equivalente', 'N/A')} kVA")
print(f"Fator segurança: {resultado3['fator_seguranca']}")
print(f"Demanda base: {resultado3['demanda_agrupamento_base']} kVA")
print(f"Demanda final: {resultado3['demanda_agrupamento_final']} kVA")
print(f"Demanda ramal: {resultado3['demanda_ramal']} kVA")

print("\n" + "=" * 60)
print("✅ Teste concluído!")
