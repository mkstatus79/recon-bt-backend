# ============================================
# GERADOR DE CHECKLIST DE EXECUÇÃO
# Para acompanhamento da obra
# USO INTERNO - NÃO ENVIAR PARA LIGHT
# ============================================

import json
import datetime
from pathlib import Path

class GeradorChecklist:
    """
    Gera checklist para acompanhamento da execução da obra
    """
    
    ITENS_PADRAO = [
        {
            'etapa': 'PREPARAÇÃO',
            'itens': [
                {'descricao': 'Projeto aprovado pela Light', 'obrigatorio': True},
                {'descricao': 'ART de execução registrada', 'obrigatorio': True},
                {'descricao': 'Materiais adquiridos (fabricantes homologados)', 'obrigatorio': True},
                {'descricao': 'Ferramentas disponíveis', 'obrigatorio': False},
            ]
        },
        {
            'etapa': 'INFRAESTRUTURA',
            'itens': [
                {'descricao': 'Eletrodutos instalados (profundidade mínima 70cm)', 'obrigatorio': True},
                {'descricao': 'Caixas de passagem posicionadas', 'obrigatorio': True},
                {'descricao': 'Valas reaterradas e compactadas', 'obrigatorio': False},
                {'descricao': 'Identificação dos dutos', 'obrigatorio': True},
            ]
        },
        {
            'etapa': 'MONTAGEM',
            'itens': [
                {'descricao': 'Caixa de medição fixada (altura 1,50m ±10%)', 'obrigatorio': True},
                {'descricao': 'Painel de medidores instalado', 'obrigatorio': True},
                {'descricao': 'Disjuntor geral instalado', 'obrigatorio': True},
                {'descricao': 'Barramentos apertados (torque adequado)', 'obrigatorio': True},
                {'descricao': 'Identificação das fases (cores padronizadas)', 'obrigatorio': True},
            ]
        },
        {
            'etapa': 'ATERRAMENTO',
            'itens': [
                {'descricao': f'Hastes instaladas (quantidade: {0})', 'obrigatorio': True},
                {'descricao': 'Interligação das hastes (cobre nu ≥50mm²)', 'obrigatorio': True},
                {'descricao': 'Caixa de inspeção instalada', 'obrigatorio': True},
                {'descricao': 'Medição de resistência ≤25Ω', 'obrigatorio': True},
            ]
        },
        {
            'etapa': 'VERIFICAÇÕES FINAIS',
            'itens': [
                {'descricao': 'Espaço operativo ≥0,70m com portas abertas', 'obrigatorio': True},
                {'descricao': 'Local limpo e organizado', 'obrigatorio': False},
                {'descricao': 'Identificação das unidades consumidoras', 'obrigatorio': True},
                {'descricao': 'Fotos tiradas para documentação', 'obrigatorio': True},
                {'descricao': 'Prontuário NR-10 disponível', 'obrigatorio': True},
            ]
        },
    ]
    
    def __init__(self):
        self.output_dir = Path(__file__).parent.parent / "output" / "interno"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_checklist(self, dados_projeto):
        """
        Gera checklist personalizado para o projeto
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_arquivo = f"checklist_obra_{timestamp}.html"
        caminho = self.output_dir / nome_arquivo
        
        # Personalizar quantidade de hastes
        num_hastes = dados_projeto.get('num_hastes', 6)
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Checklist de Execução - RECON-BT</title>
            <style>
                body {{ font-family: Arial; margin: 40px; }}
                h1 {{ color: #003366; }}
                .etapa {{ margin: 30px 0; }}
                .etapa h2 {{ background: #003366; color: white; padding: 10px; }}
                table {{ width: 100%; border-collapse: collapse; }}
                th {{ background: #f0f0f0; }}
                td, th {{ border: 1px solid #ccc; padding: 8px; }}
                .check {{ text-align: center; width: 50px; }}
                .obrigatorio {{ color: #D32F2F; font-weight: bold; }}
                .footer {{ margin-top: 50px; font-size: 0.9em; color: #666; }}
            </style>
        </head>
        <body>
            <h1>CHECKLIST DE EXECUÇÃO - RECON-BT 2026</h1>
            <p><strong>Projeto:</strong> {dados_projeto.get('nome', 'N/A')}</p>
            <p><strong>Data de geração:</strong> {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            <p><strong>Responsável:</strong> ______________________________</p>
            
            <table>
                <tr>
                    <th>Status</th>
                    <th>Item</th>
                    <th>Obrigatório</th>
                    <th>Observações</th>
                </tr>
        """
        
        for etapa in self.ITENS_PADRAO:
            # Atualizar quantidade de hastes
            if etapa['etapa'] == 'ATERRAMENTO':
                etapa['itens'][0]['descricao'] = f"Hastes instaladas (quantidade: {num_hastes})"
            
            for item in etapa['itens']:
                obrig = "✅ SIM" if item['obrigatorio'] else "❌ NÃO"
                html += f"""
                <tr>
                    <td class="check">[ ]</td>
                    <td>{item['descricao']}</td>
                    <td>{obrig}</td>
                    <td>_________________</td>
                </tr>
                """
        
        html += """
            </table>
            
            <div class="footer">
                <p>Instruções:</p>
                <ul>
                    <li>Marque [X] quando o item estiver concluído</li>
                    <li>Itens obrigatórios devem ser verificados antes de solicitar vistoria</li>
                    <li>Tire fotos dos itens marcados como obrigatórios</li>
                </ul>
                <p>⚠️ DOCUMENTO DE USO INTERNO - NÃO ENVIAR PARA LIGHT</p>
            </div>
        </body>
        </html>
        """
        
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return {
            'sucesso': True,
            'arquivo': str(caminho),
            'itens': sum(len(e['itens']) for e in self.ITENS_PADRAO)
        }


if __name__ == "__main__":
    gerador = GeradorChecklist()
    dados = {'nome': 'Edifício Solar', 'num_hastes': 6}
    resultado = gerador.gerar_checklist(dados)
    print(f"✅ Checklist gerado: {resultado['arquivo']}")
    print(f"📋 Total de itens: {resultado['itens']}")
