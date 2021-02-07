import requests
import time
import random


def get_json(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    #params   不知道什么鬼的参数 控制面板里看到的
    params = {
        'page_size': 10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }

    try:
        html = requests.get(url, headers=headers, params=params)
        return html.json()
    except BaseException:
        print('Requests Error!!!')
        pass


def downloaders(url, path):
    start_time = time.time()
    size = 0
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers, stream=True)
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    if response.status_code == 200:
        print('[文件大小]:%0.2f MB' % (content_size / chunk_size / 1024))
        with open(path, 'wb') as f:
            for date in response.iter_content(chunk_size=chunk_size):
                f.write(date)
                size += len(date)
                print('\r' + '[进度]:%s%.2f%%' %
                      ('>' * int(size * 50 / content_size),
                       float(size / content_size * 100)),
                      end=" ")

    end_time = time.time()
    print('\n' + 'Done time:  %.2f sec' % (end_time - start_time))


if __name__ == '__main__':

    for i in range(10):
        url = 'https://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url)
        infos = html['data']['items']
        for info in infos:
            title = info['item']['description']
            video_url = info['item']['video_playurl']
            print(title)
            try:
                downloaders(video_url, path='%s.mp4' % title)
                print("成功了一个")

            except BaseException:
                print('fail')
                pass
        time.sleep(int(format(random.randint(2, 8))))
