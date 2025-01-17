import requests
from bs4 import BeautifulSoup

# 伪装成浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

for start_num in range(0, 250, 25):
    response = requests.get(
        f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # 根据属性筛选
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        # 筛选出电影中文名
        if "/" not in title_string:
            print(title_string)
