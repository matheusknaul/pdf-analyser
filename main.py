from Classes.row import Row
import re
from PyPDF2 import PdfReader
    
classes = ['ENSAIOS MECÂNICOS', 'ENSAIOS QUÍMICOS', 'ENSAIOS ELÉTRICOS & MAGNÉTICOS', 'ENSAIOS ELÉTRICOS & MAGNÉTICOS E ENSAIOS MECÂNICOS', 'ENSAIOS ELÉTRICOS & MAGNÉTICOS E ENSAIO ACÚSTICO, DE VIBRAÇÃO & CHOQUE', 'ENSAIOS TÉRMICOS', 'ENSAIO ACÚSTICO, DE VIBRAÇÃO & CHOQUE', 'ENSAIOS TÉRMICOS', 'ENSAIO ACÚSTICO, DE VIBRAÇÃO E CHOQUE', 'ENSAIOS MECÂNICOS, ELÉTRICOS E MAGNÉTICOS', 'ENSAIOS BIOLÓGICOS', 'AMOSTRAGEM']
area_atividade = ['PRODUTOS RELACIONADOS A SAÚDE E SEGURANÇA  HUMANA',  'ENSAIOS MECÂNICOS', 'MEIO AMBIENTE', 'ALIMENTOS E BEBIDAS', 'PRODUTOS QUÍMICOS', 'MÁQUINAS E EQUIPAMENTOS', 'MOTORES EQUIPAMENTOS E MATERIAIS ELÉTRICOS', 'ELETRODOMÉSTICOS E SIMILARES', 'AUTOMOTIVA E OUTROS EQUIPAMENTOS DE TRANSPORTE', 'METALURGIA', 'PRODUTOS RELACIONADOS A SAÚDE E SEGURANÇA HUMANA']
produtos = ['PLACAS DE COLUNA', 'PLACAS ÓSSEAS', 'ESPAÇADOR INTERVERTEBRAL', 'BARRAS DE COLUNA', 'PRÓTESE PARCIAL E TOTAL DE ARTICULAÇÃO DE QUADRIL', 'DISPOSITIVOS INTRAMEDULARES', 'SISTEMA DE COLUNA', 'SISTEMA DE COLUNA DE NÍVEL ÚNICO', 'IMPLANTE DENTÁRIO', 'PARAFUSOS ÓSSEOS', 'PARAFUSOS DE COLUNA', 'PRÓTESE TOTAL DE ARTICULAÇÃO DE JOELHO', 'DISPOSITIVOS PARA FIXAÇÃO DA COLUNA VERTEBRAL', 'SISTEMA DE COLUNA OCCÍPITO-CERVICAL E OCCÍPITO-CERVICALTORÁXICO', 'IMPLANTES BIOABSORVÍVEIS', 'FIXADOR EXTERNO', 'RECOBRIMENTO', 'MATERIAIS METÁLICOS', 'METAIS FERROSOS, METAIS NÃO FERROSOS', 'LIGAS METÁLICAS BASE AÇO MÉDIA LIGA', 'LIGAS METÁLICAS BASE ALUMÍNIO', 'LIGAS METÁLICAS BASE COBRE', 'LIGAS METÁLICAS BASE AÇO INOX', 'LIGAS METÁLICAS BASE TITÂNIO', 'BOMBAS ELÉTRICAS DE COMBUSTÍVEIS PARA MOTORES DO CICLO OTTO', 'LÂMPADAS DE FILAMENTO PARA VEÍCULOS AUTOMOTIVOS', 'BUZINAS', 'PEÇAS AUTOMOTIVAS', 'BATERIA CHUMBOÁCIDO PARA USO EM VEÍCULOS RODOVIÁRIOS E AUTOMOTORES', 'BATERIA CHUMBOÁCIDO PARA MOTOCICLETAS TRICICLOS E QUADRICICLOS', 'BOMBAS ELÉTRICAS DE COMBUSTÍVEIS PARA MOTORES DO CICLO OTTO', 'BOMBAS ELÉTRICAS DE COMBUSTÍVEIS PARA MOTORES DO CICLO OTTO', 'BATERIA CHUMBOÁCIDO PARA MOTOCICLETAS TRICICLOS E QUADRICICLOS', 'LÂMPADAS DE FILAMENTO PARA VEÍCULOS AUTOMOTIVOS', 'AMORTECEDORES DA SUSPENSÃO', 'CINTOS DE SEGURANÇA PARA VEÍCULOS RODOVIÁRIOS', 'SEGURANÇA PARA VEÍCULOS DE TRANSPORTE PÚBLICO COLETIVO DE PASSAGEIROS E TRANSPORTE DE PASSAGEIROS TIPOS MICRO-ÔNIBUS E ÔNIBUS, CATEGORIAS M2 e M3', 'TERMINAIS DE DIREÇÃO, BARRAS DE DIREÇÃO, BARRAS DE LIGAÇÃO E TERMINAIS AXIAIS', 'ARRUELA DE ENCOSTO', 'BRONZINAS PLANAS FLANGEADAS', 'BRONZINAS PLANAS', 'BUCHA', 'ANÉIS DE PISTÃO', 'PISTÕES DE LIGA LEVE DE ALUMÍNIO', 'ANÉIS TRAVA', 'PINOS DE PISTÃO', 'CONJUNTO QUADRO E GARFO RÍGIDO DE BICICLETA', 'PEDAL E PEDIVELA DE BICICLETA', 'CORDOALHAS DE BICICLETA', 'AROS DE BICICLETA', 'RAIOS E NIPLES DE BICICLETA', 'CONJUNTO DE DIREÇÃO (GUIDÃO E SUPORTE DE GUIDÃO) DE BICICLETA', 'GARFO DE SUSPENSÃO DE BICICLETA', 'COMPONENTES DE BICICLETAS', 'MATERIAL DE ATRITO PARA FREIO', 'MOLA HELICOIDAL', 'CORRENTE DE TRANSMISSÃO', 'COROA', 'PINHÃO', 'ESCAPAMENTO', 'CORRENTES, COROAS E PINHÃO DE MOTOCICLETAS MOTONETAS, CICLOMOTORES, TRICICLOS E QUADRICICLOS', 'ARRUELA DE ENCOSTO/ BUCHA / BRONZINA DE PAREDE FINA/ PISTÕES DE LIGA LEVE DE ALUMÍNIO', 'TERMINAIS DE DIREÇÃO, BARRAS DE DIREÇÃO, BARRAS DE LIGAÇÃO E TERMINAIS AXIAIS', 'RODA DE LIGA DE ALUMINIO PARA AUTOMÓVEIS COMERCIAIS LEVES E UTILITÁRIOS ESPORTIVOS', 'BUZINAS', 'EQUIPAMENTOS DE AQUECIMENTO SOLAR DE ÁGUA', 'LUMINÁRIAS', 'LÂMPADAS LED COM DISPOSITIVO DE CONTROLE INTEGRADO', 'LÂMPADAS FLUORESCENTES COMPACTAS COM REATOR INTEGRADO À BASE', 'LÂMPADAS LED COM DISPOSITIVO DE CONTROLE INTEGRADO', 'EQUIPAMENTOS ELÉTRICOS DE ILUMINAÇÃO', 'BATERIA ESTACIONÁRIA ALCALINA, NÍQUELCÁDMIO E CHUMBOÁCIDA PARA USO FOTOVOLTAICO', 'INVÓLUCROS DE EQUIPAMENTOS', 'EQUIPAMENTOS DE AQUECIMENTO SOLAR DE ÁGUA – COLETOR SOLAR', 'EQUIPAMENTOS DE AQUECIMENTO SOLAR DE ÁGUA – RESERVATÒRIO TÉRMICO', 'EQUIPAMENTOS DE AQUECIMENTO SOLAR DE ÁGUA – SISTEMA ACOPLADO', 'ÁGUA BRUTA ÁGUA TRATADA ÁGUA PARA CONSUMO HUMANO ÁGUA RESIDUAL', 'ÁGUA BRUTA ÁGUA TRATADA ÁGUA PARA CONSUMO HUMANO ÁGUA RESIDUAL', 'ÁGUA PURIFICADA', 'ÁGUA ENVASADA ÁGUA MINERAL GELO ÁGUA PARA ABASTECIMENTO DA INDÚSTRIA DE ALIMENTOS ÁGUA DE CHILLER', 'ALIMENTOS DE ORIGEM ANIMAL CARNES E PRODUTOS CÁRNEOS', 'ALIMENTOS DE ORIGEM ANIMAL LEITE E DERIVADOS', 'Soro de leite, soro de leite em pó', 'ALIMENTOS DE ORIGEM ANIMAL LEITE E DERIVADOS', 'Leite', 'Margarina, gordura anidra (butter oil)', 'Leite em pó', 'Caseínas e caseinatos', 'Creme de leite e nata', 'Bebida láctea', 'Queijos', 'Manteiga', 'Concentrado Proteico', 'Doce de Leite', 'Leite Condensado', 'Ricota', 'ALIMENTOS DE ORIGEM ANIMAL PESCADOS E PRODUTOS DE PESCA', 'OVOS E DERIVADOS', 'MEL PRODUTOS DA COLMÉIA', 'ALIMENTOS DE ORIGEM ANIMAL PESCADOS E PRODUTOS DE PESCA LEITE E DERIVADOS OVOS E DERIVADOS MEL PRODUTOS DA COLMÉIA', 'ÁGUA ENVASADA ÁGUA MINERAL GELO', 'ALIMENTOS DE ORIGEM ANIMAL CARNES PRODUTOS CÁRNEOS PRODUTOS DA COLMÉIA PESCADOS E PRODUTOS DA PESCA OVOS E DERIVADOS LEITE E PRODUTOS LÁCTEOS ALIMENTOS PARA ANIMAIS', 'ALIMENTOS DE ORIGEM VEGETAL VEGETAIS IN NATURA FARINHAS; FARELOS ESPECIARIAS ÍNTEGRAS E MOÍDAS', 'ÁGUA BRUTA, ÁGUA TRATADA, ÁGUA PARA CONSUMO HUMANO, ÁGUA SALINA, ÁGUA SALOBRA, ÁGUA RESIDUAL', 'ÁGUA TRATADA ÁGUA PARA CONSUMO HUMANO', 'ÁGUA BRUTA', 'ÁGUA SALINA, ÁGUA SALOBRA', 'ÁGUA RESIDUAL']

