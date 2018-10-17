## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    ano = int(input("Ano: "))
    mes = int(input("Mes: "))
    dia = int(input("Dia: "))
    bissexto = False
    if ano % 4 == 0:
        if ano % 100:
            bissexto = True
        else:
            if ano % 400 == 0:
                bissexto = True
    if dia >= 28:
        if mes == 2:
            if dia == 28 and not bissexto:
                dia = 0
                mes = 3
        else:
            if dia == 30:
                if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    mes += 1
                    dia = 0
            elif dia == 31:
                dia = 0
                if mes == 12:
                    mes = 1
                    ano += 1
                else:
                    mes += 1

    print("{:0>4}-{:0>2}-{:0>2}".format(ano,mes,dia+1))

    
if __name__ == '__main__':
    main()
