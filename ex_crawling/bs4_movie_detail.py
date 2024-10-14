import csv
import requests
import re
from bs4 import BeautifulSoup
# csv 파일 읽기
url = "http://m.cine21.com"
with open("./data/movie.csv" , "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="|")
    data = list(reader)
    for row in data:
        detail_url = url + row[3]
        # print(detail_url)
        res = requests.get(detail_url)
        title = re.sub(r'[^a-zA-Z0-9가-힣\s]','',row[0])
        print(title)
        soup = BeautifulSoup(res.content, 'html.parser')
        # print(soup.prettify())
        lis = soup.select('.review_writer li')
        reviews = []
        for li in lis:
            nm = li.select_one('.name a').text
            rating = li.select_one('.num').text
            review = li.select_one('.review_txt').text
            print(nm, rating, review)
            reviews.append([nm, rating, review])


        with open(f"./data/{title}.csv", 'a', encoding="utf-8", newline='') as f:
            write = csv.writer(f, delimiter="|")
            write.writerows(reviews)

        # 각 영화 이름으로(./data/폴더에) csv파일을 만들고
        # '평론가 이름|평점|관람평' 을 저장하세요
