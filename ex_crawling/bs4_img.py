import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os
# image download
# req.urlretrieve('https://image.cine21.com/resize/cine21/poster/2019/0129/14_35_36__5c4fe6280c438[F230,329].jpg'
#                 ,'test.jpg')
image_path = "./img"
if not os.path.exists(image_path):
    os.mkdir(image_path)
url = "http://m.cine21.com/movie/boxoffice/history"
res = requests.get(url)
soup = BeautifulSoup(res.content,"html.parser")
div = soup.select_one('.lst_ranking_area')
imgs = div.find_all('img')
for i, img in enumerate(imgs):
    print(i, img['src'])
    req.urlretrieve(img['src'], os.path.join(image_path, str(i)+".jpg" ))

