import re
from Testes.text import text, area_atividade, classes, produtos
from TesteReContinuos import areaInterval

def searchElement(text, elementList):
    results = []

    for element in elementList:
        matchArea = [element]
        matches = re.finditer(element, text)
        for match in matches:
            indexMatch = [match.start(), match.end()]
            matchArea.append(indexMatch)
        results.append(matchArea)

    indices = []
    for result in results:
        for i in range(1, len(result)):
            indices.append([result[0], result[i][0], result[i][1]])

    indices = sorted(indices, key=lambda x: x[1])

    areaInterval = []
    i = 0
    while i < len(indices) - 1:
        interval = [indices[i][0], indices[i][1], indices[i+1][1]]
        areaInterval.append(interval)
        i += 1

    return areaInterval

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

# Buscar e formatar elementos
intervalList = searchElement(text, area_atividade)
formattedResult = formatResult(intervalList)
print(formattedResult[0])

group = []
for result in formattedResult:
    register = [result[0]]
    if len(result) > 2:  # Verifica se há intervalos válidos
        start_index = result[1]
        end_index = result[2]
        NewIntervalList = searchElement(text[start_index:end_index], classes)
        NewFormattedResult = formatResult(NewIntervalList)
        register.append(NewFormattedResult)
        group.append(register)

final_group = []
for test in group:
    register = [test[0]]
    if len(test[1]) > 0 and len(test[1][0]) > 2:  # Verifica se há intervalos válidos
        first_class_interval = test[1][0]
        start_index = first_class_interval[1]
        end_index = first_class_interval[2]
        NewIntervalList = searchElement(text[start_index:end_index], produtos)
        NewFormattedResult = formatResult(NewIntervalList)
        register.append(NewFormattedResult)
        final_group.append(register)

#print(final_group[0])

print(text[712:879])