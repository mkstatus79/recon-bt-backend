from jinja2 import Template, Environment, FileSystemLoader
import os
import datetime
import pdfkit

class GeradorMemorial:
    def __init__(self, template_dir="app/services/documentos/templates"):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))
    
    def gerar_html(self, dados):
        """Gera HTML do memorial a partir dos dados"""
        template = self.env.get_template('memorial_descritivo.html')
        
        # Dados padrão
        dados_padrao = {
            'data': datetime.datetime.now().strftime('%d/%m/%Y'),
            'data_hora': datetime.datetime.now().strftime('%d/%m/%Y %H:%M'),
            'unidades': [],
            'servico_cargas': [],
            'tipo_entrada': 'Individual' if dados.get('num_ucs', 1) == 1 else 'Coletiva',
            'tensao': '220/127V',
            'disjuntor_polos': 3,
            'tipo_medicao': 'Direta' if dados.get('demanda_ramal', 0) <= 76 else 'Indireta',
        }
        
        # Mesclar dados fornecidos com padrão
        dados_completos = {**dados_padrao, **dados}
        
        return template.render(dados_completos)
    
    def gerar_pdf(self, html, output_path):
        """Gera PDF a partir do HTML"""
        # Opções do pdfkit
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
        }
        
        pdfkit.from_string(html, output_path, options=options)
        return output_path
    
    def gerar_memorial(self, dados_projeto, output_dir="app/services/documentos/output"):
        """Gera memorial completo em PDF"""
        # Garantir que o diretório de saída existe
        os.makedirs(output_dir, exist_ok=True)
        
        # Nome do arquivo
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_arquivo = f"memorial_{timestamp}.pdf"
        caminho_completo = os.path.join(output_dir, nome_arquivo)
        
        # Gerar HTML
        html = self.gerar_html(dados_projeto)
        
        # Salvar HTML temporário para debug (opcional)
        html_temp = os.path.join(output_dir, f"temp_{timestamp}.html")
        with open(html_temp, 'w') as f:
            f.write(html)
        
        # Gerar PDF
        try:
            self.gerar_pdf(html, caminho_completo)
            return {
                'sucesso': True,
                'arquivo_pdf': caminho_completo,
                'arquivo_html': html_temp,
                'mensagem': 'Memorial gerado com sucesso'
            }
        except Exception as e:
            return {
                'sucesso': False,
                'erro': str(e),
                'arquivo_html': html_temp,
                'mensagem': 'Erro ao gerar PDF. HTML salvo para verificação.'
            }


def exemplo_geracao():
    """Exemplo de uso do gerador"""
    gerador = GeradorMemorial()
    
    # Dados de exemplo (baseados nos testes que rodamos)
    dados = {
        'empreendimento': 'Edifício Solar',
        'endereco': 'Rua das Flores, 123 - Centro - Rio de Janeiro/RJ',
        'responsavel': 'Eng. Marcos',
        'crea': '2026123456',
        'cliente': 'Construtora Modelo Ltda',
        'art': '202600123456',
        'num_ucs': 24,
        'area_total': 1680,
        'unidades': [
            {'identificacao': 'Apt 101-124', 'area': 70, 'demanda': 2.54, 'obs': '12 aptos tipo A'},
            {'identificacao': 'Apt 201-224', 'area': 70, 'demanda': 2.54, 'obs': '12 aptos tipo B'},
        ],
        'servico_cargas': [
            {'tipo': 'Iluminação', 'potencia': 6.5, 'fd': 80, 'demanda': 5.2},
            {'tipo': 'Motores', 'potencia': 21.34, 'fd': 63.33, 'demanda': 13.51},
        ],
        'demanda_servico_total': 18.71,
        'demanda_protecao': 50.50,
        'demanda_ramal': 62.29,
        'condutor_fase': '95',
        'condutor_neutro': '95',
        'condutor_protecao': '50',
        'disjuntor': 175,
        'disjuntor_ka': 15,
        'caixa_protecao': 'CPG200',
        'caixa_medicao': 'CSM600',
        'painel_medidores': 'PDMD2-24',
        'eletroduto_aereo': '2x3"',
        'eletroduto_sub': '2x4"',
        'num_hastes': 6,
        'condutor_aterramento': '50',
    }
    
    resultado = gerador.gerar_memorial(dados)
    
    if resultado['sucesso']:
        print(f"✅ Memorial gerado: {resultado['arquivo_pdf']}")
    else:
        print(f"❌ Erro: {resultado['erro']}")
        print(f"HTML salvo em: {resultado['arquivo_html']}")
    
    return resultado


if __name__ == "__main__":
    exemplo_geracao()
