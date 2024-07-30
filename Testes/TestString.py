
# text = 'a b c d e f a j k l m n'

# def detectaLetra(text):
#     indices = []
#     for index, letra in enumerate(text):
#         if letra == 'a':
#             print(f'Letra "a" encontrada no índice: {index}')
#             indices.append(index)
        
#     print(text[indices[0]:indices[1]])
#     return print('Deu certo!')
# detectaLetra(text)

# texto = "Bem vindofao lar!"
# palavra = 'vindo'
# len_palavra = len(palavra)
# if texto.find(palavra):
#     print(texto[texto.find(palavra)+len_palavra:])
    

lista_de_opcoes = ['Fala', 'Fita', 'Foca', 'Faca']
frase = 'A Fala da Gabi, foi imitando uma Foca segurando uma Faca para cortar uma Fita'

dicionario = []

def encontra():
    for opcao in lista_de_opcoes:
        lista = []
        match = frase.find(opcao)
        lista.append(opcao)
        lista.append(frase[match+len(opcao):])
        dicionario.append(lista)

lista_master = []

def formata(lista):
    for item in lista:
        indices = []
        lista = []
        for opcao in lista_de_opcoes:
            match = item[1].find(opcao)
            indices.append(match)
        valid_indices = [index for index in indices if index != -1]
        if valid_indices:
            lista.append(item[0])
            frase = item[1]
            lista.append(frase[:min(valid_indices)])
            lista_master.append(lista)
        else:
            print('Not found')

encontra()        
formata(dicionario)

for item in lista_master:
    print(item)
