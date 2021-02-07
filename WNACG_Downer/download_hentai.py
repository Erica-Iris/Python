import requests
import re
import time
import random
import os
import csv

csv_list=[]

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

path_header = 'E:\\WNACG\\'

def write_csv_file(lists):
    with open('E:\\WNACG\\record.csv', 'a', newline='', encoding='utf-8') as f:
        wrt = csv.writer(f)
        wrt.writerow(lists)

def print_progress(progress):
    print('\r' + '[下载进度]: [%s%s]%.2f%%' % ('█' * int(progress*28), ' ' * (28 - int(progress*28)), float(progress * 100)),end=" ")


#下载器  需要 下载地址,文件名,编号,存储位置范围
def downloaders(url, name, num, code):
    size = 0
    start_time = time.time()

    print("[文件名称]: " + name)
    #path 文件存储地址,方便使用
    file_path = path_header + code + "\\" + num + ". " + name

    response = requests.get(url=url, headers=headers, stream=True)
    #content_size 获取文件大小
    content_size = int(response.headers['content-length'])
    #文件存在且大小对的上,单位是 B
    if os.path.exists(file_path) and os.path.getsize(file_path) == content_size:
        print(" 已存在,跳过下载")
        return num, content_size, "已下载", name
    #不存在或者没下载完全
    else:
        if response.status_code == 200:
            print("[文件状态]: 正常")
            print('[文件大小]: %0.2f MB' % (content_size / 1024 / 1024))

            print("[保存位置]: " + file_path)
            #按区块大小写入文件,并打印进度
            with open(file_path, 'wb') as f:
                for data in response.iter_content(chunk_size=1024):
                    f.write(data)
                    size += len(data)
                    print_progress(size/content_size)

            end_time = time.time()
        #文件不存在 会出现  .zip  且大小为 0B
        else:
            print("[文件状态]: 文件不存在!")
            return num, 0, "文件不存在", name
        #打印一些下载信息
        print('\n' + '[下载用时]: %.2f 秒' % (end_time - start_time))
        if (content_size / 1024 / 1024 / (end_time - start_time)) >= 1:
            print("[平均速度:] %.2fMb/s" % ((content_size / 1024) / 1024 / (end_time - start_time)))
            return num, content_size, "已下载", name
        else:
            print("[平均速度:] %.2fkb/s" % (content_size / 1024 / (end_time - start_time)))
            return num, content_size, "已下载", name
def aaa():
    for f_num in range(500,1001):
        #code_num 计算 f_num在哪个文件夹范围内
        code_num = (str(int((f_num - 1) / 100) * 100 + 1) + '-' + str(int((f_num - 1) / 100 + 1) * 100))
        #判断这个文件夹是否存在,若不存在则新建
        if not os.path.exists(path_header+str(code_num)):
            os.mkdir(path_header + str(code_num))
        else:
            pass

        url = 'https://wnacg.com/download-index-aid-%.0f.html' % f_num
        print("-----------------正在下载第%.0f号文件-----------------" % f_num)
        time.sleep(int(format(random.randint(2, 8))))

        try:
            #获取下载文件名,下载地址  并把文件名,地址,编号,文件范围 传入下载器
            response = requests.get(url=url, headers=headers, stream=True)
            d_url = re.search(r'<a class="down_btn" href="(.*?)" target="_blank"><span>&nbsp;本地下載一</span></a>',response.text).group(1)
            f_name = re.search(r'<p class="download_filename">(.*?)</p>',response.text).group(1)
            csv_list=downloaders(d_url, f_name, str(f_num), code_num)
            write_csv_file(csv_list)
        except BaseException:
            print('失败')
            csv_list=[f_num, 0, "失败", f_name]
            write_csv_file(csv_list)
            pass

if __name__ == '__main__':
    aaa()