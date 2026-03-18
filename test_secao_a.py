from app.core.calculos.secao_a import Cargas, calcular_secao_a, exemplo_calculo

print("=" * 60)
print("TESTE DO CÁLCULO DA SEÇÃO A - RECON-BT 2026")
print("=" * 60)

# Exemplo do Fascículo 06 - Caso 01
print("\n📋 EXEMPLO 1 - Apartamento 70m² (Fascículo 06 - Caso 01)")
print("-" * 40)

resultado1 = exemplo_calculo()

print(f"D1 (Iluminação e tomadas): {resultado1['d1']['demanda']:.2f} kVA")
print(f"D2 (Aquecimento): {resultado1['d2']['demanda']:.2f} kVA")
print(f"D3 (Ar condicionado): {resultado1['d3']['demanda']:.2f} kVA")
print(f"D4 (Ar central): {resultado1['d4']['demanda']:.2f} kVA")
print(f"D5 (Motores): {resultado1['d5']['demanda']:.2f} kVA")
print(f"D6 (Especiais): {resultado1['d6']['demanda']:.2f} kVA")
print(f"\n📊 Demanda total: {resultado1['demanda_total_kva']:.2f} kVA")
print(f"📊 Demanda total (kW): {resultado1['demanda_total_kw']:.2f} kW")

print("\n" + "=" * 60)

# Exemplo do Fascículo 06 - Caso 02
print("\n📋 EXEMPLO 2 - Casa 300m² (Fascículo 06 - Caso 02)")
print("-" * 40)

cargas2 = Cargas()

# C1 - Iluminação (9.0 kVA - valor mínimo)
cargas2.adicionar_iluminacao(9.0)

# C2 - Aquecimento
cargas2.adicionar_aquecimento("chuveiro", 4.40)  # 3 chuveiros
cargas2.adicionar_aquecimento("chuveiro", 4.40)
cargas2.adicionar_aquecimento("chuveiro", 4.40)
cargas2.adicionar_aquecimento("torneira", 3.25)  # 2 torneiras
cargas2.adicionar_aquecimento("torneira", 3.25)
cargas2.adicionar_aquecimento("sauna", 9.00)     # 1 sauna

# C3 - Ar condicionado
cargas2.adicionar_ar("janela", 0.584, residencial=True)  # 2 janelas
cargas2.adicionar_ar("janela", 0.584, residencial=True)
cargas2.adicionar_ar("split", 0.877, residencial=True)   # 3 splits
cargas2.adicionar_ar("split", 0.877, residencial=True)
cargas2.adicionar_ar("split", 0.877, residencial=True)

# C5 - Motores
cargas2.adicionar_motor(1)    # 1 CV
cargas2.adicionar_motor(0.5)  # 1/2 CV
cargas2.adicionar_motor(0.25) # 1/4 CV (não reserva)

resultado2 = calcular_secao_a(cargas2)

print(f"D1: {resultado2['d1']['demanda']:.2f} kVA")
print(f"D2: {resultado2['d2']['demanda']:.2f} kVA")
print(f"D3: {resultado2['d3']['demanda']:.2f} kVA")
print(f"D4: {resultado2['d4']['demanda']:.2f} kVA")
print(f"D5: {resultado2['d5']['demanda']:.2f} kVA")
print(f"D6: {resultado2['d6']['demanda']:.2f} kVA")
print(f"\n📊 Demanda total: {resultado2['demanda_total_kva']:.2f} kVA")
print(f"📊 Demanda total (kW): {resultado2['demanda_total_kw']:.2f} kW")

print("\n" + "=" * 60)
print("✅ Teste concluído!")
