###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-10-10
#
# Descricao:  PROJETO1B - CLASSE DOCUMENTO
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np
from Ngrama import Ngrama

class Documento:
	'''
	CLASSE DOCUMENTO
	'''
	def __init__(self,documento):
		self._documento = documento
		
	def palavras(self):
		'''
		Concentra todas as palavras do documento adotando filtro de letras minusculas e minimizando
		a poluição por caracteres alheios: espacos, pontos de interrogacao, exclamacao, etc.
		'''
		self._lista_de_palavras = np.array([])
		self._nova_palavra = True
		self._palavra = ""
		for letra in self._documento:
			if ((letra != " ") and (letra != ".") and (letra != ",") and (letra != "\n") and (letra != ";") and
			 (letra != "?") and (letra != '"') and (letra != "(") and (letra != ")") and (letra != "[") and
			  (letra != "]") and (letra != "{") and (letra != "}") and (letra != '\'') and (letra != "*") and
			   (letra != "!") and (letra != "+") and (letra != "-") and (letra != ":") and (letra != "/") and
			    (letra != "	") and (letra != "\xa0")):
				if (ord(letra) >= 65) and (ord(letra) <= 90):
					self._palavra += chr(ord(letra) + 32)
					self._nova_palavra = True
				else:
					self._palavra += letra
					self._nova_palavra = True
			else:
				if (self._nova_palavra == True):
					self._lista_de_palavras = np.append(self._lista_de_palavras,self._palavra)
					self._palavra = ""
					self._nova_palavra = False
		if (self._nova_palavra == True):
			self._lista_de_palavras = np.append(self._lista_de_palavras,self._palavra)
			self._palavra = ""

		return self._lista_de_palavras

	def gerarNGramas(self):
		'''
		Gera lista encadeada contendo todos os Ngramas (5-grama) de um dado vetor de palavras.
		Documento1
		'''
		self._lista_palavras = self.palavras()
		self._lista_de_ngramas = np.array([])
		self._indice_ngrama = 0
		for ng in range(len(self._lista_palavras) - 4):
			self._cincograma = Ngrama(self._lista_palavras,self._indice_ngrama)
			self._lista_de_ngramas = np.append(self._lista_de_ngramas,self._cincograma.cincoG_intervalo())
			self._indice_ngrama += 1
		return self._lista_de_ngramas