import requests
from bs4 import BeautifulSoup
from redis import StrictRedis
store=StrictRedis(host='localhost',port=6379,db=0)
default=5
ipadd=[]

def get_ip():####从西刺ip代理爬取免费的代理ip。
    url='https://lab.crossincode.com/proxy/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0', }
    r=requests.get(url=url,headers=header)
    soup=BeautifulSoup(r.text,'lxml')
    infos=soup.find_all('td')
    count=0
    for info in infos:
        ipadd.append(info)
    for j in range(1,len(ipadd)+1):
        # print(j)
        if j % 6 == 1:
            ip = ipadd[j-1]
            port = ipadd[j]
            # count = count + 1
            store.zadd('xici_ip', {ip+':'+port: default})
    print(count)

def check_ip():
    TEST_URL='https://www.baidu.com'
    store.zremrangebyscore ('xici_ip',0,0)
    count2=0

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0', }

    for proxy in store.zrangebyscore('xici_ip', 1, 9):####只检测分数在1-9之间的，其它的没管
        count2+=1
        proxy = proxy.decode('utf-8')
        # proxy='http://'+proxys
        # proxys = '139.224.147.40:8080'
        print(proxy)
        proxys = {'http': 'http://' + proxy,
                  'https': 'https://' + proxy
                  }
        print('testing' + ' ...第' + str(count2) + '个 ')
        try:####异常就都捕获了。
            r = requests.get(url=TEST_URL, headers=header, proxies=proxys, timeout=1.0)
            if r.status_code == 200:
                store.zincrby('xici_ip', 1, proxy)
                print('第' + str(count2) + '个:  ' + '成功')
        except:
            store.zincrby('xici_ip', -1, proxy)
            print('第' + str(count2) + '个:  ' + '失败')
if __name__ == '__main__':
	get_ip()
	check_ip()
