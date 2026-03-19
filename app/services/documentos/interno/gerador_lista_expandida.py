# ============================================
# GERADOR DE LISTA DE MATERIAIS EXPANDIDA
# Inclui custos, fornecedores e códigos
# USO INTERNO - NÃO ENVIAR PARA LIGHT
# ============================================

import csv
import json
import datetime
from pathlib import Path

class GeradorListaExpandida:
    """
    Gera lista completa de materiais com:
    - Códigos de fabricante
    - Preços estimados
    - Fornecedores sugeridos
    - Quantidades por etapa
    """
    
    def __init__(self):
        self.output_dir = Path(__file__).parent.parent / "output" / "interno"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_lista(self, dimensionamento, fornecedores=None):
        """
        Gera lista expandida com custos
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Base de preços (simulada)
        precos_base = {
            'disjuntor_175A': 850.00,
            'disjuntor_200A': 950.00,
            'disjuntor_225A': 1100.00,
            'cabo_95mm2': 45.50,
            'cabo_50mm2': 28.90,
            'cabo_35mm2': 22.50,
            'caixa_csm600': 1250.00,
            'caixa_cpg200': 780.00,
            'haste_5_8': 85.00,
            'eletroduto_3': 32.50,
            'eletroduto_4': 45.00,
        }
        
        # Materiais baseados no dimensionamento
        materiais = [
            {
                'codigo': 'DIS-175',
                'descricao': 'Disjuntor tripolar 175A',
                'fabricante': 'Schneider',
                'quantidade': 1,
                'unidade': 'un',
                'preco_unit': precos_base['disjuntor_175A'],
                'total': precos_base['disjuntor_175A'],
                'aplicacao': 'Proteção geral'
            },
            {
                'codigo': 'CAB-95',
                'descricao': 'Cabo de cobre 95mm² PVC',
                'fabricante': 'Prysmian',
                'quantidade': 120,
                'unidade': 'm',
                'preco_unit': precos_base['cabo_95mm2'],
                'total': 120 * precos_base['cabo_95mm2'],
                'aplicacao': 'Ramal de entrada'
            },
            {
                'codigo': 'CAB-50',
                'descricao': 'Cabo de cobre 50mm² (proteção)',
                'fabricante': 'Prysmian',
                'quantidade': 50,
                'unidade': 'm',
                'preco_unit': precos_base['cabo_50mm2'],
                'total': 50 * precos_base['cabo_50mm2'],
                'aplicacao': 'Condutor de proteção'
            },
            {
                'codigo': 'CX-CSM600',
                'descricao': 'Caixa CSM600',
                'fabricante': 'Multipol',
                'quantidade': 1,
                'unidade': 'un',
                'preco_unit': precos_base['caixa_csm600'],
                'total': precos_base['caixa_csm600'],
                'aplicacao': 'Medição'
            },
            {
                'codigo': 'HASTE-58',
                'descricao': 'Haste aço cobreada 5/8"x2,40m',
                'fabricante': 'Plasson',
                'quantidade': 6,
                'unidade': 'un',
                'preco_unit': precos_base['haste_5_8'],
                'total': 6 * precos_base['haste_5_8'],
                'aplicacao': 'Aterramento'
            },
        ]
        
        # Calcular totais
        total_materiais = sum(m['total'] for m in materiais)
        
        # Gerar CSV
        csv_path = self.output_dir / f"lista_materiais_{timestamp}.csv"
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['Código', 'Descrição', 'Fabricante', 'Quantidade', 'Unidade', 'Preço Unit.', 'Total', 'Aplicação'])
            for m in materiais:
                writer.writerow([
                    m['codigo'],
                    m['descricao'],
                    m['fabricante'],
                    m['quantidade'],
                    m['unidade'],
                    f"R$ {m['preco_unit']:.2f}",
                    f"R$ {m['total']:.2f}",
                    m['aplicacao']
                ])
            writer.writerow([])
            writer.writerow(['TOTAL GERAL', '', '', '', '', '', f"R$ {total_materiais:.2f}"])
        
        # Gerar JSON
        json_path = self.output_dir / f"lista_materiais_{timestamp}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'data': datetime.datetime.now().isoformat(),
                'materiais': materiais,
                'total': total_materiais,
                'observacoes': 'Preços estimados - sujeitos a alteração'
            }, f, indent=2)
        
        return {
            'sucesso': True,
            'csv': str(csv_path),
            'json': str(json_path),
            'total': total_materiais
        }


if __name__ == "__main__":
    gerador = GeradorListaExpandida()
    resultado = gerador.gerar_lista({})
    print(f"✅ CSV: {resultado['csv']}")
    print(f"💰 Total estimado: R$ {resultado['total']:.2f}")
