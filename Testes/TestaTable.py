from Row import Row
from Table import Table

row1 = Row("Saúde", "Mecânico", "Placa", "Ensaio de placa", "Abnt nbr 7206")
row2 = Row("Saúde", "Químico", "Placa", "Ensaio de placa", "Abnt nbr 124512")
row3 = Row("Saúde", "Meio Ambiente", "Placa", "Ensaio de placa", "Abnt nbr 1212")

table = Table([row1, row2, row3])
table.returnRows()