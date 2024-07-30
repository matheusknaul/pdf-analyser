from Row import Row

class Table():

    def __init__(self, rows):
        self.rows = rows

    def returnRows(self):
        for row in self.rows:
            print(row.returnRow())