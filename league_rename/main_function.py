import os


def change_names(o_name):
    
    # 从文件名中提取出BXXXXXXXX某某某
    c_name="B"
    p=0
    for i in o_name:
        if i<="9" and i>="0":
            c_name=c_name+i
            p=p+1
        if p == 8:
            break
    p=0
    c_name=c_name+" "
    for i in o_name:
        if '\u4e00' <= i <= '\u9fa5':
            c_name=c_name+i
            p=p+1
    
    if p==2:
        c_name=c_name[0:11]+"   "+c_name[-1]
    return c_name

def change_coding(name_):
    pass

def change_name_list(name_list):
    for name in name_list:
        pass

def get_new_dir_name(o_name):
    o_name=o_name[0:7]
    return o_name

if __name__ == "__main__":
    path = input("输入文件夹位置:")
    path=path.replace('\\',r'\\')

    # files= os.listdir(path)
    # for file in files:
    #     if not os.path.isdir(file):
    #         # print(change_names(file))
    #         os.rename(path+"\\"+file,path+"\\"+change_names(file)+".jpg")    
    
    for dirs in os.listdir(path):
        for files in os.listdir(path+"\\"+dirs):
            if not os.path.isdir(files):
                os.rename(path+"\\"+dirs+"\\"+files,path+"\\"+dirs+change_names(files)+".jpg")
        os.rename(os.path.join(path,dirs),os.path)
        
    for i in range(1,100):
        print(whatfuck)
        
        
    if sadafadfafd:
        pass
    else:
        pass