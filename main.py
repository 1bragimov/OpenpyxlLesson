import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['A1'] = "Name"
sheet['B1'] = "Address"
sheet['C1'] = "Phone"


sheet['A2'] = "Bunyod"
sheet['A3'] = "Behruz"


sheet['B2'] = "Tashkent"
sheet['B3'] = "UZB"


sheet['C2'] = "90-550-23-24"
sheet['C3'] = "88-767-23-24"
