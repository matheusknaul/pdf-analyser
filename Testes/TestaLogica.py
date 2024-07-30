classes = ['FISICO', 'QUIMICO', 'MECÂNICO']
produtos = ['Placa óssea', 'Lápis', 'Buzina', 'Chapa de aço']

text = "QUIMICO Lápis Determinação de carbono SMWW 2392 B FISICO Placa óssea Ensaio de tração ABNT NBR 7206 FISICO Chapa de aço Ensaio de compressão ABNT NBR 6743 MECÂNICO Buzina Ensaio de frequência ABNT NBT 58934"

resultClasses = []
resultProdutos = []
lista_master = []

def searchElement(text, listAnalys, listResult):
    for element in listAnalys:
        lista =  []
        match = text.find(element)
        lista.append(element)
        lista.append(text[match+len(element):])
        listResult.append(lista)

def testSearchElement(text, listAnalys, listResult):
    for listAnalys in text:
        print(listAnalys)

testSearchElement(text, classes, resultClasses)

def createRow():
    pass

def formartResult(listResult, listAnalys):
    for result in listResult:
        indices = []
        lista = []
        for element in listAnalys:
            match = result[1].find(element)
            indices.append(match)
        valid_indices = [index for index in indices if index != -1]
        if valid_indices:
            lista.append(result[0])
            frase = result[1]
            lista.append(frase[:min(valid_indices)])
            lista_master.append(lista)
        else:
            print('Not found')

searchElement(text, classes, resultClasses)
formartResult(resultClasses, classes)

for result in resultClasses:
    print(result)

