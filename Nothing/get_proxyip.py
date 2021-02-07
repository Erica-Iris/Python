import requests
from bs4 import BeautifulSoup
from redis import StrictRedis
store=StrictRedis(host='localhost',port=6379,db=0)
default=5
ipadd=[]
def get_ip():
    url='https://lab.crossincode.com/proxy/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0', }
    r=requests.get(url=url,headers=header)
    soup=BeautifulSoup(r.text,'lxml')
    infos=soup.find_all('td')
    # count=0
    # print(r.text)
    for i in infos:
        ipadd.append(i)
    for j in range(1,len(ipadd)+1):
        # print(j)
        if j % 6 == 1:
            ip = ipadd[j-1]
            port = ipadd[j]
            # count = count + 1
            store.zadd('xici_ip', {ip+':'+port: default})
    # print(count)
    #     print(i)
    # print(type(infos))
    # body > div > div > div.col-md-10.col-xs-12 > div.center-block.root-index-block > table > tbody > tr:nth-child(2) > td:nth-child(1)
    # print(len(ipadd))
    # print()


def check_ip():
    TEST_URL='http://www.baidu.com'
    store.zremrangebyscore ('xici_ip',0,0)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    for proxy in store.zrangebyscore('xici_ip', 1, 9):
        proxy = proxy.decode('utf-8')
        print(proxy)
        proxys = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        print('testing' + '...No.' )

        try:####异常就都捕获了。
            r = requests.get(url=TEST_URL, headers=header, proxies=proxys, timeout=1.0)
            if r.status_code == 200:
                store.zincrby('xici_ip', 1, proxy)
                print('第' + '个:  ' + '成功')
        except:
            store.zincrby('xici_ip', -1, proxy)
            print('第' + '个:  ' + '失败')

if __name__ == '__main__':
    get_ip()
    check_ip()