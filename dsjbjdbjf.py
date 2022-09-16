import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
url='https://baike.sogou.com/city/map.v'

req=requests.get(url=url,headers=headers)
req.encoding='utf-8'

html=BeautifulSoup(req.text, 'html.parser')
print(html)
ass=html.select('.yb_city_left h3 a')
print(ass)
hrefList=[]
for a in ass:
    url='https://baike.sogou.com'+a.get('href')
    hrefList.append(url)

for url in hrefList:
    print('start extraction',url)

    req=requests.get(url=url,headers=headers)
    req.encoding='utf-8'
    html=BeautifulSoup(req.text, 'html.parser')

    title=html.select('h1')[0].get_text()
    com_title=html.select('.lemma-intr.tltle')[0].find(text)
    com_com=html.select('.lemma intro.content')[0].get_text()

    with open('ecruteak.txt','a',encoding='utf-8')as f:
        f.write(title+'\n')
        f.write(com_title+'\n')
        f.write(com_com+'\n\n')
