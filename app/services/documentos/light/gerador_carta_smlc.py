# ============================================
# GERADOR DE CARTA DE OPÇÃO SMLC - ANEXO VI
# Documento oficial para optar pelo sistema de medição centralizada
# ============================================

import os
import datetime
import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class GeradorCartaSMLC:
    """
    Gera a Carta de Opção SMLC conforme Anexo VI do RECON-BT 2026
    """
    
    def __init__(self):
        self.template_dir = Path(__file__).parent.parent / "templates_light"
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        self.output_dir = Path(__file__).parent.parent / "output" / "light"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_html(self, dados):
        """Gera HTML da carta SMLC"""
        template = self.env.get_template('carta_smlc.html')
        
        hoje = datetime.datetime.now()
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        
        dados_completos = {
            'dia': hoje.day,
            'mes': meses[hoje.month - 1],
            'ano': hoje.year,
            'data_geracao': hoje.strftime('%d/%m/%Y %H:%M'),
            'protocolo': f"SMLC-{hoje.strftime('%Y%m%d%H%M%S')}",
            
            'interessado': dados.get('interessado', ''),
            'empreendimento': dados.get('empreendimento', ''),
            'endereco': dados.get('endereco', ''),
            'responsavel_pagamento': dados.get('responsavel_pagamento', ''),
            'responsavel_tecnico': dados.get('responsavel_tecnico', ''),
            'crea': dados.get('crea', ''),
            'responsavel_imovel': dados.get('responsavel_imovel', ''),
            'cpf_cnpj': dados.get('cpf_cnpj', ''),
        }
        
        return template.render(dados_completos)
    
    def validar_condicoes_smlc(self, dados):
        """
        Valida se o projeto atende condições para SMLC
        Base: Fascículo 08, item 2.4
        """
        from app.core.validacao.regras import ValidadorProjetoSimplificado
        
        # Verifica distância da proteção geral (se aplicável)
        if dados.get('distancia_protecao', 0) > 5:
            return {
                'valido': True,
                'motivo': 'Distância superior a 5 metros da proteção geral - SMLC obrigatório'
            }
        
        # Verifica se medidores são nos andares
        if dados.get('local_medidores') == 'ANDARES':
            return {
                'valido': True,
                'motivo': 'Medidores distribuídos nos andares - SMLC obrigatório'
            }
        
        return {
            'valido': dados.get('opcao_smlc', False),
            'motivo': 'Opção voluntária pelo SMLC' if dados.get('opcao_smlc', False) else 'SMLC não aplicável'
        }
    
    def gerar_para_light(self, dados):
        """Gera carta oficial para anexar ao processo"""
        
        # Valida condições
        validacao = self.validar_condicoes_smlc(dados)
        
        if not validacao['valido'] and not dados.get('forcar_geracao', False):
            return {
                'sucesso': False,
                'erro': 'Projeto não atende condições para SMLC',
                'motivo': validacao['motivo']
            }
        
        # Gera documento
        html = self.gerar_html(dados)
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        arquivo = self.output_dir / f"carta_smlc_{timestamp}.html"
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return {
            'sucesso': True,
            'documento': str(arquivo),
            'protocolo': f"SMLC-{timestamp}",
            'validacao': validacao,
            'mensagem': 'Carta SMLC gerada com sucesso'
        }


# Exemplo de uso
if __name__ == "__main__":
    gerador = GeradorCartaSMLC()
    
    dados = {
        'interessado': 'Construtora Modelo Ltda',
        'empreendimento': 'Edifício Solar',
        'endereco': 'Rua das Flores, 123 - Centro - Rio de Janeiro/RJ',
        'responsavel_pagamento': 'Construtora Modelo Ltda - CNPJ 12.345.678/0001-90',
        'responsavel_tecnico': 'Eng. Marcos Silva',
        'crea': '2026123456',
        'responsavel_imovel': 'João da Silva',
        'cpf_cnpj': '123.456.789-00',
        'local_medidores': 'ANDARES',  # ANDARES, TERREO_AFASTADO, TERREO_JUNTO
        'distancia_protecao': 15,
        'opcao_smlc': True
    }
    
    resultado = gerador.gerar_para_light(dados)
    if resultado['sucesso']:
        print(f"✅ Carta SMLC gerada: {resultado['documento']}")
        print(f"📋 Motivo: {resultado['validacao']['motivo']}")
    else:
        print(f"❌ Erro: {resultado['erro']}")

