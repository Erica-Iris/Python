import requests,time,random
from bs4 import BeautifulSoup
import re

cookie = 'PHPSESSID=grm6lq4vegb2n8gk1v2o1ohjf1; c_secure_uid=NDgx; c_secure_pass=e4fa3ffa0248da38f68637e4bdad6e27; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cookie': cookie}
url = 'https://ptsbao.club/'
wbdata = requests.get(url,headers=header).text
r=BeautifulSoup(wbdata,'html.parser')
# with open('sss.txt','w',encoding='utf-8') as f:
#     f.write(wbdata)
#     f.close()
# print(r.prettify())
r.find_all(re.compile(</font>(.*?)<font class='color_uploaded'>))
print(r)