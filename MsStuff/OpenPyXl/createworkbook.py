from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

workbook.save(filename="registry.xlsx")