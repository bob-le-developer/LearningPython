import requests
from bs4 import BeautifulSoup

header={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

url='https://baijiahao.baidu.com/s?id=1611316124457325132&wfr=spider&for=pc'

req=requests.get(url=url,headers=headers)

req.encodings='utf-8'
html=BeautifulSoup(req.text,'html.parser')

imgs=html.select('.index-module_articleWrap_27phx img')
print(imgs)
for i in imgs:
    url=i.get('src')
    img=requests.get(url=url).content
    print(img)
    with open('电影\\'+str(img.index(i))+'.jpg','wb') as f:
        f.write(img)
