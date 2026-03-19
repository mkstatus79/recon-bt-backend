# ============================================
# MÓDULO DE VALIDAÇÃO DE REGRAS - RECON-BT 2026
# Implementa todas as regras de negócio da automação
# ============================================

import datetime
import re
from typing import Dict, List, Any, Optional

# --------------------------------------------
# REG-BT-001: Validação de Limite de Carga BT
# --------------------------------------------
class ValidadorLimiteCarga:
    """
    Verifica se a carga solicitada enquadra-se em BT ou deve ir para MT
    Base: RECON-BT 2026, Fascículo 04, Item 1.3.1.1
    """
    
    LIMITE_BT_INDIVIDUAL = 76  # kVA
    LIMITE_BT_COLETIVA_RES = 300  # kVA
    LIMITE_BT_COLETIVA_NRES = 225  # kVA
    
    @classmethod
    def validar(cls, tipo_ligacao: str, carga_kva: float, tipo_ocupacao: str = "RESIDENCIAL") -> Dict[str, Any]:
        """
        Valida se carga está dentro dos limites BT
        
        Args:
            tipo_ligacao: "INDIVIDUAL" ou "COLETIVA"
            carga_kva: Demanda em kVA
            tipo_ocupacao: "RESIDENCIAL", "NAO_RESIDENCIAL" ou "MISTA"
        
        Returns:
            Dict com resultado da validação
        """
        resultado = {
            "valido": True,
            "mensagem": "Carga dentro dos limites BT",
            "bloqueio": False,
            "redirecionamento": None
        }
        
        if tipo_ligacao == "INDIVIDUAL":
            if carga_kva > cls.LIMITE_BT_INDIVIDUAL:
                resultado["valido"] = False
                resultado["bloqueio"] = True
                resultado["mensagem"] = (
                    f"Carga de {carga_kva} kVA superior ao limite de {cls.LIMITE_BT_INDIVIDUAL} kVA "
                    "para atendimento individual em BT."
                )
                resultado["redirecionamento"] = "RECON-MT"
        
        elif tipo_ligacao == "COLETIVA":
            limite = cls.LIMITE_BT_COLETIVA_RES if tipo_ocupacao == "RESIDENCIAL" else cls.LIMITE_BT_COLETIVA_NRES
            if carga_kva > limite:
                resultado["valido"] = False
                resultado["bloqueio"] = True
                resultado["mensagem"] = (
                    f"Carga de {carga_kva} kVA superior ao limite de {limite} kVA "
                    f"para entrada coletiva {tipo_ocupacao.lower()} em BT."
                )
                resultado["redirecionamento"] = "COMPARTIMENTO_TRANSFORMACAO"
        
        return resultado


