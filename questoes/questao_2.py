## QUESTÃO 2 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
	x = y = 0 #espaço inicial x = 0 e y = 0
    while True:
    	comando = input("Digite comando: ") #recebe comando do teclado
    	if len(comando) == 0: #se o comando for vazio, encerra loop
    		break
    	direcao = comando[:comando.index(" ")] #direcao é a substring do começo ate o espaço
    	if comando[comando.index(" ")+1:].isdigit(): #se a partir do espaço, o que sobra é um digito, atribui a q
    		qtd = int(comando[comando.index(" ")+1:])
    	else: #se a partir do espaço há um input invalido, a quantidade é invalida e a entrada é descartada
    		continue
    	if direcao == "CIMA": #se foi pra cima, aumenta a coordenada y
    		y += qtd
    	elif direcao == "BAIXO": #se foi pra baixo, diminui a coordenada y
    		y -= qtd
    	elif direcao == "ESQUERDA": #se foi pra esquerda, diminui a coordenada x
    		x -= qtd
    	elif direcao == "DIREITA": #se foi pra direita, aumenta a coordenada x
    		x += qtd
    	else: #direcao invalida, desconsidera a entrada
    		continue
    print(round((x**2 + y**2)**.5)) #imprime na tela a distancia como o inteiro mais proximo do resultado


    
if __name__ == '__main__':
    main()
