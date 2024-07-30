classes = ['MECÂNICO', 'QUIMICO', 'FISICO']
produtos = ['Placa óssea', 'Lápis', 'Buzina', 'Chapa de aço']

text = "QUIMICO Lápis Determinação de carbono SMWW 2392 B FISICO Placa óssea Ensaio de tração ABNT NBR 7206 FISICO Chapa de aço Ensaio de compressão ABNT NBR 6743 MECÂNICO Buzina Ensaio de frequência ABNT NBT 58934 QUIMICO Lápis Determinação de piroca SMWW 2392 B"

def getIndices(listAnalys, text):
    indices = []
    results = []
    for element in listAnalys:
        start = 0
        while True:
            start = text.find(element, start)
            if start == -1:
                break
            indices.append(start)
            start += len(element)

    indices = sorted(set(indices))

    print(indices)
    i = 0
    while i < len(indices):
        if i == len(indices) - 1:
            results.append(text[indices[i]:])
        else:
            results.append(text[indices[i]:indices[i + 1]])
        i += 1

    return results

print(getIndices(classes, text))