# --------------------------------------------
# REG-BT-002: Obrigatoriedade de Aprovação Prévia
# --------------------------------------------
class ValidadorAprovacaoPrevia:
    """
    Verifica se projeto precisa de aprovação prévia da Light
    Base: REN 1000/2021, Art. 50; RECON-BT 2026
    """
    
    PRAZO_VALIDADE_DIAS = 540  # 18 meses
    
    @classmethod
    def validar(cls, tipo_ligacao: str, carga_kva: float, possui_projeto: bool = False) -> Dict[str, Any]:
        """
        Valida necessidade de projeto aprovado
        
        Args:
            tipo_ligacao: "INDIVIDUAL" ou "COLETIVA"
            carga_kva: Demanda em kVA
            possui_projeto: Se já possui projeto aprovado
        
        Returns:
            Dict com resultado da validação
        """
        resultado = {
            "exige_projeto": False,
            "bloqueio": False,
            "mensagem": "",
            "codigo_aprovacao": None
        }
        
        # Casos que exigem projeto
        if tipo_ligacao == "COLETIVA":
            resultado["exige_projeto"] = True
            resultado["mensagem"] = "Entrada coletiva exige projeto aprovado pela Light"
        elif tipo_ligacao == "INDIVIDUAL" and carga_kva > 76:
            resultado["exige_projeto"] = True
            resultado["mensagem"] = "Carga > 76 kVA em entrada individual exige projeto aprovado"
        
        # Verifica se já tem projeto
        if resultado["exige_projeto"]:
            if not possui_projeto:
                resultado["bloqueio"] = True
                resultado["mensagem"] += " - Necessário upload do protocolo de aprovação"
        
        return resultado
    
    @classmethod
    def validar_validade(cls, data_aprovacao: datetime.date) -> Dict[str, Any]:
        """
        Verifica se projeto aprovado ainda está dentro do prazo
        """
        hoje = datetime.date.today()
        dias_validade = (hoje - data_aprovacao).days
        
        resultado = {
            "valido": dias_validade <= cls.PRAZO_VALIDADE_DIAS,
            "dias_restantes": cls.PRAZO_VALIDADE_DIAS - dias_validade,
            "expirado": dias_validade > cls.PRAZO_VALIDADE_DIAS
        }
        
        if resultado["expirado"]:
            resultado["mensagem"] = f"Projeto expirado há {dias_validade - cls.PRAZO_VALIDADE_DIAS} dias"
        elif resultado["dias_restantes"] < 30:
            resultado["alerta"] = f"Projeto expira em {resultado['dias_restantes']} dias"
        
        return resultado


# --------------------------------------------
# REG-TEC-003: Consistência de Dados da ART
# --------------------------------------------
class ValidadorART:
    """
    Valida consistência entre ART e formulário de solicitação
    Base: RECON-BT 2026; Orientação Técnica ART/RRT/TRT
    """
    
    @classmethod
    def validar_consistencia(cls, dados_formulario: Dict, dados_art: Dict) -> Dict[str, Any]:
        """
        Compara dados do formulário com os da ART
        
        Args:
            dados_formulario: Dict com campos do formulário
            dados_art: Dict extraído da ART
        
        Returns:
            Dict com inconsistências encontradas
        """
        inconsistencias = []
        
        # Campos obrigatórios para comparar
        comparacoes = [
            ("carga_kva", "demanda_kva", "carga/demanda"),
            ("endereco_completo", "endereco_obra", "endereço da obra"),
            ("responsavel_crea", "profissional_registro", "registro do profissional"),
            ("cliente_nome", "contratante_nome", "nome do contratante"),
        ]
        
        for campo_form, campo_art, descricao in comparacoes:
            valor_form = dados_formulario.get(campo_form)
            valor_art = dados_art.get(campo_art)
            
            if valor_form and valor_art and str(valor_form).strip() != str(valor_art).strip():
                inconsistencias.append({
                    "campo": descricao,
                    "valor_formulario": valor_form,
                    "valor_art": valor_art
                })
        
        resultado = {
            "consistente": len(inconsistencias) == 0,
            "inconsistencias": inconsistencias,
            "acoes_sugeridas": []
        }
        
        if not resultado["consistente"]:
            resultado["acoes_sugeridas"].append("Emitir ART complementar ou retificadora")
            resultado["mensagem"] = f"{len(inconsistencias)} inconsistência(s) encontrada(s) com a ART"
        
        return resultado


