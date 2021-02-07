from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time


brower = webdriver.Chrome(executable_path='E:\product\python\chromedriver.exe')

brower.get('https://ptsbao.club/')
# brower.maximize_window()
# brower.find_element_by_name('username').send_keys('PTSBAO')
# brower.find_element_by_name('password').send_keys('qazwsx123456?')

# time.sleep(10)
# brower.find_element_by_xpath('//*[@id="nav_block"]/form[2]/table/tbody/tr[10]/td/input[1]').click()
# dictcookie=brower.get_cookies()
# jsoncookie=json.dumps(dictcookie)
# with open('cookies.json','w') as f:
#     f.write(jsoncookie)
brower.delete_all_cookies()
with open(r'E:\product\python\2048_AI\cookie.json','r',encoding='utf-8') as f:
    listcookies=json.loads(f.read())
for co in listcookies:
    brower.add_cookie({
        'domain':'.ptsbao.club',
        'name':co['name'],
        'value':co['value'],
        'path':'/',
        'expires':None
    })
brower.refresh()