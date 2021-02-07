import re, datetime, os
def adjust_srt(x, f_name, y = r'd:/output/',z = 0):
    """
    调整视频字幕时间，+z字幕延后z秒显示，输出新文件
    x：原字幕文件路径
    y：输出调整后文件路径+文件名
    z:调整时间（s）
    注：函数仅适用于整体调整，字幕随时间阶段偏移的情况比较复杂，
    相对也比较少见，在此就不追加分段调整功能了，感兴趣的可以自己完善~
    """

    f0 = open(r'' + x, 'r',encoding='utf-8')
    pat = r"\d\d:\d\d:\d\d" # 正则表达式
    f1 = f0.read()
    l0 = re.findall(pat, f1) # 正则过滤所有字幕显示时间，输出是一个列表
 
    temp = []
    for i in l0:
        h = int(i[0: 2])
        m = int(i[3: 5])
        s = int(i[6:])
        delta = datetime.timedelta(seconds = z) # 调整时间
        t = datetime.datetime(2018, 7, 20, h, m, s) + delta # 加入年月日格式化调整后的字幕时间
        t1 = datetime.datetime.strftime(t, '%H:%M:%S') # 去掉年月日
        temp.append(t1) # 得到调整后的时间列表
 
    result = []
    for i in range(len(temp)):
        f1 = f1.replace(l0[i], temp[i]) # 替换字幕时间
 
    if os.path.exists(y[0:10]): # 判断输出路径是否存在
        pass
        print( "it's already exists")
    else:
        print( 'make dir')
        os.mkdir(y[0:10]) # 不存在则新建目录
    new = open(y+f_name, 'w',encoding='utf-8')
    new.write(f1) # 将调整后文件写入
    f0.close()
    new.close()
 
# path = r'E:/IDM Download/Devilman_ Crybaby Chinese/[DragsterPS] Devilman Crybaby S01E01 [720p] [Multi-Audio] [Multi-Subs] [A0006120]_Track40.txt'

for i in os.listdir(r'E:/IDM Download/Devilman_ Crybaby Chinese/'):
    path=r'E:/IDM Download/Devilman_ Crybaby Chinese/'+i
    adjust_srt(path, i,z = 10)