# --------------------------------------------
# REG-BT-004: Elegibilidade para Projeto Simplificado
# --------------------------------------------
class ValidadorProjetoSimplificado:
    """
    Verifica se entrada coletiva pode usar projeto simplificado
    Base: RECON-BT 2026, Fascículo 03, Nota 1
    """
    
    @classmethod
    def validar(cls, num_ucs_residenciais: int, num_ucs_servico: int, demanda_max_uc: float) -> Dict[str, Any]:
        """
        Valida elegibilidade para projeto simplificado
        
        Condições:
        - Até 6 unidades residenciais
        - Até 1 unidade de serviço
        - Demanda individual ≤ 15 kVA
        """
        resultado = {
            "elegivel": False,
            "tipo": "PADRAO",
            "mensagem": "",
            "exigencias": []
        }
        
        # Verifica condições
        condicoes = []
        if num_ucs_residenciais <= 6:
            condicoes.append(True)
        else:
            condicoes.append(False)
            resultado["exigencias"].append(f"Número de UCs residenciais ({num_ucs_residenciais}) excede o limite de 6")
        
        if num_ucs_servico <= 1:
            condicoes.append(True)
        else:
            condicoes.append(False)
            resultado["exigencias"].append(f"Número de UCs de serviço ({num_ucs_servico}) excede o limite de 1")
        
        if demanda_max_uc <= 15:
            condicoes.append(True)
        else:
            condicoes.append(False)
            resultado["exigencias"].append(f"Demanda individual máxima ({demanda_max_uc} kVA) excede o limite de 15 kVA")
        
        # Se todas as condições forem atendidas
        if all(condicoes):
            resultado["elegivel"] = True
            resultado["tipo"] = "SIMPLIFICADO"
            resultado["mensagem"] = "Projeto elegível para fluxo simplificado"
            resultado["exigencias"] = ["Utilizar formulário específico de projeto simplificado"]
        else:
            resultado["tipo"] = "COMPLETO"
            resultado["mensagem"] = "Projeto exige fluxo completo com projeto detalhado"
        
        return resultado


# --------------------------------------------
# REG-BUS-005: Monitoramento de Vistoria e Prazos
# --------------------------------------------
class GestorVistoria:
    """
    Gerencia fluxo pós-vistoria e prazos de correção
    Base: REN 1000/2021, Art. 94
    """
    
    PRAZO_CORRECAO_DIAS = 3  # dias úteis
    PRAZO_RELATORIO_DIAS = 3  # dias úteis
    
    def __init__(self):
        self.pendencias = []
        self.data_vistoria = None
        self.data_limite_correcao = None
    
    def registrar_vistoria(self, status: str, data: datetime.date, observacoes: str = ""):
        """
        Registra resultado da vistoria
        """
        self.data_vistoria = data
        
        if status == "APROVADO":
            return {
                "status": "APROVADO",
                "mensagem": "Vistoria aprovada. Prosseguir para ligação.",
                "proximo_passo": "LIGACAO"
            }
        
        elif status == "REPROVADO":
            # Calcula prazo para correção (dias úteis)
            self.data_limite_correcao = self._calcular_dias_uteis(data, self.PRAZO_CORRECAO_DIAS)
            
            return {
                "status": "REPROVADO",
                "mensagem": "Vistoria reprovada. Necessário correção das pendências.",
                "prazo_correcao": self.data_limite_correcao.isoformat(),
                "dias_para_correcao": self.PRAZO_CORRECAO_DIAS,
                "proximo_passo": "CORRECAO"
            }
    
    def adicionar_pendencia(self, descricao: str, fotos_necessarias: bool = True):
        """
        Adiciona pendência ao relatório de vistoria
        """
        pendencia = {
            "descricao": descricao,
            "fotos_necessarias": fotos_necessarias,
            "corrigida": False,
            "fotos": []
        }
        self.pendencias.append(pendencia)
    
    def registrar_correcao(self, pendencia_idx: int, fotos: List[str] = None):
        """
        Registra correção de uma pendência com evidências fotográficas
        """
        if 0 <= pendencia_idx < len(self.pendencias):
            self.pendencias[pendencia_idx]["corrigida"] = True
            if fotos:
                self.pendencias[pendencia_idx]["fotos"] = fotos
    
    def verificar_correcoes(self) -> Dict[str, Any]:
        """
        Verifica se todas as pendências foram corrigidas dentro do prazo
        """
        hoje = datetime.date.today()
        todas_corrigidas = all(p["corrigida"] for p in self.pendencias)
        
        if hoje > self.data_limite_correcao:
            return {
                "pode_solicitar_nova_vistoria": todas_corrigidas,
                "prazo_expirado": True,
                "mensagem": "Prazo de correção expirado. Necessário justificativa.",
                "pendencias_pendentes": [p for p in self.pendencias if not p["corrigida"]]
            }
        
        return {
            "pode_solicitar_nova_vistoria": todas_corrigidas,
            "prazo_expirado": False,
            "dias_restantes": (self.data_limite_correcao - hoje).days,
            "pendencias_pendentes": [p for p in self.pendencias if not p["corrigida"]]
        }
    
    def _calcular_dias_uteis(self, data_inicio: datetime.date, dias: int) -> datetime.date:
        """
        Calcula data considerando apenas dias úteis
        (simplificado - considera sábado e domingo)
        """
        from pandas import date_range
        
        dias_uteis = 0
        data_atual = data_inicio
        
        while dias_uteis < dias:
            data_atual += datetime.timedelta(days=1)
            if data_atual.weekday() < 5:  # 0-4 = segunda a sexta
                dias_uteis += 1
        
        return data_atual


