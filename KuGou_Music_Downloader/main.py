import os
from urllib.request import urlretrieve
from tkinter import *
import requests
import jsonpath
#下载
def music_load(url1,title):
    os.makedirs('下载的音乐',exist_ok=True)
    path = '下载的音乐\{}.mp3'.format(title)
    text.insert(END,'歌曲:{},正在下载。。。'.format(title))
    text.see(END)
    text.update()
    urlretrieve(url1,path)
    text.insert(END,'下载完毕:{},可以去听听'.format(title))
    text.see(END)
    text.update()

# 爬虫
def get_music():
    url = 'http://www.youtap.xin/'
    name = entry1.get()
    platfrom = var.get()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    params = {
                'input': name,
                'filter': 'name',
                'type': platfrom,
                'page': 2
    }
    res = requests.post(url, params, headers=headers)
    html = res.json()
    print(html)
    title = jsonpath.jsonpath(html,'$..title')[0]
    print(title)
    author = jsonpath.jsonpath(html,'$..author')[0]
    print(author)
    url1 = jsonpath.jsonpath(html,'$..url')[0]
    print(url1)
    music_load(url1,title)

# 主界面
root = Tk()
root.geometry('600x600+400+200')
root.title('超级无敌音乐下载器')
label1 = Label(root, text='请在此输入歌名', font=('微软雅黑', 20))
label1.grid()
entry1 = Entry(root, font=('微软雅黑', 20))
entry1.grid(row=0, column=1)
var = StringVar()
r1 = Radiobutton(root, text='QQ', variable=var, value='qq')
r1.grid(row=1, column=0)
r2 = Radiobutton(root, text='kugou', variable=var, value='kugou')
r2.grid(row=1, column=1)

text = Listbox(root, font=('微软雅黑', 16), width=50, height=15)
text.grid(row=2, columnspan=2)

b1 = Button(root, text='开始下载', font=('微软雅黑', 15),command=get_music)
b1.grid(row=3, column=0)
b2 = Button(root, text='退出程序', font=('微软雅黑', 15), command=root.quit)
b2.grid(row=3, column=1)

root.mainloop()