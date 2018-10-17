## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

from string import ascii_lowercase, ascii_uppercase, digits
chars_especiais = "$#@"
def main1():
    #print("questao 1")
    senhas = input("Digite as senhas a serem verificadas:\n")
    i = 0
    senhas_aceitas=''
    while i < len(senhas):
        if senhas[i] == " ":
            i+=1
            continue
        tem_minusculo = tem_numero = tem_maiusculo = tem_especial = False
        senha=''
        while i < len(senhas) and senhas[i] != "," and senhas[i] != " ":
            senha+=senhas[i]
            if senhas[i] in ascii_lowercase:
                tem_minusculo = True
            if senhas[i] in ascii_uppercase:
                tem_maiusculo = True
            if senhas[i].isdigit():
                tem_digito = True
            if senhas[i] in chars_especiais:
                tem_especial = True
            i+=1
        if tem_minusculo and tem_maiusculo and tem_digito and tem_especial:
            if len(senha) >= 6 and len(senha) <= 12:
                senhas_aceitas += senha + ", "
        i+=1
    print(senhas_aceitas[:-2])


if __name__ == '__main__':
    main()
