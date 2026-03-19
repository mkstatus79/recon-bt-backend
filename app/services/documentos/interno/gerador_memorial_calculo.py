# ============================================
# GERADOR DE MEMORIAL DE CÁLCULO - USO INTERNO
# Documento detalhado para o engenheiro/técnico
# NÃO ENVIAR PARA LIGHT
# ============================================

import os
import datetime
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class GeradorMemorialCalculo:
    """
    Gera memorial de cálculo detalhado com todas as memórias
    Inclui fórmulas, tabelas e passos intermediários
    """
    
    def __init__(self):
        self.template_dir = Path(__file__).parent.parent / "templates_interno"
        self.template_dir.mkdir(exist_ok=True)
        self.output_dir = Path(__file__).parent.parent / "output" / "interno"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Criar template simples se não existir
        self._criar_template()
    
    def _criar_template(self):
        """Cria template HTML para memorial de cálculo"""
        template_path = self.template_dir / "memorial_calculo.html"
        
        if not template_path.exists():
            template_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Memorial de Cálculo - RECON-BT 2026</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #003366; border-bottom: 2px solid #003366; }
        h2 { color: #003366; margin-top: 30px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th { background: #003366; color: white; padding: 10px; }
        td { border: 1px solid #ccc; padding: 8px; }
        .secao { background: #f5f5f5; padding: 15px; margin: 20px 0; }
        .formula { font-family: monospace; background: #eee; padding: 10px; }
        .obs { color: #666; font-size: 0.9em; margin-top: 5px; }
    </style>
</head>
<body>
    <h1>MEMORIAL DE CÁLCULO - RECON-BT 2026</h1>
    <p><strong>Projeto:</strong> {{projeto_nome}}</p>
    <p><strong>Data:</strong> {{data}}</p>
    <p><strong>Responsável:</strong> {{responsavel}}</p>

    <h2>1. DADOS DE ENTRADA</h2>
    <table>
        <tr><th>Parâmetro</th><th>Valor</th></tr>
        {% for item in dados_entrada %}
        <tr><td>{{item.parametro}}</td><td>{{item.valor}}</td></tr>
        {% endfor %}
    </table>

    <h2>2. CÁLCULO DA DEMANDA</h2>
    
    <div class="secao">
        <h3>2.1 Seção A (Unidades Individuais)</h3>
        {% for uc in unidades %}
        <h4>UC {{loop.index}}</h4>
        <table>
            <tr><th>Parcela</th><th>Carga (kVA)</th><th>FD (%)</th><th>Demanda (kVA)</th></tr>
            {% for parcela in uc.parcelas %}
            <tr>
                <td>{{parcela.descricao}}</td>
                <td>{{parcela.carga}}</td>
                <td>{{parcela.fd}}</td>
                <td>{{parcela.demanda}}</td>
            </tr>
            {% endfor %}
            <tr style="font-weight: bold;">
                <td colspan="3">TOTAL</td>
                <td>{{uc.total}}</td>
            </tr>
        </table>
        {% endfor %}
    </div>

    <div class="secao">
        <h3>2.2 Seção B (Conjunto)</h3>
        <table>
            <tr><th>Parâmetro</th><th>Valor</th><th>Fórmula</th></tr>
            {% for item in secao_b %}
            <tr>
                <td>{{item.parametro}}</td>
                <td>{{item.valor}}</td>
                <td class="formula">{{item.formula}}</td>
            </tr>
            {% endfor %}
        </table>
    </div>

    <h2>3. DIMENSIONAMENTO</h2>
    <table>
        <tr><th>Componente</th><th>Especificação</th><th>Base</th></tr>
        {% for item in dimensionamento %}
        <tr>
            <td>{{item.componente}}</td>
            <td>{{item.especificacao}}</td>
            <td>{{item.base}}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>4. OBSERVAÇÕES TÉCNICAS</h2>
    <ul>
        {% for obs in observacoes %}
        <li>{{obs}}</li>
        {% endfor %}
    </ul>

    <div class="obs">
        <p>Documento gerado automaticamente em {{data_hora}}</p>
        <p>⚠️ USO INTERNO - NÃO ENVIAR PARA LIGHT</p>
    </div>
</body>
</html>
"""
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(template_content)
    
    def gerar_memorial(self, dados_projeto):
        """Gera memorial de cálculo completo"""
        
        # Preparar dados
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_arquivo = f"memorial_calculo_{timestamp}.html"
        caminho = self.output_dir / nome_arquivo
        
        # Dados de entrada formatados
        dados_entrada = [
            {'parametro': 'Tipo de entrada', 'valor': dados_projeto.get('tipo_entrada', '')},
            {'parametro': 'Número de UCs', 'valor': dados_projeto.get('num_ucs', 0)},
            {'parametro': 'Área total (m²)', 'valor': dados_projeto.get('area_total', 0)},
            {'parametro': 'Tensão (V)', 'valor': dados_projeto.get('tensao', '220/127')},
        ]
        
        # Simular parcelas (em produção viria dos cálculos reais)
        parcelas = [
            {'descricao': 'Iluminação e tomadas', 'carga': 2.5, 'fd': 80, 'demanda': 2.0},
            {'descricao': 'Aquecimento', 'carga': 7.65, 'fd': 100, 'demanda': 7.65},
            {'descricao': 'Ar condicionado', 'carga': 1.17, 'fd': 100, 'demanda': 1.17},
        ]
        
        secao_b = [
            {'parametro': 'Área equivalente', 'valor': '76 m²', 'formula': 'Σ(n×S)/Σn'},
            {'parametro': 'Demanda por UC', 'valor': '2.54 kVA', 'formula': 'Tabela 6.11'},
            {'parametro': 'Fator diversificação', 'valor': '19.88', 'formula': 'Tabela 6.13'},
        ]
        
        dimensionamento = [
            {'componente': 'Disjuntor geral', 'especificacao': '175A tripolar', 'base': 'Tabela 7.3'},
            {'componente': 'Condutor fase', 'especificacao': '95 mm²', 'base': 'Tabela 8.4'},
            {'componente': 'Condutor neutro', 'especificacao': '95 mm²', 'base': 'NBR 5410'},
            {'componente': 'Condutor proteção', 'especificacao': '50 mm²', 'base': 'Tabela 10.2'},
        ]
        
        # Gerar HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"><title>Memorial de Cálculo</title></head>
        <body>
            <h1>MEMORIAL DE CÁLCULO - RECON-BT 2026</h1>
            <p><strong>Projeto:</strong> {dados_projeto.get('nome', 'N/A')}</p>
            <p><strong>Data:</strong> {datetime.datetime.now().strftime('%d/%m/%Y')}</p>
            
            <h2>1. DADOS DE ENTRADA</h2>
            <table border="1">
                <tr><th>Parâmetro</th><th>Valor</th></tr>
                {"".join(f'<tr><td>{p["parametro"]}</td><td>{p["valor"]}</td></tr>' for p in dados_entrada)}
            </table>
            
            <h2>2. CÁLCULO SEÇÃO A</h2>
            <table border="1">
                <tr><th>Descrição</th><th>Carga</th><th>FD%</th><th>Demanda</th></tr>
                {"".join(f'<tr><td>{p["descricao"]}</td><td>{p["carga"]}</td><td>{p["fd"]}</td><td>{p["demanda"]}</td></tr>' for p in parcelas)}
            </table>
            
            <h2>3. DIMENSIONAMENTO</h2>
            <table border="1">
                <tr><th>Componente</th><th>Especificação</th></tr>
                {"".join(f'<tr><td>{d["componente"]}</td><td>{d["especificacao"]}</td></tr>' for d in dimensionamento)}
            </table>
            
            <p><em>Documento gerado automaticamente - USO INTERNO</em></p>
        </body>
        </html>
        """
        
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return {
            'sucesso': True,
            'arquivo': str(caminho),
            'tamanho': os.path.getsize(caminho)
        }


# Exemplo de uso
if __name__ == "__main__":
    gerador = GeradorMemorialCalculo()
    dados = {'nome': 'Edifício Solar', 'tipo_entrada': 'COLETIVA', 'num_ucs': 24}
    resultado = gerador.gerar_memorial(dados)
    print(f"✅ Memorial gerado: {resultado['arquivo']}")
