# pip install selenium
# pip install chromedriver_autoinstaller
from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# 브라우저 드라이서 설치
chromedriver_autoinstaller.install(True)
# 브라우저 오픈
driver = webdriver.Chrome()
driver.implicitly_wait(3) # 브라우저가 켜질때까지 대기.
url ="https://www.msn.com/ko-kr/news/techandscience"
# url 페이지로 이동
driver.get(url)
time.sleep(1) # 1초 멈춤
# find_element <- 단일 엘리먼트 찾기(By.  id,class,tag_name,xpath....
body = driver.find_element(By.TAG_NAME, 'body')
pagedown = 1
cnt = 10
while pagedown < cnt:
    body.send_keys(Keys.PAGE_DOWN) # 스크롤 내리기
    time.sleep(1)
    pagedown +=1

articles = driver.find_elements(By.ID, 'root')

for article in articles:
    title = article.find_element(By.TAG_NAME, 'h3').text
    link = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
    print(f"Title: {title}, Link: {link}")
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())
driver.close() # 브라우저 종료
