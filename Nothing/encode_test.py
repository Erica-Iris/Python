import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

res = requests.get('https://www.23wx.cc/du/7/7464/8987566.html',
                    headers=headers)
res.encoding='gbk'
html=res.text
print(html)
