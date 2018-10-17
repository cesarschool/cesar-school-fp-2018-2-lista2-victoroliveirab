## QUESTÃO 3 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from string import ascii_lowercase
def main():
    #print("questao 3")
        entrada = input("Digite sua cifra em formato ROT + <chave> + ' ' + 'mensagem'. ")
    if entrada[:3] != "ROT":
        print("Erro")
    else:
        cifra = int(entrada[3:5])
        cifrado = ascii_lowercase[cifra:] + ascii_lowercase[:cifra]
        msg = ''
        if entrada[5] == " " or entrada[5] == ",":
            i = 6
        else:
            i = 5
        while i < len(entrada):
            if entrada[i].isalpha():
                if entrada[i].isupper():
                    msg += cifrado[ascii_lowercase.index(entrada[i].lower())].upper()
                else:
                    msg += cifrado[ascii_lowercase.index(entrada[i])]
            else:
                if entrada[i] in " .,!?":
                    msg += entrada[i]
                else:
                    msg = "Erro"
                    break
            i+=1

        print(msg)

    
if __name__ == '__main__':
    main()
