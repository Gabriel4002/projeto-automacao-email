from openpyxl import load_workbook, Workbook
#Comando que cria uma pasta de trabalho
wb = Workbook()
ws = wb.active
#Comando que define o nome da planilha ativa
ws.title = 'exemplo'
#Comando que insere valor nas colunas da planilha ativa em ordem. Repetir o comando dessa forma fara com que seja adicionado nas linhas abaixo
ws.append(['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1'])
ws.append(['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2'])
wb.save('planilha/teste.xlsx')