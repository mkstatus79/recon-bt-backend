#!/usr/bin/env python3
"""
Script para gerar pacote completo do projeto
Reúne todos os módulos e gera documentação
"""

import sys
import os
import json
import datetime
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.calculos.secao_a import calcular_secao_a, Cargas
from app.core.calculos.secao_b import calcular_secao_b
from app.core.dimensionamento.tabelas_dim import (
    dimensionar_individual, dimensionar_coletivo,
    eletroduto_aereo, eletroduto_subterraneo
)
from app.core.dimensionamento.aterramento import dimensionar_aterramento_completo
from app.services.documentos.gerador_memorial import GeradorMemorial
from app.services.documentos.gerador_formularios import GeradorFormularios

class GeradorPacoteCompleto:
    def __init__(self, nome_projeto="projeto_recon_bt"):
        self.nome_projeto = nome_projeto
        self.data = datetime.datetime.now()
        self.pasta_saida = Path(f"pacotes/{nome_projeto}_{self.data.strftime('%Y%m%d_%H%M%S')}")
        self.pasta_saida.mkdir(parents=True, exist_ok=True)
        
        self.dados_projeto = {}
        self.resultados = {}
        
    def coletar_dados(self):
        """Coleta dados do projeto (simulado - em produção viria do frontend)"""
        print("\n📋 COLETANDO DADOS DO PROJETO...")
        
        self.dados_projeto = {
            # Dados gerais
            "empreendimento": "Edifício Solar",
            "endereco": "Rua das Flores, 123 - Centro - Rio de Janeiro/RJ",
            "cliente": "Construtora Modelo Ltda",
            "cliente_cpf_cnpj": "12.345.678/0001-90",
            "cliente_telefone": "(21) 99999-9999",
            "cliente_email": "construtora@email.com",
            "responsavel": "Eng. Marcos",
            "crea": "2026123456",
            "art": "202600123456",
            
            # Características da edificação
            "tipo_entrada": "COLETIVA",
            "num_ucs": 24,
            "area_total": 1680,
            "tensao": "220/127V",
            "fases": 3,
            "tipo_rede": "aereo",
            
            # Dados para cálculos
            "unidades": [
                {"area": 70, "quantidade": 24, "com_aquecimento": True}
            ],
            "servico_kva": 18.71,
            "secao_fase": 95,
        }
        
        print("✅ Dados coletados")
        return self.dados_projeto
    
    def executar_calculos(self):
        """Executa todos os cálculos do projeto"""
        print("\n📊 EXECUTANDO CÁLCULOS...")
        
        # Seção B (coletiva)
        from app.core.calculos.secao_b import calcular_secao_b
        self.resultados["secao_b"] = calcular_secao_b(
            self.dados_projeto["unidades"],
            self.dados_projeto["servico_kva"]
        )
        print("  ✅ Seção B calculada")
        
        # Dimensionamento individual (para referência)
        demanda_ramal = self.resultados["secao_b"]["demanda_ramal"]
        self.resultados["dimensionamento"] = dimensionar_individual(demanda_ramal)
        print("  ✅ Dimensionamento calculado")
        
        # Eletrodutos
        self.resultados["eletrodutos"] = {
            "aereo": eletroduto_aereo(demanda_ramal),
            "subterraneo": eletroduto_subterraneo(demanda_ramal)
        }
        print("  ✅ Eletrodutos dimensionados")
        
        # Aterramento
        dados_aterro = {
            "tipo_entrada": self.dados_projeto["tipo_entrada"],
            "num_ucs": self.dados_projeto["num_ucs"],
            "demanda_kva": demanda_ramal,
            "secao_fase": self.dados_projeto["secao_fase"],
            "tipo_rede": self.dados_projeto["tipo_rede"]
        }
        self.resultados["aterramento"] = dimensionar_aterramento_completo(dados_aterro)
        print("  ✅ Aterramento dimensionado")
        
        return self.resultados
    
    def preparar_dados_memorial(self):
        """Prepara dados para o memorial descritivo"""
        demanda_ramal = self.resultados["secao_b"]["demanda_ramal"]
        
        return {
            **self.dados_projeto,
            "data": self.data.strftime('%d/%m/%Y'),
            "data_hora": self.data.strftime('%d/%m/%Y %H:%M'),
            "demanda_ramal": round(demanda_ramal, 2),
            "demanda_protecao": round(self.resultados["secao_b"]["demanda_protecao_geral"], 2),
            "demanda_servico_total": self.dados_projeto["servico_kva"],
            "condutor_fase": "95",
            "condutor_neutro": "95",
            "condutor_protecao": self.resultados["aterramento"]["condutor_protecao"],
            "disjuntor": self.resultados["dimensionamento"]["disjuntor"] if self.resultados["dimensionamento"] else 175,
            "disjuntor_ka": self.resultados["aterramento"]["capacidade_disjuntor_ka"],
            "caixa_protecao": "CPG200",
            "caixa_medicao": "CSM600",
            "painel_medidores": "PDMD2-24",
            "eletroduto_aereo": self.resultados["eletrodutos"]["aereo"],
            "eletroduto_sub": self.resultados["eletrodutos"]["subterraneo"],
            "num_hastes": self.resultados["aterramento"]["num_hastes"],
            "condutor_aterramento": self.resultados["aterramento"]["condutor_interligacao"],
        }
    
    def gerar_documentos(self):
        """Gera todos os documentos do projeto"""
        print("\n📄 GERANDO DOCUMENTOS...")
        
        # Memorial descritivo
        gerador_memorial = GeradorMemorial()
        dados_memorial = self.preparar_dados_memorial()
        memorial = gerador_memorial.gerar_memorial(
            dados_memorial,
            output_dir=str(self.pasta_saida)
        )
        print(f"  ✅ Memorial: {memorial['arquivo_pdf'] if memorial['sucesso'] else 'HTML salvo'}")
        
        # Formulários
        gerador_form = GeradorFormularios()
        gerador_form.output_dir = str(self.pasta_saida)
        
        formularios = gerador_form.gerar_solicitacao_ligacao(self.dados_projeto)
        print(f"  ✅ Formulário: {formularios['arquivo_json']}")
        
        art = gerador_form.gerar_art_minuta(self.dados_projeto)
        print(f"  ✅ ART: {art['arquivo_json']}")
        
        # Lista de materiais
        materiais = gerador_form.gerar_lista_materiais(self.dados_projeto)
        print(f"  ✅ Lista materiais: {materiais['arquivo_json']}")
        
        # Salvar resultados completos
        with open(self.pasta_saida / "resultados_completos.json", "w") as f:
            json.dump({
                "dados_projeto": self.dados_projeto,
                "resultados": self.resultados,
                "memorial": str(memorial.get('arquivo_pdf', '')),
                "formularios": str(formularios.get('arquivo_json', '')),
            }, f, indent=2, default=str)
        
        return self.pasta_saida
    
    def executar(self):
        """Executa o pipeline completo"""
        print("=" * 60)
        print("🚀 GERADOR DE PACOTE COMPLETO - RECON-BT 2026")
        print("=" * 60)
        print(f"📁 Pasta de saída: {self.pasta_saida}")
        
        self.coletar_dados()
        self.executar_calculos()
        self.gerar_documentos()
        
        print("\n" + "=" * 60)
        print(f"✅ PACOTE GERADO COM SUCESSO!")
        print(f"📂 Pasta: {self.pasta_saida}")
        print("=" * 60)
        
        return self.pasta_saida

if __name__ == "__main__":
    gerador = GeradorPacoteCompleto()
    pasta = gerador.executar()
