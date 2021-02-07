# import csv

# # 使用数字和字符串的数字都可以
# datas = [['num', 'name','size','state'],
#          [1, 'a',123234,'Done'],
#          [2, 'b',234324,'Done'],
#          [3, 'c',123241,'Done']]

# with open('example.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     for row in datas:
#         writer.writerow(row)
        
    # 还可以写入多行
    # writer.writerows(datas)
import os

list=[]
for i in range(1,10000):
    if not (str(int(i/100)*100+1)+'-'+str(int(i/100+1)*100)) in list:
        list.append((str(int(i/100)*100+1)+'-'+str(int(i/100+1)*100)))
    else:
        pass
    
    if  os.path.exists("E:\\"+(str(int(i/100)*100+1)+'-'+str(int(i/100+1)*100))):
        os.rmdir("E:\\"+(str(int(i/100)*100+1)+'-'+str(int(i/100+1)*100)))
    else:
        pass
    

print(list)