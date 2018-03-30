import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

MaoYanHeaders = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "uuid=1A6E888B4A4B29B16FBA1299108DBE9CDFE0F270F2640051092C5B91D4925C7A; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; __mta=219052582.1507114997794.1507115797315.1507118482776.11; _lxsdk_s=af27c2388b4347ab08f2353fe7c8%7C%7C4",
        "Host": "maoyan.com",
        "Referer": "http://maoyan.com/board/4?offset=90/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    }

def get_one_page(url):
    try:
        response = requests.get(url, headers=MaoYanHeaders)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>'
            +'.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
                'index': item[0],
                'image': item[1],
                'title': item[2],
                'actor': item[3].strip()[3:],
                'time': item[4].strip()[5:],
                'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    pool= Pool()
    pool.map(main, [i*10 for i in range(10)])