def getPdfText(pdf):
    """
    This function extracts the PDF text page by page from
    the file placed in the argument.

    Args:
        pdf (str): Path to the PDF document as a string.

    Returns:
        list: A list of string, where each string is the text
        from one page of the PDF.
    """
    pageList = []
    with open(pdf,'rb') as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            page_text = page.extract_text().replace('\n','')
            pageList.append(page_text)
    return pageList

def searchElement(text, listAnalys):
    """_summary_

    Args:
        text (str): text that will be analyzed.
        listAnalys (_type_): _description_

    Returns:
        _type_: _description_
    """
    index = []
   
    results = []
    for element in listAnalys:
        match = []
        start = 0
        while True:
            start = text.find(element, start)
            if start == -1:
                break
            match.append(element)
            match.append(start)
            start += len(element)
            print("O indice do elemento é: ", listAnalys.index(element))
            index.append(match)
            print(index)
    
    indices = sorted(index, key=lambda x: x[1])

    i = 0
    while i < len(indices):
        if i == len(indices) - 1:
            results.append(text[indices[i][1]:])
        else:
            results.append(text[indices[i][1]:indices[i+1][1]])
        i += 1

    return results

texto = ""
lista_de_paginas = getPdfText('escopo.pdf')
for pagina in lista_de_paginas:
    texto += pagina

returns = searchElement(texto, area_atividade)

for result in returns:
    print("AAAAAAAAA")
    print(result)


def makeRow(listAnalys):
    listArea = []
    listClasses = []
    listProducts = []
    
    for page in listAnalys:
        listArea.append(searchElement(page, area_atividade))
    print("listArea finished")
    
    for block in listArea:
        for item in block:
            listClasses.append(searchElement(item, classes))
            
    for block in listClasses:
        for item in block:
            listProducts.append(searchElement(item, produtos))
            
    print("listProducts finisehd")
    print("Testing...")
    for block in listProducts:
        for result in block:
            print(result)

# makeRow(lista_de_paginas)
    
        










