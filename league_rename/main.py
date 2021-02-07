import zipfile
import main_function
import os

# files=zipfile.ZipFile("E:\\B190403团支部第十季青年大学习截图.zip")
# zip_list=files.namelist()
# for zip_file in zip_list:
#     # print(zip_file)
#     # print(zip_file.encode('utf-8'))
#     try:
#         zip_file = zip_file.encode('cp437').decode('gbk')
#     except:
#         zip_file = zip_file.encode('utf-8').decode('utf-8')
#     # print(zip_file)
#     print(main_function.change_names(zip_file))


if __name__ == "__main__":
    o_path = input("请输入文件位置(或者文件夹位置):")
    if os.path.isdir(o_path):
        # 对文件夹处理
        for file_name in os.listdir(o_path):
            # print(file_name)
            # 列出每一个zip文件
            files=zipfile.ZipFile(o_path+'\\'+file_name)
            # 每个zip文件里的照片文件
            zip_file_list=files.namelist()
            for zip_file in zip_file_list:
                # 对照片文件重新编码,解决中文乱码问题
                # print(zip_file.encode('utf-8'))
                try:
                    zip_file = zip_file.encode('cp437').decode('gbk')
                except:
                    zip_file = zip_file.encode('utf-8').decode('utf-8')
                print(main_function.change_names(zip_file))
    elif os.path.isfile(o_path):
        # 对压缩文件的处理
        print( "it's a normal file")
    else:
        # 遇到特殊文件时候的处理
        print( "it's a special file(socket,FIFO,device file)")