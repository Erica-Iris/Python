import requests
import parsel
import re

url='https://wnacg.com/albums-index-page-1-sname-aaa.html'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

html=requests.get(url=url,headers=headers).text
# print(html)
book_name_list=parsel.Selector(html).xpath('//*[@id="bodywrap"]/div[2]/div[1]/ul/li/div[2]/div[1]')
for i in book_name_list:
    file_name_url = i.xpath('./a/@href').extract()[0]
    print(file_name_url)
    file_name = i.xpath('./a/text()').extract()[0]
    print(file_name)
    file_name_url=re.search(r'aid-(.*?).html',file_name_url).group(1)
    print(file_name_url)