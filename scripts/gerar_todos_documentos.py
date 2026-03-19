#!/usr/bin/env python3
"""
Script para gerar todos os documentos de uma vez
Útil para testar o sistema completo
"""

import sys
import os
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.documentos.light.gerador_solicitacao import GeradorSolicitacaoLight
from app.services.documentos.light.gerador_psd import GeradorPSD
from app.services.documentos.light.gerador_carta_smlc import GeradorCartaSMLC
from app.services.documentos.light.gerador_termo_gerador import GeradorTermoGerador
from app.services.documentos.interno.gerador_memorial_calculo import GeradorMemorialCalculo
from app.services.documentos.interno.gerador_lista_expandida import GeradorListaExpandida
from app.services.documentos.interno.gerador_checklist import GeradorChecklist

def gerar_tudo():
    """Gera todos os documentos de uma vez"""
    
    print("=" * 60)
    print("🚀 GERADOR DE TODOS OS DOCUMENTOS")
    print("=" * 60)
    
    # Dados base do projeto
    dados_projeto = {
        'nome': 'Edifício Solar',
        'cliente_nome': 'João da Silva',
        'cliente_cpf_cnpj': '123.456.789-00',
        'endereco_logradouro': 'Rua das Flores',
        'endereco_numero': '123',
        'endereco_bairro': 'Centro',
        'tipo_entrada': 'COLETIVA',
        'num_ucs': 24,
        'area_total': 1680,
        'responsavel_nome': 'Eng. Marcos',
        'responsavel_crea': '2026123456',
        'num_hastes': 6
    }
    
    resultados = {}
    
    # Documentos Light
    print("\n📄 GERANDO DOCUMENTOS LIGHT...")
    
    solic = GeradorSolicitacaoLight()
    res = solic.gerar_para_light(dados_projeto)
    resultados['solicitacao'] = res
    print(f"  ✅ Solicitação: {res['documento_oficial']}")
    
    psd = GeradorPSD()
    res = psd.gerar_para_light(dados_projeto)
    resultados['psd'] = res
    print(f"  ✅ PSD: {res['documento']}")
    
    # Documentos Internos
    print("\n📋 GERANDO DOCUMENTOS INTERNOS...")
    
    memorial = GeradorMemorialCalculo()
    res = memorial.gerar_memorial(dados_projeto)
    resultados['memorial'] = res
    print(f"  ✅ Memorial: {res['arquivo']}")
    
    lista = GeradorListaExpandida()
    res = lista.gerar_lista({})
    resultados['lista'] = res
    print(f"  ✅ Lista materiais: {res['csv']}")
    print(f"  💰 Total estimado: R$ {res['total']:.2f}")
    
    checklist = GeradorChecklist()
    res = checklist.gerar_checklist(dados_projeto)
    resultados['checklist'] = res
    print(f"  ✅ Checklist: {res['arquivo']}")
    
    print("\n" + "=" * 60)
    print("✅ TODOS OS DOCUMENTOS GERADOS COM SUCESSO!")
    print("=" * 60)
    
    return resultados

if __name__ == "__main__":
    gerar_tudo()
