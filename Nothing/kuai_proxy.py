import requests
import parsel


def get_html():
    #step one
    base_url = 'https://www.kuaidaili.com/free/'
    head = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    #step two
    data = requests.get(url=base_url, headers=head).text()
    return data


def parse_data(data):
    html_data = parsel.Selector(data)
    parse_list = html_data.xpath(
        '//table[@class="table table-boredered table-striped"]/tbody/tr')
    return parse_list


def check_ip(data):
    


if __name__ == '__main__':
    pro_list = []
    data = get_html()
    pro_list = parse_data(data)
    for tr in pro_list:
        pro_dict = {}
        typee = tr.xpath('./td[3]/text()').extract_first()
        ip = tr.xpath('./td[0]/text()').extract_first()
        port = tr.xpath('./td[1]/text()').extract_first()
        pro_dict[typee] = ip + ":" + port
        pro_list.append(pro_dict)
