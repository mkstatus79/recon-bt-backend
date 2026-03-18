import os
import datetime
from typing import Dict, Any
import json

class GeradorFormularios:
    """
    GERADOR DE FORMULÁRIOS OFICIAIS LIGHT
    Código 100% pronto - será testado no PC com as bibliotecas apropriadas
    """
    
    def __init__(self, templates_dir="app/services/documentos/templates"):
        self.templates_dir = templates_dir
        self.output_dir = "app/services/documentos/output"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def gerar_solicitacao_ligacao(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera formulário de Solicitação de Ligação Nova
        Baseado no modelo oficial da Light
        """
        campos = {
            'consumidor': {
                'nome': dados.get('cliente_nome', ''),
                'cpf_cnpj': dados.get('cliente_cpf_cnpj', ''),
                'telefone': dados.get('cliente_telefone', ''),
                'email': dados.get('cliente_email', '')
            },
            'endereco': {
                'logradouro': dados.get('endereco_logradouro', ''),
                'numero': dados.get('endereco_numero', ''),
                'complemento': dados.get('endereco_complemento', ''),
                'bairro': dados.get('endereco_bairro', ''),
                'cidade': dados.get('endereco_cidade', 'Rio de Janeiro'),
                'cep': dados.get('endereco_cep', '')
            },
            'tecnico': {
                'nome': dados.get('responsavel_nome', ''),
                'crea': dados.get('responsavel_crea', ''),
                'art': dados.get('responsavel_art', '')
            },
            'instalacao': {
                'tipo_entrada': dados.get('tipo_entrada', 'INDIVIDUAL'),
                'num_ucs': dados.get('num_ucs', 1),
                'demanda_total_kva': dados.get('demanda_total', 0),
                'demanda_ramal_kva': dados.get('demanda_ramal', 0),
                'tensao': dados.get('tensao', '220/127V'),
                'fases': dados.get('fases', 3)
            },
            'materiais': {
                'disjuntor': dados.get('disjuntor', ''),
                'condutor': dados.get('condutor', ''),
                'caixa_medicao': dados.get('caixa_medicao', ''),
                'caixa_protecao': dados.get('caixa_protecao', '')
            },
            'documentos_anexos': {
                'projeto_aprovado': dados.get('projeto_aprovado', False),
                'art_execucao': dados.get('art_execucao', ''),
                'procuracoes': dados.get('procuracoes', [])
            },
            'controle': {
                'data_geracao': datetime.datetime.now().isoformat(),
                'versao_formulario': '2026.1',
                'protocolo': f"LGT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            }
        }
        
        # Salvar dados em JSON (universal)
        caminho_json = os.path.join(
            self.output_dir, 
            f"solicitacao_ligacao_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(campos, f, ensure_ascii=False, indent=2)
        
        return {
            'sucesso': True,
            'arquivo_json': caminho_json,
            'mensagem': 'Dados do formulário gerados. Para gerar PDF, execute no PC.',
            'dados': campos
        }
    
    def gerar_art_minuta(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera minuta de ART (Anotação de Responsabilidade Técnica)
        """
        art = {
            'profissional': {
                'nome': dados.get('responsavel_nome', ''),
                'registro': dados.get('responsavel_crea', ''),
                'conselho': 'CREA-RJ'
            },
            'contratante': {
                'nome': dados.get('cliente_nome', ''),
                'cpf_cnpj': dados.get('cliente_cpf_cnpj', '')
            },
            'empreendimento': {
                'nome': dados.get('empreendimento_nome', ''),
                'endereco': dados.get('endereco_completo', '')
            },
            'atividade': {
                'tipo': 'PROJETO DE ENTRADA DE ENERGIA ELÉTRICA',
                'norma': 'RECON-BT 2026',
                'descricao': f"Projeto de entrada coletiva com {dados.get('num_ucs', 1)} unidades"
            },
            'dados_tecnicos': {
                'demanda_kva': dados.get('demanda_total', 0),
                'area_m2': dados.get('area_total', 0),
                'nivel_tensao': dados.get('tensao', '220/127V')
            },
            'controle': {
                'data_emissao': datetime.datetime.now().strftime('%d/%m/%Y'),
                'hash_validacao': f"ART-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            }
        }
        
        caminho_json = os.path.join(
            self.output_dir,
            f"art_minuta_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(art, f, ensure_ascii=False, indent=2)
        
        return {
            'sucesso': True,
            'arquivo_json': caminho_json,
            'mensagem': 'Minuta de ART gerada. Para finalizar, acesse o site do CREA.',
            'dados': art
        }
    
    def gerar_lista_materiais(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera lista de materiais para compra/orçamento
        """
        materiais = []
        
        # Adicionar materiais baseados no dimensionamento
        if 'materiais' in dados:
            for item in dados['materiais']:
                materiais.append({
                    'codigo': item.get('codigo', ''),
                    'descricao': item.get('descricao', ''),
                    'quantidade': item.get('quantidade', 1),
                    'unidade': item.get('unidade', 'un'),
                    'observacao': item.get('observacao', '')
                })
        
        # Materiais padrão
        materiais_padrao = [
            {'codigo': 'DISJ-001', 'descricao': f"Disjuntor {dados.get('disjuntor', '100')}A tripolar", 'quantidade': 1},
            {'codigo': 'CABO-001', 'descricao': f"Cabo {dados.get('condutor', '4x95')} mm²", 'quantidade': 50, 'unidade': 'm'},
            {'codigo': 'CX-001', 'descricao': dados.get('caixa_medicao', 'CSM600'), 'quantidade': 1},
            {'codigo': 'HASTE-001', 'descricao': 'Haste aço cobreada 5/8"x2,40m', 'quantidade': dados.get('num_hastes', 6)},
        ]
        
        if not materiais:
            materiais = materiais_padrao
        
        resultado = {
            'projeto': dados.get('empreendimento_nome', ''),
            'data': datetime.datetime.now().strftime('%d/%m/%Y'),
            'materiais': materiais,
            'observacoes': 'Lista gerada automaticamente pelo sistema RECON-BT 2026'
        }
        
        caminho_json = os.path.join(
            self.output_dir,
            f"lista_materiais_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)
        
        return {
            'sucesso': True,
            'arquivo_json': caminho_json,
            'dados': resultado
        }


def exemplo_formularios():
    """Exemplo de uso dos geradores"""
    gerador = GeradorFormularios()
    
    # Dados de exemplo (baseados nos testes que rodamos)
    dados = {
        'cliente_nome': 'João da Silva',
        'cliente_cpf_cnpj': '123.456.789-00',
        'cliente_telefone': '(21) 99999-9999',
        'cliente_email': 'joao@email.com',
        'endereco_logradouro': 'Rua das Flores',
        'endereco_numero': '123',
        'endereco_complemento': 'Apto 101',
        'endereco_bairro': 'Centro',
        'endereco_cidade': 'Rio de Janeiro',
        'endereco_cep': '20000-000',
        'responsavel_nome': 'Eng. Marcos',
        'responsavel_crea': '2026123456',
        'responsavel_art': '202600123456',
        'tipo_entrada': 'COLETIVA',
        'num_ucs': 24,
        'demanda_total': 75.88,
        'demanda_ramal': 82.97,
        'tensao': '220/127V',
        'fases': 3,
        'disjuntor': '175A',
        'condutor': '4x95',
        'caixa_medicao': 'CSM600',
        'caixa_protecao': 'CPG200',
        'num_hastes': 6,
        'empreendimento_nome': 'Edifício Solar',
        'area_total': 1680,
        'projeto_aprovado': True,
        'art_execucao': '202600654321',
        'procuracoes': ['Procuração anexa'],
        'materiais': [
            {'codigo': 'DISJ-175', 'descricao': 'Disjuntor 175A tripolar', 'quantidade': 1},
            {'codigo': 'CABO-95', 'descricao': 'Cabo 95mm²', 'quantidade': 120, 'unidade': 'm'},
            {'codigo': 'CX-CSM600', 'descricao': 'Caixa CSM600', 'quantidade': 1},
        ]
    }
    
    print("=" * 60)
    print("GERAÇÃO DE FORMULÁRIOS - RECON-BT 2026")
    print("=" * 60)
    
    # Gerar solicitação de ligação
    print("\n📋 Gerando Solicitação de Ligação...")
    resultado1 = gerador.gerar_solicitacao_ligacao(dados)
    print(f"   JSON salvo em: {resultado1['arquivo_json']}")
    
    # Gerar minuta de ART
    print("\n📋 Gerando minuta de ART...")
    resultado2 = gerador.gerar_art_minuta(dados)
    print(f"   JSON salvo em: {resultado2['arquivo_json']}")
    
    # Gerar lista de materiais
    print("\n📋 Gerando lista de materiais...")
    resultado3 = gerador.gerar_lista_materiais(dados)
    print(f"   JSON salvo em: {resultado3['arquivo_json']}")
    
    print("\n" + "=" * 60)
    print("✅ FORMULÁRIOS GERADOS COM SUCESSO!")
    print("📌 Os dados estão salvos em formato JSON.")
    print("📌 Para gerar PDFs, execute no computador com as bibliotecas apropriadas.")
    
    return resultado1, resultado2, resultado3


if __name__ == "__main__":
    exemplo_formularios()
