import urllib.request
import wget
from bs4 import BeautifulSoup

url = "http://www.digitalforensics.or.kr"
req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url+"/images").read()
soup = BeautifulSoup(sourcecode, "html.parser")

href = soup.select('pre > a')

down = []
for i in href:
    image = i.get('href')
    urlimage = url+str(image)
    print(image)
    down.append(urlimage)

for j in down:
    wget.download(j, out='.')
    print("save")
