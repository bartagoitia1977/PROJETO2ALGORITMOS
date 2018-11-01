from Corpus import Corpus
import os
listaref = []
list_ref = os.listdir("dados/src")
for filename in list_ref:
	listaref.append("dados/src/" + filename)

listasusp = []
list_susp = os.listdir("dados/susp")
for file in list_susp:
	listasusp.append("dados/susp/" + file)

work = Corpus(listaref)

for susp in listasusp:
	print("Testando arquivo suspeito",susp,"aguarde...")
	lista = work.VerificarPlagio(susp,0.1)
	print("Arquivos provaveis fontes de possivel plagio",susp + ":",lista)
	ask = str(input("Deseja continuar? s/n: "))
	if (ask == "s"):
		pass
	if (ask == "n"):
		break


