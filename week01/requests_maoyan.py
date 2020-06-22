# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-06-22   20:03
# 文件名称    : requests_maoyan  PY
# 开发工具    : PyCharm


import requests
from bs4 import BeautifulSoup as bs
import pandas
import lxml.etree

url = "https://maoyan.com/films?showType=3"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"}
film = []
#def obtain_movie(url, num):
res = requests.get(url, headers=header)
print(f"网络返回码为：{res.status_code}")
#print(f'{res.text}')
soup = bs(res.text, features="html.parser")
for args in soup.find_all('div',attrs={'class':'movie-item-hover'},limit=10):
    for subargs in args.find_all('a'):
        href = subargs.get('href')
       # href_1 = href[7:22]
        res_1 = requests.get('https://maoyan.com'+href, headers=header)
        selector = lxml.etree.HTML(res_1.text)
        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        print(f'{film_name}')
        film_tag1 = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
        film_tag2 = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[2]/text()')
        film_tag3 = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[3]/text()')
        film_tag = []
        film_tag.append(f'{film_tag1}/{film_tag2}/{film_tag3}')
        print(f'{film_tag}')
        film_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        print(f'{film_time}')
        film.append([film_name, film_tag, film_time])
movie = pandas.DataFrame(data=film)
movie.to_csv('./movie_1.csv', encoding='utf8', index=False, header=False)



