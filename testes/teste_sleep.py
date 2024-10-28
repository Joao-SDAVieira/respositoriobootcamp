from time import sleep
#20
frase = '''Em linguística, a noção de texto é ampla e 
ainda aberta a uma definição mais precisa. 
Grosso modo, pode ser entendido como 
manifestação linguística das ideias de um autor, 
que serão interpretadas pelo leitor de acordo com 
seus conhecimentos linguísticos e culturais. 
Seu tamanho é variável. "Conjunto de palavras e 
frases articuladas, escritas sobre qualquer suporte". 
"Obra escrita considerada na sua redação original e autêntica". '''
#297
# for i,letter in enumerate(frase):
#     print(i, letter)
    

for i,letter in enumerate(frase):
    if i > 296:
        print(letter,end='')
        sleep(0.07)
    else:
        print(letter,end='')
        sleep(0.02)