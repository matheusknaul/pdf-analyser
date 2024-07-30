
class Row():
    def __init__(self, area_atividade, classe_ensaio, produto, descricao, normas):
        self.area_atividade = area_atividade
        self.classe_ensaio = classe_ensaio
        self.produto = produto
        self.descricao = descricao
        self.normas = normas
        self.returnRow()


    def returnRow(self):
        return [self.area_atividade, self.classe_ensaio, self.produto, self.descricao, self.normas]