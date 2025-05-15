import openpyxl

workbook = openpyxl.load_workbook('Instrumentos 2019-2024_19_11.xlsx')
worksheet = workbook['Empenhos']
worksheet.cell(row=1, column=6, value='Links')

for row in range(2, worksheet.max_row + 1):
    formula = worksheet.cell(row=row, column=3).value

    if formula and formula.startswith('=HYPERLINK('):
        link = formula.split('"')[1]
    else:
        link = None
    worksheet.cell(row=row, column=6, value=link)

workbook.save('empenhos_updated.xlsx')
print("Links have been extracted and saved to a new column in 'empenhos_updated.xlsx'.")
