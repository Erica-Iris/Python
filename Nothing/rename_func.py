import os
import re
path = input("请输入文件路径:")
func_num = int(input("可选用功能:\n1.删除文件内固定字符\n2.添加后缀名\n3.批量改名\n"))
file_name_list = os.listdir(path)
if func_num == 1:
    del_word = input("请输入需要删除的文字: ")
    for file_name in file_name_list:
        refile_name = file_name.split(del_word)[0] + file_name.split(
            del_word)[1]
        os.rename(os.path.join(path, file_name),
                  os.path.join(path, refile_name))
        print(file_name + "     ------------->      " + refile_name)
if func_num == 2:
    add_keyword = input("请输入后缀名: ")
    for file_name in file_name_list:
        refile_name = file_name + "." + add_keyword
        os.rename(os.path.join(path, file_name),
                  os.path.join(path, refile_name))
if func_num ==3:
    for i in file_name_list:
        print(i)
        if i.split('.')[-1] == 'mkv':
            for j in file_name_list:
                if re.split('第|話',j)[1]==i.split(' ')[5]:
                    print("yes")