# ============================================
# GERADOR DE TERMO DE RESPONSABILIDADE PARA GERADOR - ANEXO VII
# Documento oficial para geração particular de emergência
# ============================================

import os
import datetime
import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class GeradorTermoGerador:
    """
    Gera o Termo de Responsabilidade para Gerador conforme Anexo VII
    """
    
    CONSELHOS = ['CREA', 'CAU', 'CFT']
    
    def __init__(self):
        self.template_dir = Path(__file__).parent.parent / "templates_light"
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        self.output_dir = Path(__file__).parent.parent / "output" / "light"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def gerar_html(self, dados):
        """Gera HTML do termo de gerador"""
        template = self.env.get_template('termo_gerador.html')
        
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
            'protocolo': f"GER-{hoje.strftime('%Y%m%d%H%M%S')}",
            
            # Dados da empresa/responsável técnico
            'empresa': dados.get('empresa', ''),
            'cnpj': dados.get('cnpj', ''),
            'profissional': dados.get('profissional', ''),
            'conselho': dados.get('conselho', 'CREA'),
            'registro': dados.get('registro', ''),
            
            # Dados do consumidor
            'consumidor': dados.get('consumidor', ''),
            'endereco': dados.get('endereco', ''),
            'municipio': dados.get('municipio', ''),
            'responsavel_imovel': dados.get('responsavel_imovel', ''),
            'cpf_responsavel': dados.get('cpf_responsavel', ''),
            
            # Especificações do gerador
            'fabricante': dados.get('fabricante', ''),
            'modelo': dados.get('modelo', ''),
            'potencia': dados.get('potencia', ''),
            'tensao': dados.get('tensao', '220/127V'),
            'chave': dados.get('chave', 'Manual/Elétrica com intertravamento'),
            'intertravamento': dados.get('intertravamento', 'Mecânico'),
        }
        
        return template.render(dados_completos)
    
    def validar_gerador(self, dados):
        """
        Valida as condições do gerador conforme RECON-BT
        Fascículo 04, item 3.1
        """
        inconsistencias = []
        
        # Verificar tipo de chave
        if 'paralelismo' in dados.get('chave', '').lower():
            inconsistencias.append({
                'tipo': 'ERRO',
                'mensagem': 'Gerador de emergência não pode operar em paralelo com a rede'
            })
        
        # Verificar intertravamento
        if not dados.get('intertravamento'):
            inconsistencias.append({
                'tipo': 'ERRO',
                'mensagem': 'É obrigatório dispositivo de intertravamento mecânico'
            })
        
        # Verificar conselho profissional
        if dados.get('conselho') not in self.CONSELHOS:
            inconsistencias.append({
                'tipo': 'ALERTA',
                'mensagem': f'Conselho {dados.get("conselho")} não reconhecido. Esperado: CREA, CAU ou CFT'
            })
        
        return {
            'valido': len([i for i in inconsistencias if i['tipo'] == 'ERRO']) == 0,
            'inconsistencias': inconsistencias
        }
    
    def gerar_para_light(self, dados):
        """Gera termo oficial para anexar ao processo"""
        
        # Validações
        validacao = self.validar_gerador(dados)
        
        if not validacao['valido']:
            return {
                'sucesso': False,
                'erro': 'Gerador não atende requisitos de segurança',
                'detalhes': validacao['inconsistencias']
            }
        
        # Gera documento
        html = self.gerar_html(dados)
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        arquivo = self.output_dir / f"termo_gerador_{timestamp}.html"
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return {
            'sucesso': True,
            'documento': str(arquivo),
            'protocolo': f"GER-{timestamp}",
            'validacao': validacao,
            'mensagem': 'Termo de gerador gerado com sucesso'
        }


# Exemplo de uso
if __name__ == "__main__":
    gerador = GeradorTermoGerador()
    
    dados = {
        'empresa': 'Engenharia Silva Ltda',
        'cnpj': '12.345.678/0001-90',
        'profissional': 'Eng. Marcos Silva',
        'conselho': 'CREA',
        'registro': '2026123456',
        'consumidor': 'João da Silva',
        'endereco': 'Rua das Flores, 123 - Centro',
        'municipio': 'Rio de Janeiro',
        'responsavel_imovel': 'João da Silva',
        'cpf_responsavel': '123.456.789-00',
        'fabricante': 'Stamford',
        'modelo': 'S10-4P',
        'potencia': '100',
        'tensao': '220/127V',
        'chave': 'Manual com intertravamento mecânico',
        'intertravamento': 'Mecânico'
    }
    
    resultado = gerador.gerar_para_light(dados)
    if resultado['sucesso']:
        print(f"✅ Termo de gerador gerado: {resultado['documento']}")
    else:
        print(f"❌ Erro: {resultado['erro']}")
        for item in resultado.get('detalhes', []):
            print(f"   • {item['mensagem']}")
