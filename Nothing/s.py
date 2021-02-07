import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.1dy.com/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#wp > div.deanwp > div:nth-child(1) > ul > li:nth-child(1) > div.deanmovieimg > a > img')
# print(data)
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('src')
        # 'ID':re.findall('\d+',item.get('href'))
    }
print(result)