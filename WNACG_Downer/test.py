import requests
import parsel

key_word=input('输入搜索关键词: ')
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url='https://wnacg.com/albums-index-page-1-sname-%s.html' % key_word
html=requests.get(url=url,headers=headers).text
page_num_list=parsel.Selector(html).xpath('//*[@id="bodywrap"]/div[2]/div[2]/div')
for i in page_num_list:
    try:
        print(i.xpath('./a/text()').extract()[-1])
    except:
        print('1')

# print(html)