# --------------------------------------------
# REG-MAT-006: Validação de Fabricantes de Materiais
# --------------------------------------------
class ValidadorMateriais:
    """
    Valida se materiais são de fabricantes homologados pela Light
    Base: Lista de Fabricantes Validados Light
    """
    
    # Lista simulada - em produção, viria de API/banco de dados
    FABRICANTES_VALIDADOS = {
        "CAIXAS": ["MULTIPOL", "FORTLEV", "SCHNEIDER", "SIEMENS"],
        "DISJUNTORES": ["SCHNEIDER", "SIEMENS", "ABB", "GENERAL_ELECTRIC"],
        "POSTES": ["MULTIPOL", "PLASSON", "FORTLEV"],
        "CONDUTORES": ["PRYSMIAN", "NEXANS", "FICAP", "SIL"],
    }
    
    @classmethod
    def validar_material(cls, tipo: str, fabricante: str) -> Dict[str, Any]:
        """
        Valida se fabricante está na lista homologada
        
        Args:
            tipo: "CAIXAS", "DISJUNTORES", "POSTES", "CONDUTORES"
            fabricante: Nome do fabricante
        
        Returns:
            Dict com resultado da validação
        """
        fabricantes_validos = cls.FABRICANTES_VALIDADOS.get(tipo.upper(), [])
        fabricante_upper = fabricante.upper().strip()
        
        # Verifica se está na lista (case insensitive)
        valido = any(fab in fabricante_upper for fab in fabricantes_validos)
        
        resultado = {
            "valido": valido,
            "tipo": tipo,
            "fabricante": fabricante,
            "fabricantes_validos": fabricantes_validos,
            "bloqueio": False
        }
        
        if not valido:
            resultado["bloqueio"] = True
            resultado["mensagem"] = (
                f"Fabricante '{fabricante}' não homologado pela Light para {tipo}. "
                "Risco alto de reprovação em vistoria."
            )
            resultado["acao"] = "Consultar lista oficial no site da Light"
        
        return resultado
    
    @classmethod
    def validar_lista_materiais(cls, materiais: List[Dict]) -> Dict[str, Any]:
        """
        Valida uma lista completa de materiais
        
        Args:
            materiais: Lista de dicts com 'tipo' e 'fabricante'
        
        Returns:
            Dict com resultado consolidado
        """
        resultados = []
        bloqueios = []
        
        for material in materiais:
            validacao = cls.validar_material(material["tipo"], material["fabricante"])
            resultados.append(validacao)
            if validacao.get("bloqueio"):
                bloqueios.append(validacao)
        
        return {
            "valido": len(bloqueios) == 0,
            "resultados": resultados,
            "bloqueios": bloqueios,
            "pode_solicitar_vistoria": len(bloqueios) == 0,
            "mensagem": f"{len(bloqueios)} material(is) não homologado(s) encontrado(s)" if bloqueios else "Todos os materiais são homologados"
        }


