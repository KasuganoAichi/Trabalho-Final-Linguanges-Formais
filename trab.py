
def fA():
	return 'Automato minimo'
	
def fB():
	return 'Lista de Palavras'
	
def fC():
	return 'GR Equivalente'
	
def fD():
	return 'Igualdade de Automatos'
	
def fechar():
	return 'Bye bye'
	
	
#Switch para as letras a-d
#As funções são definidas acima, e troca o nome da string pela chamada dela
def switch_demo(argument):
        
        switcher = {'a': fA(), 'b': fB(), 'c': fC(), 'd': fD(), 'e': fechar()}
        print(argument)
        print (switcher.get(argument, "OPCAO INVALIDA"))
	

def main():
	argument = 1
	while argument!=0:
		print("Escolha sua opcao: \na. Criar automato minimo\nb. Testar lista de palavras (num automato minimo)\nc. Criar a Gramatica Regular equivalente\nd. Verificar equivalencia entre automatos\n(e para fechar)")
		argument = input()
		switch_demo(argument)
		if argument=='e':
		    break

if __name__ == "__main__":
	main()
