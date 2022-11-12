import xlrd

pj = xlrd.open_workbook_xls('文件/工作簿1.xlsx')
sheet_number = pj.nsheets()
print(sheet_number)