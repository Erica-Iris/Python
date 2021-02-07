# import requests

# for i in range(1,100):
#     num=str(i)
#     for p in range(1,4-len(num)):
#         num='0'+num
#     print('https://images.dmzj.com/c/cross-days/CH01/{}.jpg'.format(num))

import requests
from bs4 import BeautifulSoup
url='https://manhua.dmzj.com/crossdays/11053.shtml#@page=30'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0', }
r=requests.get(url=url,headers=header)
print(r.text)
soup = BeautifulSoup(r.text,'lxml')
img = soup.select('#center_box > img')
for i in img:
    imgurl = i.get('src')