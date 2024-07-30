classes = ['MECÂNICO','QUIMICO', 'FISICO']
produtos = ['Placa óssea', 'Lápis', 'Buzina', 'Chapa de aço']

text = "QUIMICO Lápis Determinação de carbono SMWW 2392 B FISICO Placa óssea Ensaio de tração ABNT NBR 7206 MECÂNICO Chapa de aço Ensaio de compressão ABNT NBR 6743 FISICO Buzina Ensaio de frequência ABNT NBT 58934"

def getIndices(listAnalys, text):
    index = []
    result = []
    for element in listAnalys:
        match = text.find(element)
        index.append(match)
    index = sorted(index)
    print(index)
    i = 0
    while i <= len(index) - 1:
        if i == len(index) - 1:
            result.append(text[index[i]:])
            print(i)
        else:
            print(i)
            result.append(text[index[i]:index[i+1]])
        i = i + 1
    return result
        
print(getIndices(classes, text))