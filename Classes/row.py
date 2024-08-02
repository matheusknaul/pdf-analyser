
class Row():
    def __init__(self, area_atividade, produto, descricao):
        self.area_atividade = area_atividade
        self.produto = produto
        self.descricao = descricao
        self.returnRow()


    def returnRow(self):
        return [self.area_atividade, self.produto, self.descricao]