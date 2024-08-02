from Testes.text import text, area_atividade, classes, produtos
import re

results = []

for area in area_atividade:
    matchArea = [area]
    matches = re.finditer(area, text)
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

for indice in indices:
    print(indice)

# matches = re.finditer('is', frase)

# for match in matches:
#     start = match.start()
#     end = match.end()

