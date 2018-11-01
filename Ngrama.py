###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-10-28
#
# Descricao:  PROJETO2B - CLASSE NGRAMA
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

class Ngrama:
	'''
	Ngrama(vetor - lista ou vetor numpy, indice da primeira sequencia de caracteres)
	Vai retornar a primeira e a ultima palavras em sequencia de caracteres de
	um intervalo de 5 palavras.
	'''
	def __init__(self,vetor,indice_inicio):
		self._indice_inicio = indice_inicio
		self._vetor = vetor
				
	def cincoG_intervalo(self):		
		if (self._indice_inicio > (len(self._vetor) - 5)):
			raise IndexError
		else:
			self._palavra1 = self._vetor[self._indice_inicio]
			self._palavra5 = self._vetor[self._indice_inicio + 4]
			self._chrGrama = self._palavra1 + self._palavra5
		return str(self._chrGrama)

	def __str__(self):
		return "'" + str(self._chrGrama) + "'"

	def __repr__(self):
		return "Ngrama('" + str(self._chrGrama) + "')"	