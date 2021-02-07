# import xlrd

# from datetime import date,datetime

# ex_file="E:\\a.xlsx"

# def read_excel():
#     wb=xlrd.open_workbook(filename=ex_file)
#     # print(wb.sheet_names())
#     sheet1=wb.sheet_by_index(0)
#     # print(sheet1)
#     # print(sheet1.name)
#     # rows=sheet1.row_values(2)
#     col_ti=sheet1.col_values(2)
#     col_an=sheet1.col_values(7)

#     # print(rows)
#     # print(col_ti)
#     # print(col_an)
#     # print(sheet1.cell(1,0).value)
#     # print(sheet1.cell_value(1,0))
#     # print(sheet1.row(1)[0].value)
#     print(col_ti[3])

# read_excel()
# /html/body/div[2]/div[2]/div/table/tbody/tr[1]/th/font/text()

from bs4 import BeautifulSoup

import lxml
# import parsel

# with open("E:\\a.html", encoding='utf-8') as f:
    # print(f.read())
    # soup=BeautifulSoup(f.read(),'html.parser')
    # print(type(f.read()))#type:str

    # print(soup.prettify())格式化

    # for bo in soup.body.children:
    #     print(bo)
    # data = parsel.Selector(f.read())
    # ti_mu_list = data.xpath("/html/body/div[2]/div[2]/div/table/tbody/tr/th/font/text()")
    # print(ti_mu_list)
    
soup = BeautifulSoup(open("E:\\a.html",encoding='utf-8'),'lxml')

# print(soup.prettify())
timulist=[]
timulist=soup.find("table").find_all("font")
for i in timulist:
    p=i.string.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    print(p)


