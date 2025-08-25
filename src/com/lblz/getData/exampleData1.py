import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

movies = []
for item in soup.find_all('div', class_='item'):
    title = item.find('span', class_='title').text
    rating = item.find('span', class_='rating_num').text
    quote = item.find('span', class_='inq').text if item.find('span', class_='inq') else ""

    movies.append({
        '排名': len(movies) + 1,
        '片名': title,
        '评分': rating,
        '短评': quote
    })
for item in movies:
    print(item)
print(f"抓取到{len(movies)}部电影！")
