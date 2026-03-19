# ============================================
# EMPACOTADOR DE DOCUMENTOS PARA LIGHT
# Garante que apenas documentos oficiais sejam enviados
# ============================================

import os
import zipfile
import datetime
from pathlib import Path
from typing import List, Dict

class EmpacotadorLight:
    """
    Empacota apenas os documentos OBRIGATÓRIOS para envio à Light
    """
    
    # Documentos obrigatórios por tipo de projeto
    DOCS_OBRIGATORIOS = {
        'INDIVIDUAL_SIMPLES': [
            'solicitacao_ligacao',
            'art_projeto',
        ],
        'INDIVIDUAL_MEDIA': [
            'solicitacao_ligacao',
            'projeto_entrada',
            'art_projeto',
            'art_execucao',
        ],
        'COLETIVA': [
            'solicitacao_ligacao',
            'projeto_entrada',
            'art_projeto',
            'art_execucao',
            'carta_smlc',  # se aplicável
            'termo_gerador',  # se aplicável
            'carta_cessao',  # se aplicável
        ],
        'MEDICAO_INDIRETA': [
            'solicitacao_ligacao',
            'projeto_entrada',
            'art_projeto',
            'art_execucao',
            'especificacao_tc',
        ],
    }
    
    def __init__(self, projeto_id, tipo_projeto='COLETIVA'):
        self.projeto_id = projeto_id
        self.tipo_projeto = tipo_projeto
        self.pasta_projeto = Path(f"pacotes/projeto_{projeto_id}")
        self.pasta_projeto.mkdir(parents=True, exist_ok=True)
    
    def adicionar_documento(self, caminho_arquivo, nome_destino=None):
        """
        Adiciona um documento à pasta do projeto
        """
        if not nome_destino:
            nome_destino = Path(caminho_arquivo).name
        
        destino = self.pasta_projeto / nome_destino
        import shutil
        shutil.copy2(caminho_arquivo, destino)
        return str(destino)
    
    def listar_documentos_obrigatorios(self):
        """
        Retorna lista de documentos obrigatórios para este tipo de projeto
        """
        return self.DOCS_OBRIGATORIOS.get(self.tipo_projeto, [])
    
    def verificar_documentos(self, documentos_disponiveis):
        """
        Verifica se todos os documentos obrigatórios estão presentes
        """
        obrigatorios = self.listar_documentos_obrigatorios()
        presentes = []
        faltantes = []
        
        for doc in obrigatorios:
            if any(doc in d for d in documentos_disponiveis):
                presentes.append(doc)
            else:
                faltantes.append(doc)
        
        return {
            'completo': len(faltantes) == 0,
            'presentes': presentes,
            'faltantes': faltantes
        }
    
    def criar_pacote_light(self, documentos, nome_pacote=None):
        """
        Cria um pacote ZIP apenas com os documentos obrigatórios para Light
        """
        if not nome_pacote:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            nome_pacote = f"light_projeto_{self.projeto_id}_{timestamp}.zip"
        
        # Verifica documentos obrigatórios
        verificacao = self.verificar_documentos(documentos.keys())
        
        if not verificacao['completo']:
            return {
                'sucesso': False,
                'erro': 'Documentos obrigatórios faltantes',
                'faltantes': verificacao['faltantes'],
                'mensagem': 'Complete os documentos antes de enviar à Light'
            }
        
        # Cria pasta temporária apenas com documentos Light
        pasta_light = self.pasta_projeto / "para_light"
        pasta_light.mkdir(exist_ok=True)
        
        # Copia apenas os documentos obrigatórios
        for doc_nome, doc_caminho in documentos.items():
            if any(obrig in doc_nome for obrig in verificacao['presentes']):
                destino = pasta_light / Path(doc_caminho).name
                import shutil
                shutil.copy2(doc_caminho, destino)
        
        # Cria ZIP
        caminho_zip = self.pasta_projeto / nome_pacote
        with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for arquivo in pasta_light.glob('*'):
                zipf.write(arquivo, arquivo.name)
        
        return {
            'sucesso': True,
            'pacote': str(caminho_zip),
            'documentos': verificacao['presentes'],
            'mensagem': 'Pacote Light pronto para envio'
        }
    
    def gerar_relatorio_envio(self):
        """
        Gera relatório do que será enviado à Light
        """
        relatorio = {
            'projeto_id': self.projeto_id,
            'tipo_projeto': self.tipo_projeto,
            'data': datetime.datetime.now().isoformat(),
            'documentos_obrigatorios': self.listar_documentos_obrigatorios(),
            'status': 'Aguardando documentos',
            'observacoes': [
                'Este pacote contém APENAS documentos oficiais exigidos pela Light',
                'Documentos internos NÃO devem ser incluídos'
            ]
        }
        return relatorio


# Exemplo de uso
if __name__ == "__main__":
    # Criar empacotador para projeto coletivo
    empacotador = EmpacotadorLight(projeto_id=2301, tipo_projeto='COLETIVA')
    
    # Simular documentos disponíveis
    documentos = {
        'solicitacao_ligacao': 'docs/solicitacao.pdf',
        'projeto_entrada': 'docs/projeto.pdf',
        'art_projeto': 'docs/art_projeto.pdf',
        'art_execucao': 'docs/art_execucao.pdf',
        'carta_smlc': 'docs/carta_smlc.pdf',
    }
    
    # Verificar se está completo
    verificacao = empacotador.verificar_documentos(documentos.keys())
    print(f"📋 Documentos completos: {verificacao['completo']}")
    
    if verificacao['completo']:
        # Criar pacote
        resultado = empacotador.criar_pacote_light(documentos)
        print(f"✅ Pacote criado: {resultado['pacote']}")
    else:
        print(f"❌ Faltam: {verificacao['faltantes']}")
