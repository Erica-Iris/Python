import requests
from bs4 import BeautifulStoneSoup
import parsel

url = "https://www.beitai.pt/torrents.php"

cookies = {
    'cookie':
    'c_secure_ssl=bm9wZQ%3D%3D; c_secure_uid=MTUxNw%3D%3D; c_secure_pass=f3145823d234db509ed7d5ef5c0dee2a; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D'
}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
r = requests.get(url, cookies=cookies, headers=headers).text

list = parsel.Selector(r).xpath('//table[@class="torrents_tbody"]/tbody')
print(list)
# print(r)