# --------------------------------------------
# MÓDULO PRINCIPAL DE VALIDAÇÃO
# --------------------------------------------
class ValidadorReconBT:
    """
    Módulo central de validação que integra todas as regras
    """
    
    def __init__(self):
        self.validacoes = []
        self.erros = []
        self.alertas = []
    
    def validar_projeto(self, dados_projeto: Dict) -> Dict[str, Any]:
        """
        Executa todas as validações para um projeto
        """
        resultado = {
            "valido": True,
            "bloqueios": [],
            "alertas": [],
            "redirecionamentos": [],
            "detalhes": {}
        }
        
        # REG-BT-001: Limite de Carga
        limite = ValidadorLimiteCarga.validar(
            dados_projeto.get("tipo_ligacao", "INDIVIDUAL"),
            dados_projeto.get("carga_kva", 0),
            dados_projeto.get("tipo_ocupacao", "RESIDENCIAL")
        )
        resultado["detalhes"]["limite_carga"] = limite
        if limite.get("bloqueio"):
            resultado["valido"] = False
            resultado["bloqueios"].append(limite["mensagem"])
            if limite.get("redirecionamento"):
                resultado["redirecionamentos"].append(limite["redirecionamento"])
        
        # REG-BT-002: Aprovação Prévia
        aprovacao = ValidadorAprovacaoPrevia.validar(
            dados_projeto.get("tipo_ligacao", "INDIVIDUAL"),
            dados_projeto.get("carga_kva", 0),
            dados_projeto.get("possui_projeto", False)
        )
        resultado["detalhes"]["aprovacao_previa"] = aprovacao
        if aprovacao.get("bloqueio"):
            resultado["valido"] = False
            resultado["bloqueios"].append(aprovacao["mensagem"])
        
        # REG-BT-004: Projeto Simplificado
        if dados_projeto.get("tipo_ligacao") == "COLETIVA":
            simplificado = ValidadorProjetoSimplificado.validar(
                dados_projeto.get("num_ucs_residenciais", 0),
                dados_projeto.get("num_ucs_servico", 0),
                dados_projeto.get("demanda_max_uc", 0)
            )
            resultado["detalhes"]["projeto_simplificado"] = simplificado
            if simplificado["elegivel"]:
                resultado["alertas"].append("Projeto elegível para fluxo simplificado")
        
        return resultado


# --------------------------------------------
# EXEMPLO DE USO
# --------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("TESTE DO MÓDULO DE VALIDAÇÃO DE REGRAS")
    print("=" * 60)
    
    # Teste REG-BT-001
    print("\n📋 REG-BT-001 - Limite de Carga BT")
    print("-" * 40)
    casos = [
        ("INDIVIDUAL", 70, "RESIDENCIAL"),
        ("INDIVIDUAL", 80, "RESIDENCIAL"),
        ("COLETIVA", 250, "RESIDENCIAL"),
        ("COLETIVA", 250, "NAO_RESIDENCIAL"),
    ]
    
    for tipo, carga, ocupacao in casos:
        resultado = ValidadorLimiteCarga.validar(tipo, carga, ocupacao)
        status = "✅" if resultado["valido"] else "❌"
        print(f"{status} {tipo} {carga}kVA ({ocupacao}): {resultado['mensagem']}")
    
    # Teste REG-BT-004
    print("\n📋 REG-BT-004 - Projeto Simplificado")
    print("-" * 40)
    casos = [
        (6, 1, 15, "Vila com 6 casas"),
        (8, 1, 15, "8 apartamentos"),
        (6, 2, 15, "6 aptos + 2 serviços"),
    ]
    
    for ucs, servico, demanda, desc in casos:
        resultado = ValidadorProjetoSimplificado.validar(ucs, servico, demanda)
        tipo = "✅ SIMPLIFICADO" if resultado["elegivel"] else "❌ COMPLETO"
        print(f"{tipo} - {desc}")
