# ============================================
# GERADOR DE SOLICITAÇÃO DE LIGAÇÃO - LIGHT
# Documento OFICIAL para envio à concessionária
# ============================================

import os
import datetime
import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class GeradorSolicitacaoLight:
    """
    Gera o formulário oficial de Solicitação de Ligação Nova
    IDÊNTICO ao PDF da Light - para envio à concessionária
    """
    
    def __init__(self):
        self.template_dir = Path(__file__).parent.parent / "templates_light"
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        self.output_dir = Path(__file__).parent.parent / "output" / "light"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_html(self, dados):
        """Gera HTML idêntico ao formulário Light"""
        template = self.env.get_template('solicitacao_ligacao.html')
        
        # Dados padrão com protocolo único
        dados_completos = {
            'protocolo': f"LGT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            'data': datetime.datetime.now().strftime('%d/%m/%Y'),
            'cliente_nome': dados.get('cliente_nome', ''),
            'cliente_cpf_cnpj': dados.get('cliente_cpf_cnpj', ''),
            'cliente_telefone': dados.get('cliente_telefone', ''),
            'cliente_email': dados.get('cliente_email', ''),
            'endereco_logradouro': dados.get('endereco_logradouro', ''),
            'endereco_numero': dados.get('endereco_numero', ''),
            'endereco_complemento': dados.get('endereco_complemento', ''),
            'endereco_cep': dados.get('endereco_cep', ''),
            'endereco_bairro': dados.get('endereco_bairro', ''),
            'endereco_cidade': dados.get('endereco_cidade', 'Rio de Janeiro'),
            'tipo_entrada': dados.get('tipo_entrada', 'INDIVIDUAL'),
            'num_ucs': dados.get('num_ucs', 1),
            'demanda_total': dados.get('demanda_total', 0),
            'responsavel_nome': dados.get('responsavel_nome', ''),
            'responsavel_crea': dados.get('responsavel_crea', ''),
            'responsavel_art': dados.get('responsavel_art', ''),
        }
        
        return template.render(dados_completos)
    
    def salvar_rascunho(self, dados):
        """Salva rascunho do formulário (JSON)"""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        arquivo_json = self.output_dir / f"rascunho_solicitacao_{timestamp}.json"
        
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        
        return str(arquivo_json)
    
    def gerar_para_light(self, dados, formato='html'):
        """
        Gera documento APENAS para envio à Light
        Este é o documento oficial que será protocolado
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Gera HTML
        html = self.gerar_html(dados)
        
        # Salva HTML
        arquivo_html = self.output_dir / f"solicitacao_light_{timestamp}.html"
        with open(arquivo_html, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Salva rascunho dos dados
        self.salvar_rascunho(dados)
        
        return {
            'sucesso': True,
            'documento_oficial': str(arquivo_html),
            'protocolo': f"LGT-{timestamp}",
            'mensagem': 'Formulário oficial Light gerado. Pronto para envio à concessionária.',
            'dados': dados
        }
    
    def validar_campos_obrigatorios(self, dados):
        """Valida se todos os campos obrigatórios estão preenchidos"""
        obrigatorios = [
            'cliente_nome', 'cliente_cpf_cnpj', 'endereco_logradouro',
            'endereco_numero', 'endereco_bairro', 'tipo_entrada',
            'responsavel_nome', 'responsavel_crea'
        ]
        
        faltantes = []
        for campo in obrigatorios:
            if not dados.get(campo):
                faltantes.append(campo)
        
        return {
            'valido': len(faltantes) == 0,
            'campos_faltantes': faltantes
        }


# Exemplo de uso
if __name__ == "__main__":
    gerador = GeradorSolicitacaoLight()
    
    # Dados de exemplo
    dados = {
        'cliente_nome': 'João da Silva',
        'cliente_cpf_cnpj': '123.456.789-00',
        'cliente_telefone': '(21) 99999-9999',
        'cliente_email': 'joao@email.com',
        'endereco_logradouro': 'Rua das Flores',
        'endereco_numero': '123',
        'endereco_complemento': 'Apto 101',
        'endereco_cep': '20000-000',
        'endereco_bairro': 'Centro',
        'endereco_cidade': 'Rio de Janeiro',
        'tipo_entrada': 'INDIVIDUAL',
        'num_ucs': 1,
        'demanda_total': 62.29,
        'responsavel_nome': 'Eng. Marcos',
        'responsavel_crea': '2026123456',
        'responsavel_art': '202600123456',
    }
    
    resultado = gerador.gerar_para_light(dados)
    print(f"✅ Documento gerado: {resultado['documento_oficial']}")
    print(f"📋 Protocolo: {resultado['protocolo']}")
