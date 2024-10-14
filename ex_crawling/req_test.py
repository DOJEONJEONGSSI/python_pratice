import requests
from bs4 import BeautifulSoup
url ="https://www.msn.com/ko-kr/news/techandscience"
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())