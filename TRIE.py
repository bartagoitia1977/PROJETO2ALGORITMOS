###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-11-04
#
# Descricao:  PROJETO2C - ARVORE TRIE
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

class Folha:
	def __init__(self):
		self._objeto = []
		self._folha = 37*[None]
		self._fim_palavra = False

	@property
	def objeto(self):
		return self._objeto
	@objeto.setter
	def objeto(self,item):
		self._objeto = item

	@property
	def folha(self):
		return self._folha
	@folha.setter
	def folha(self,item):
		self._folha = item

	@property
	def fim_palavra(self):
		return self._fim_palavra
	@fim_palavra.setter
	def fim_palavra(self,item):
		self._fim_palavra = item
	

class TRIE:
	def __init__(self):
		self._root = Folha()
		
	def indexador(self,letra):
		self._letra = letra
		if ((ord(self._letra) >= 97) and (ord(self._letra) <= 122)):
			return ord(self._letra) - 97
		elif ((ord(self._letra) >= 48) and (ord(self._letra) <= 57)):
			return ord(self._letra) - 22
		else:
			return 36

	def inserir(self,chave,objeto):
		self._chave = chave
		self._objeto = objeto
		self._apontador = self._root
		self._tamchave = len(self._chave)
		for cont in range(self._tamchave):
			self._indice = self.indexador(self._chave[cont])
			if (self._apontador.folha[self._indice] is None):
				self._apontador.folha[self._indice] = Folha()
			self._apontador = self._apontador.folha[self._indice]
		self._apontador._fim_palavra = True
		self._apontador.objeto.append(self._objeto)
			
	def procurar(self,chave):
		self._chave = chave
		self._apontador = self._root
		self._tamchave = len(self._chave)
		for cont in range(self._tamchave):
			self._indice = self.indexador(self._chave[cont])
			if (self._apontador.folha[self._indice] is None):
				return False
			self._apontador = self._apontador.folha[self._indice]
		if (not(self._apontador) is None) and (self._apontador.fim_palavra):
			return self._apontador.objeto
		else:
			return False