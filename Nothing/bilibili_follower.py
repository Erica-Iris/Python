import requests
import re
import time

a = 'https://api.bilibili.com/x/relation/stat?vmid='

list = {'敬汉卿': '9824766', '老番茄': '546195', 'L e x ': '777536'}

list2 = {'敬汉卿': 0, '老番茄': 0, 'L e x ': 0}

while True:
    for i in list:
        url = a + list[i]

        html = requests.get(url).text

        followers = re.search(r'follower":(.*?)}', html)

        print(i + "的粉丝数: " + followers.group(1)+"    增加了:"+str(int(followers.group(1))-list2[i]))

        list2[i]=int(followers.group(1))

    time.sleep(10)

    print("---------------分割线--------------")

# print(html)