import requests
import parsel
from bs4 import BeautifulSoup

url = 'https://pt.m-team.cc/'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'cookie':
    'tp=ODE1NDlhMTNiNDI0ZGY2ZjViMjFhN2RjM2U3YWY0MGU4ZDBhOTc4MQ%3D%3D; __cfduid=dbefe3a3ccddd2f9893665498bee546d01583519148'
}
html = requests.get(url=url, headers=headers).text
# print(html)
soup=BeautifulSoup(html)
with open('a.txt','w',encoding='utf-8')as f:
    f.write(html)
a = parsel.Selector(html).xpath(
    '//*[@id="outer"]/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody'
)

for i in a:
    p=i.xpath('./td[1]/text()').extract()[0]
    print(p)