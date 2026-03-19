# ============================================
# GERADOR DE PSD (Pedido de Serviços Diversos) - LIGHT
# Documento OFICIAL para alterações de carga
# ============================================

import os
import datetime
import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class GeradorPSD:
    """
    Gera o formulário oficial de Pedido de Serviços Diversos
    """
    
    TIPOS_SERVICO = [
        'AUMENTO_CARGA',
        'DIMINUICAO_CARGA', 
        'RELOCACAO_MEDIDOR',
        'SUBSTITUICAO',
        'PADRONIZACAO',
        'VIATEC'
    ]
    
    def __init__(self):
        self.template_dir = Path(__file__).parent.parent / "templates_light"
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        self.output_dir = Path(__file__).parent.parent / "output" / "light"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_html(self, dados):
        """Gera HTML idêntico ao formulário PSD Light"""
        template = self.env.get_template('psd.html')
        
        # Dados padrão
        dados_completos = {
            'protocolo': f"PSD-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            'data': datetime.datetime.now().strftime('%d/%m/%Y'),
            
            # Identificação
            'uc': dados.get('uc', ''),
            'cliente_nome': dados.get('cliente_nome', ''),
            'cliente_cpf_cnpj': dados.get('cliente_cpf_cnpj', ''),
            'cliente_telefone': dados.get('cliente_telefone', ''),
            'cliente_email': dados.get('cliente_email', ''),
            
            # Endereço
            'endereco_logradouro': dados.get('endereco_logradouro', ''),
            'endereco_numero': dados.get('endereco_numero', ''),
            'endereco_complemento': dados.get('endereco_complemento', ''),
            'endereco_cep': dados.get('endereco_cep', ''),
            'endereco_bairro': dados.get('endereco_bairro', ''),
            'endereco_cidade': dados.get('endereco_cidade', 'Rio de Janeiro'),
            
            # Serviço
            'servico': dados.get('servico', 'AUMENTO_CARGA'),
            'outros_servicos': dados.get('outros_servicos', ''),
            
            # Alteração
            'carga_atual': dados.get('carga_atual', 0),
            'carga_pretendida': dados.get('carga_pretendida', 0),
            'fases_atual': dados.get('fases_atual', 3),
            'fases_pretendido': dados.get('fases_pretendido', 3),
            'tensao_atual': dados.get('tensao_atual', '220/127V'),
            'tensao_pretendido': dados.get('tensao_pretendido', '220/127V'),
            
            # Medidores
            'medidor_1': dados.get('medidor_1', ''),
            'medidor_2': dados.get('medidor_2', ''),
            'medidor_3': dados.get('medidor_3', ''),
            'medidor_4': dados.get('medidor_4', ''),
            
            # Documentos anexos
            'art_anexada': dados.get('art_anexada', False),
            'projeto_anexado': dados.get('projeto_anexado', False),
            'procuracao_anexada': dados.get('procuracao_anexada', False),
            'fotos_anexadas': dados.get('fotos_anexadas', False),
        }
        
        return template.render(dados_completos)
    
    def gerar_para_light(self, dados):
        """Gera documento oficial para Light"""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Validações automáticas
        from app.core.validacao.regras import ValidadorLimiteCarga
        
        # Verifica limite de carga
        if dados.get('servico') == 'AUMENTO_CARGA':
            limite = ValidadorLimiteCarga.validar(
                dados.get('tipo_ligacao', 'INDIVIDUAL'),
                dados.get('carga_pretendida', 0)
            )
            if not limite['valido']:
                return {
                    'sucesso': False,
                    'erro': 'Limite de carga excedido',
                    'detalhes': limite['mensagem']
                }
        
        # Gera HTML
        html = self.gerar_html(dados)
        
        # Salva
        arquivo_html = self.output_dir / f"psd_{timestamp}.html"
        with open(arquivo_html, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return {
            'sucesso': True,
            'documento': str(arquivo_html),
            'protocolo': f"PSD-{timestamp}",
            'mensagem': 'PSD gerado com sucesso'
        }

# Exemplo de uso
if __name__ == "__main__":
    gerador = GeradorPSD()
    
    dados = {
        'uc': '123456789',
        'cliente_nome': 'João da Silva',
        'cliente_cpf_cnpj': '123.456.789-00',
        'servico': 'AUMENTO_CARGA',
        'carga_atual': 30,
        'carga_pretendida': 50,
        'tipo_ligacao': 'INDIVIDUAL'
    }
    
    resultado = gerador.gerar_para_light(dados)
    print(f"✅ PSD gerado: {resultado['documento']}")
