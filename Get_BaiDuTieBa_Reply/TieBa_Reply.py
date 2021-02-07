
import tkinter as tk
import requests as req
import parsel
import time
import random
import threading
import os


def get_html():
    global cok
    url = 'http://tieba.baidu.com/i/i/replyme'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Cookie": cok
    }
    html = req.get(url=url, headers=headers).text
    return html


def update():
    html = get_html()
    listt = parsel.Selector(html).xpath('//*[@id="feed"]/ul/li')
    list_ = []
    for i in listt:
        reply_user = i.xpath('./div/div/div[1]/a/text()').extract()
        reply_text = i.xpath('./div/div/div[2]/a/text()').extract()
        reply_time = i.xpath('./div[2]/div[1]/text()').extract()
        #去掉多余的冒号
        if reply_user[0][-1] == '：':
            reply_user[0] = reply_user[0][0:-1]
            # print(reply_user[0])
        if len(reply_text) > 0:
            list_.append((reply_time[0] + "    " + reply_user[0] + ": " +
                          reply_text[0]))
        else:
            list_.append(
                (reply_time[0] + "    " + reply_user[0] + ": " + "图片"))
    time.sleep(random.randint(2, 8))

    return list_


def closecl():
    reply.destroy()
    os._exit(0)


reply = tk.Tk()
reply.geometry('500x300')
reply.title('REPLY')
# reply.resizable(0, 0)

cok = 'TIEBA_USERTYPE=5a13ed6608e16318a3da11b1; BAIDUID=6B875CE66AB01D0805EF115388CD2163:FG=1; BIDUPSID=6B875CE66AB01D0805EF115388CD2163; PSTM=1580210449; bdshare_firstime=1580352456080; rpln_guide=1; MCITY=-%3A; BDUSS=DhVTkV6QTN4eEc3WDNsdWtKRjgzazZOY2RsampSSWNVWkNXflZPNHFjcHNkWDVlRVFBQUFBJCQAAAAAAAAAAAEAAADxYR04zuK93DQ2MgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGzoVl5s6FZeZ; STOKEN=f80fbd47f4ed98ecfb1dc280d8b65682feab07de21c8225aa8a9fad9df856980; TIEBAUID=f034d094e0bcbc82edf0a16c; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1583026686,1583106972,1583511710,1583601625; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1583539226,1583592025,1583601622,1583687630; st_key_id=17; LONGID=941449713; 941449713_FRSVideoUploadTip=1; wise_device=0; st_data=8f32cea14721ba09e7be7102c053dbb8bb8baf16c36ba4ecfdf4d3ccd73e5b996b546483514fa3db6ef1ff5c53d0b0a02ca57f3274a1036c26c9cdec9e20260935f7d8585b80043e4e0cb8f81209117bb27102144efd32d1bdc7d44dc2a0eab14ddb0a81f73c6255eb0f98b57dc6ff67e00d0ad1f218f93d8db0ee8dd23e292a; st_sign=386201f7; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1583733585; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; ZD_ENTRY=baidu; BDRCVFR[FhauBQh29_R]=mbxnW11j9Dfmh7GuZR8mvqV; PSINO=7; H_PS_PSSID=30963_1454_21115_30794_30995_30824_26350'
list_old = []

e = tk.Entry(reply, show=None, font=('微软雅黑', 14))
e.place(x=0, y=0, relwidth=0.6)


def get_cookie():
    global cok
    var = e.get()
    cok = var
    # t.insert(tk.INSERT, var)
    # print(type(var))
    # print(cok)


b1 = tk.Button(reply, text='登录', command=get_cookie, font=('更纱黑体 UI SC', 14))
b1.place(relx=0.6, y=0, relwidth=0.2)

b2 = tk.Button(reply, text='退出', command=closecl, font=('更纱黑体 UI SC', 14))
b2.place(relx=0.8, y=0, relwidth=0.2)

# t = tk.Text(reply, height=3)
# t.pack()

l_box = tk.Listbox(reply, width='50', font=('更纱黑体 UI SC', 11))
l_box.place(x=0, y=50, height=250, relwidth=1)


def main():
    list_old = update()

    for item in list_old:
        l_box.insert(tk.END, item)

    while True:
        list_new = update()
        for item in list_new:
            if not (item in list_old):
                l_box.insert(0, item)
                list_old.append(item)


thread = threading.Thread(target=main)
thread.start()
reply.protocol("WM_DELETE_WINDOW", closecl)
reply.mainloop()