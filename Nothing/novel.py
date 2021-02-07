import requests
import parsel
import time
import random
import os
import chardet

def get_html(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers)
    res.encoding='gbk'
    html=res.text
    # chardet.detect(res)
    return html



def get_catalog():
    resourse = {}
    url = 'https://www.23wx.cc/du/7/7464/'
    html = get_html(url)
    dd_list = parsel.Selector(html).xpath('//*[@id="list"]/dl/dd')

    for i in dd_list:
        title = i.xpath('./a/text()').extract()[0]
        href = 'https://www.23wx.cc/du/7/7464/' + i.xpath('./a/@href').extract()[0]
        resourse[title] = href
        # print(title[0],href[0])

    return resourse



def main():
    catalog = get_catalog()

    for j in catalog:
        url = catalog[j]
        path = 'E:\\qindi\\' + j + '.txt'
        print('[正在下载]: '+ j)
        if not(os.path.exists(path)):
            try:
                text = parsel.Selector(get_html(url)).xpath('//*[@id="content"]/text()').extract()

                with open(path,'w',encoding='utf-8')as f:
                    for i in text:
                        f.write(i + '\n')
                print('下载完成')
            except:
                print('下载失败')
            time.sleep(random.randint(1,2))
        else:
            print("已下载,跳过")
        
            

main()
        
