import requests
import re
import datetime
import time

def gethtml():
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Cookie":"c_secure_uid=OTIwODk%3D; c_secure_pass=46235e8836c12d918018d33b747334ba; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D"
        }
    html = requests.get("https://pt.soulvoice.club/attendance.php", headers=headers).text
    if html.find("本次签到获得") > -1:
        return True
    elif html.find("您今天已经签到过了") > -1:
        return True
    else:
        return False

def mian():
    while True:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        if date in datetable:
            print("wait1")
            time.sleep(3600)
        elif gethtml() == True:
            print("add1")
            datetable.append(date)
        else:
            print("wait2")
            time.sleep(3600)

if __name__ == "__main__":
    datetable = []
    mian()