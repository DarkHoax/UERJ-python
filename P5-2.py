def pesquisa_binaria(lista, item):
	comeco = 0
	fim = len(lista)-1
	meio = (len(lista)-1) // 2
	while True:
		if len(lista) <= 1:
			return meio
		if item == lista[meio]:
			return meio # endereço
		elif item < lista[meio]:
			fim = meio
		elif item > lista[meio]:
			comeco = meio
		if meio == comeco:
			return -1
		meio = (fim + comeco) //2



def escrever_arquivo(aam):
	arquivo = open('aam.txt', 'w')
	while True:
        nome = input('insira o nome: ')
        if nome == '': break
        while True:
            try:
                salario = float(input("insira o salario (-1 para cancelar):"))
                if salario < 1000.00 or salario >999999.99: raise ValueError
                frase = nome + " " + str(salario) + "\n"
                arquivo.write(frase)

	        except ValueError:
		        print('salario deve ser um numero')

	arquivo.close()

def nome_em_arquivo(nome_procurado, aam):
	arquivo = open('aam.txt', 'r')
	linhas = []
	for linha in arquivo:
		
		palavras = linha.split(" ") # forma lista de palavras na linha do arquivo
		nome = ""
		
		for item in palavras: # procura em todos os itens na lista acrescenta os que nao sao convertiveis pra numero == palavras
			try:
				int(item)
			except ValueError:
				nome += item + " "

		salario = palavras[len(palavras)-1] # o ultimo na lista sempre sera o salario
		nome = nome[:-1] # tira o ultimo espaço
		dados = [nome, salario]
		linhas.append(dados)

	nomes = []

	for dado in linhas:
		nomes.append(dado[0])
	#print(nomes)
	resultado = pesquisa_binaria(nomes, nome_procurado) # o endereco sera o mesmo na lista dados

	if resultado == -1:
		print('{} NÃO ESTÁ NO ARQUIVO!'.format(nome_procurado))
	else:
		print("NOME ENCONTRADO NO ARQUIVO!")
		print("Nome:" + linhas[resultado][0])
		print("Salario:" + str(linhas[resultado][1]))

	arquivo.close()


aam = input("insira nome arq: ")
escrever_arquivo(aam)
nome_procurado = input("insira nome procurado")
nome_em_arquivo(nome_procurado, aam)