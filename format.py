from Testes.text import text, area_atividade, classes, produtos
import re
from TesteReContinuos import areaInterval
from search import searchElement

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
    