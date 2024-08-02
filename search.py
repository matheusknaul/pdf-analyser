import re
from Testes.text import text, area_atividade, classes, produtos
from TesteReContinuos import areaInterval

def searchElement(text, elementList):
    results = []

    for element in elementList:
        matchArea = [element]
        matches = re.finditer(element, text)
        for match in matches:
            indexMatch = []
            indexMatch.append(match.start())
            indexMatch.append(match.end())
            matchArea.append(indexMatch)
        results.append(matchArea)

    indices = []

    for result in results:
        i = 1
        while i < len(result):
            index = []
            index.append(result[0])
            index.append(result[i][0])
            indices.append(index)
            i += 1;

    indices = sorted(indices, key=lambda x: x[1])

    areaInterval = []

    i = 0
    while True:
        if i >= len(indices):
            break
        try:
            interval = []
            interval.append(indices[i][0])
            interval.append(indices[i][1])
            interval.append(indices[i+1][1])
            areaInterval.append(interval)
            i += 1
        except Exception as e:
            print(e)
            break
    
    return areaInterval

#intervalList = searchElement(text, area_atividade)
def formatResult(intervalList):
    formatted_result = []
    current_class = None
    current_start = None
    current_end = None

    for entry in intervalList:
        classification, start, end = entry
        if classification != current_class: 
            if current_class is not None:
                formatted_result.append([current_class, current_start, current_end])
            current_class = classification
            current_start = start
            current_end = end
        else:
            current_end = end

    if current_class is not None:
        formatted_result.append([current_class, current_start, current_end])

    return formatted_result

intervalListActivity = searchElement(text, area_atividade)
formattedResultActivity = formatResult(intervalListActivity)

intervalListClass = searchElement(text, classes)
formattedResultClass = formatResult(intervalListClass)

intervalListProducts = searchElement(text, produtos)
formattedResultProducts = formatResult(intervalListProducts)


preparingRow = []

for area in formattedResultActivity:
    setRow = []
    setRow.append(area[0])
    for product in formattedResultProducts:
        interval = []
        if product[1] >= area[1] and area[2] >= product[2]:
            interval.append(product[0])
            interval.append(product[1])
            interval.append(product[2])
            setRow.append(interval)

    preparingRow.append(setRow)

print(preparingRow[0])

import pandas as pd

linhas = []

for row in preparingRow:
    i = 1
    while i != len(row):
        dataRow = {
            'Área de atividade':row[0],
            'Produtos': row[i][0],
            'Descrição':text[row[i][1]+len(row[i][0]):row[i][2]]
        }
        linhas.append(dataRow)
        i+=1

df = pd.DataFrame(linhas)

df.to_excel('Scrap.xlsx', index=False)
    

