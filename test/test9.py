# from openpyxl import load_workbook
import csv
import os, sys
import json

# files="F:\\wnacg\\record.xlsx"
fil = 'f:\\wnacg\\record.csv'
filee = 'f:\\wnacg\\record.json'

# wb=load_workbook(filename=files)
# sheet_range=wb['record']
# print(sheet_range['A1'].value)
# ws=wb['record']
# ws['A1']='1111'
# wb.save(files)

# def write_excel(x,y,val):
#     wb=load_workbook(filename=files)
#     sit=x+y
#     ws=wb['record']
#     ws[sit]=val
#     wb.save(files)


def write_json(num, size, state, name):
    with open(filee, 'wb') as f:
        data = json.loads(f,encoding='utf-8')
        data[num]['size'] = size
        data[num]['state'] = state
        data[num]['name'] = name


with open(fil, 'r', newline='', encoding='utf-8') as f:
    rea = csv.reader(f)
    for row in rea:
        # write_excel('A',str(int(row[0])+1),row[0])
        # write_excel('B',str(int(row[0])+1),row[1])
        # write_excel('C',str(int(row[0])+1),row[2])
        # write_excel('D',str(int(row[0])+1),row[3])
        write_json(row[0], row[1], row[2], row[3])

# txt_e = """
# {
#   "header":{
#     "funcNo": "IF010002",
#     "opStation": "11.11.1.1",
#     "appId": "aaaaaa",
#     "deviceId": "kk",
#     "ver":"wx-1.0",
#     "channel": "4"
#   },
#   "payload": {
#     "mobileTel": "13817120001"
#   }
# }
# """

# json_data=json.loads(txt_e)

# json_data['header']['funcNo']="assssss"

# print(json_data)