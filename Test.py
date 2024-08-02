from search import searchElement, formatResult
from Testes.text import text, area_atividade, classes, produtos
import re
from TesteReContinuos import areaInterval

intervalList = searchElement(text, area_atividade)
formattedResult = formatResult(intervalList)


group = []
# for result in formattedResult:
#     print("-=-=--=-=-=-=-=-==--=-=-==--=-==-=-")
#     print(result)

for result in formattedResult:
    register = []
    register.append(result[0])
    NewIntervalList = searchElement(result[1], classes)
    NewFormattedResult = formatResult(NewIntervalList)
    register.append(NewFormattedResult)
    group.append(register)


final_group = []


for test in group:
    register = []
    register.append(test[0])
    register.append(test[1][0][0])
    NewIntervalList = searchElement(test[1][0][0], produtos)
    NewFormattedResult = formatResult(NewIntervalList)
    register.append(NewFormattedResult)
    final_group.append(register)

print(final_group[0])

# for element in group:
#     print(element)


