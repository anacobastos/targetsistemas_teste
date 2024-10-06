#2) Escreva um programa que verifique, em uma string, 
# a existência da letra ‘a’, seja maiúscula ou minúscula, 
# além de informar a quantidade de vezes em que ela ocorre.

#frase = input("Escreva a string a ser lida") 
testes = ['ana caroline','banana','CARAMBA','MacA','Tem um monte de 121212 aaaaaaa','bolo']
for frase in testes:
    quant = frase.count('a')+frase.count('A')
    if(quant==0): print("Não tem 'a' ou 'A' em \"",frase,"\"")
    else: print('tem ',quant,"'a' ou 'A' em \"",frase,"\"")