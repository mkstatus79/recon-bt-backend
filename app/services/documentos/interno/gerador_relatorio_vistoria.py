# ============================================
# GERADOR DE RELATÓRIO DE VISTORIA
# Baseado na REG-BUS-005 (monitoramento de prazos)
# USO INTERNO - CONTROLE DE RETRABALHO
# ============================================

import datetime
from pathlib import Path

class GeradorRelatorioVistoria:
    """
    Gera relatório de vistoria com controle de prazos e pendências
    """
    
    def __init__(self):
        self.output_dir = Path(__file__).parent.parent / "output" / "interno"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_relatorio(self, dados_vistoria):
        """
        dados_vistoria = {
            'data_vistoria': '2026-03-19',
            'status': 'REPROVADO',
            'pendencias': [...],
            'responsavel': 'Fulano',
            'protocolo': 'LGT-12345'
        }
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        arquivo = self.output_dir / f"relatorio_vistoria_{timestamp}.html"
        
        # Calcular prazos
        data_vistoria = datetime.datetime.strptime(dados_vistoria['data_vistoria'], '%Y-%m-%d')
        prazo_relatorio = data_vistoria + datetime.timedelta(days=3)  # dias úteis simplificado
        prazo_correcao = prazo_relatorio + datetime.timedelta(days=3)
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Relatório de Vistoria</title>
            <style>
                body {{ font-family: Arial; margin: 40px; }}
                h1 {{ color: #003366; }}
                .reprovado {{ background: #FFEBEE; padding: 20px; }}
                .pendencia {{ margin: 10px 0; padding: 10px; border-left: 4px solid #D32F2F; }}
                .prazo {{ background: #F5F5F5; padding: 15px; }}
            </style>
        </head>
        <body>
            <h1>RELATÓRIO DE VISTORIA - RECON-BT 2026</h1>
            <p><strong>Protocolo:</strong> {dados_vistoria['protocolo']}</p>
            <p><strong>Data da vistoria:</strong> {dados_vistoria['data_vistoria']}</p>
            <p><strong>Responsável Light:</strong> {dados_vistoria['responsavel']}</p>
            <p><strong>Status:</strong> <span style="color: #D32F2F;">{dados_vistoria['status']}</span></p>
            
            <div class="reprovado">
                <h2>PENDÊNCIAS ENCONTRADAS</h2>
                {''.join(f'<div class="pendencia">• {p}</div>' for p in dados_vistoria['pendencias'])}
            </div>
            
            <div class="prazo">
                <h2>PRAZOS (REG-BUS-005)</h2>
                <p><strong>Data limite para relatório:</strong> {prazo_relatorio.strftime('%d/%m/%Y')}</p>
                <p><strong>Data limite para correção:</strong> {prazo_correcao.strftime('%d/%m/%Y')}</p>
                <p><strong>Dias restantes para correção:</strong> {(prazo_correcao - datetime.datetime.now()).days}</p>
            </div>
            
            <h3>EVIDÊNCIAS FOTOGRÁFICAS</h3>
            <p>☐ Foto 1: _________________</p>
            <p>☐ Foto 2: _________________</p>
            <p>☐ Foto 3: _________________</p>
            
            <p><em>Gerado em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}</em></p>
            <p>⚠️ USO INTERNO</p>
        </body>
        </html>
        """
        
        with open(arquivo, 'w') as f:
            f.write(html)
        
        return {
            'sucesso': True,
            'arquivo': str(arquivo),
            'prazo_correcao': prazo_correcao.strftime('%d/%m/%Y')
        }


# Exemplo
if __name__ == "__main__":
    gerador = GeradorRelatorioVistoria()
    dados = {
        'data_vistoria': '2026-03-19',
        'status': 'REPROVADO',
        'pendencias': [
            'Altura do visor incorreta (1,80m)',
            'Aterramento com resistência >25Ω',
            'Identificação das unidades ausente'
        ],
        'responsavel': 'Carlos Técnico',
        'protocolo': 'LGT-20260319-001'
    }
    res = gerador.gerar_relatorio(dados)
    print(f"✅ Relatório: {res['arquivo']}")
    print(f"📅 Prazo correção: {res['prazo_correcao']}")
