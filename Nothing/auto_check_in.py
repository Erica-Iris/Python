import requests


def check_in(url, cok):
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Cookie": cok
    }
    html = requests.get(url=url, headers=headers).text
    if html.find("本次签到获得") > -1:
        return "已签到"
    elif html.find("您今天已经签到过了") > -1:
        return "已签到"
    else:
        return "出错辽"


site_urls = {
    'PTHome': 'https://pthome.net/attendance.php',
    'HDDisk': 'https://hddisk.life/attendance.php',
    'HDZone': 'https://hdzone.me/attendance.php',
    'LEAGUEHD': 'https://leaguehd.com/attendance.php',
    'HDDolby': 'https://www.hddolby.com/attendance.php',
    'SoulVoice':'https://pt.soulvoice.club/attendance.php',
    'NicePT':'https://www.nicept.net/attendance.php'
}
site_cookies = {
    'PTHome':
    'UM_distinctid=16fef13982d12a-0c8cb97459b747-6701b35-144000-16fef13982e273; c_secure_uid=MTE3NTk5; c_secure_pass=19f732c3611496bcdb518a1c2e421c45; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cfduid=d64abe9a4a742601970a2365d110f32101582916055; CNZZDATA1275677506=1970450426-1580260767-%7C1583346019',
    'HDDisk':
    'c_secure_uid=MTAwNDgx; c_secure_pass=b3785d442b58dcf3d35e524275ed6aef; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cfduid=d2264b728c092acf8c4a20ea9deb8cfd61583077070',
    'HDZone':
    'c_secure_uid=NjE2; c_secure_pass=e4106bfa8118f72ae5f087784ce0d9fc; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cfduid=d07887f2c943cab9e7ebc68b6e7f99c1c1582808088',
    'LEAGUEHD':
    'c_secure_uid=MTE5MDk%3D; c_secure_pass=aefeabd51c049895c350e1f4cce952ea; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cfduid=d342e499c56fd613c9674fc0d634876511582789440',
    'HDDolby':
    '__cfduid=dd644b4d2d7fbf25ce5222b9a542792521582791477; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_uid=MTQ2MjQ%3D; c_secure_pass=07f8a8ca71449b19a1e0f350e4166c75; c_secure_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __51cke__=; __tins__20553957=%7B%22sid%22%3A%201583372685731%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201583374499062%7D; __51laig__=12',
    'SoulVoice':
    'c_secure_uid=OTIwODk%3D; c_secure_pass=46235e8836c12d918018d33b747334ba; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D',
    'NicePT':
    'c_secure_uid=OTg1NDA%3D; c_secure_pass=63c0d2a00385b0423f00aa571fc65b3d; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D; __cfduid=d9999aee15c330261edc4a5b5ab0c1a141582916056'
}

for site_name in site_urls:
    # print(site_urls[site_name],site_cookies[site_name])
    res = check_in(site_urls[site_name], site_cookies[site_name])
    print(site_name, res)
