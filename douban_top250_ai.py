import requests
from bs4 import BeautifulSoup
import csv
import time


def scrape_douban_top250():
    base_url = "https://movie.douban.com/top250"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Referer": "https://movie.douban.com/",
        "Cookie": "your_cookie_here"  # 将复制的 Cookie 放在这里
    }
    time.sleep(3)  # 每次请求暂停 3 秒

    movies = []

    for start in range(0, 250, 25):
        url = f"{base_url}?start={start}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        movie_items = soup.find_all('div', class_='item')

        for item in movie_items:
            movie = {}

            title = item.find('span', class_='title')
            if title:
                movie['电影名'] = title.get_text(strip=True)

            rating = item.find('span', class_='rating_num')
            if rating:
                movie['评分'] = rating.get_text(strip=True)

            movies.append(movie)

    with open('douban_top250.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['电影名', '评分'])
        writer.writeheader()
        writer.writerows(movies)


if __name__ == "__main__":
    scrape_douban_top250()
