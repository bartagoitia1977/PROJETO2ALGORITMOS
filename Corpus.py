###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-10-14
#
# Descricao:  PROJETO1B - CLASSE CORPUS
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np
from Ngrama import Ngrama
from Documento import Documento
from TRIE import TRIE

class Corpus:
	'''
	Recebe lista de documentos referencia a serem analisados.
	Dentro da lista como parametro: ["filename1.txt","filename2.txt",...]
	'''

	def __init__(self,lista_de_referencias):
		self._lista_de_referencias = lista_de_referencias

	def VerificarPlagio(self,doc_suspeito,limiar):
		self._doc_suspeito = doc_suspeito
		self._limiar = limiar
		self._dic_acima_do_limiar = {}
		self._susp = open(self._doc_suspeito,"r")
		self._susp_dados = self._susp.read()
		self._listacontencao = []
		self._saida = []
		for filename in self._lista_de_referencias:
			self._ref = open(filename,"r")
			self._ref_dados = self._ref.read()
			self._contencao = self.contencao(self._susp_dados,self._ref_dados)
			if (self._contencao >= self._limiar):
				self._dic_acima_do_limiar[str(self._contencao)] = filename
		for cont in self._dic_acima_do_limiar:
			self._listacontencao.append(cont)
		self._listacontencaoord = self.ordenar(self._listacontencao)
		for valor in self._listacontencaoord:
			self._saida.append(str(self._dic_acima_do_limiar[valor]) + " = " + str("%.2f"%float(valor)))
		return self._saida
		
	def trocar(self,lista,A,B):
		
		self._lista = lista
		self._A = A
		self._B = B
		self._aux = self._lista[self._A]
		self._lista[self._A] = self._lista[self._B]
		self._lista[self._B] = self._aux

	def ordenar(self,lista):
		
		self._lista = lista
		self._tamanho = len(self._lista)
		for e in range((self._tamanho - 1),0,-1):
			for f in range(0,e):
				if float(self._lista[f]) > float(self._lista[f + 1]):
					self.trocar(self._lista,f,f + 1)
		return self._lista

	def contencao(self,doc1,doc2):
		self._doc1 = doc1
		self._doc2 = doc2
		self._doc_doc1 = Documento(self._doc1)
		self._doc_doc2 = Documento(self._doc2)
		self._vet_doc1 = self._doc_doc1.gerarNGramas()
		self._vet_doc2 = self._doc_doc2.gerarNGramas()
		self._trie_doc2 = TRIE()
		for ng in self._vet_doc2:
			self._trie_doc2.inserir(ng,"X")
		self._repeticao = 0
		self._contencao = 0
		for enegrama in self._vet_doc1:
			self._verificador = self._trie_doc2.procurar(enegrama)
			if (self._verificador != False):
				self._repeticao += 1
		self._contencao = (self._repeticao / len(self._vet_doc1))
		return self._contencao