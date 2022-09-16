import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
url='https://zh.wikihow.com/%E9%A6%96%E9%A1%B5'

req=requests.get(url=url,headers=headers)
req.encoding='utf-8'

html=BeautifulSoup(req.text, 'html.parser')

ass=html.select('.hp_categories_list')

hrefList=[]

for a in ass:
    url='https://zh.wikihow.com'+a.get('href')
    hrefList.append(url)

for url in hrefList:
    print('loading',url)

    req=requests.get(url=url,headers=headers)
    req.encoding='utf-8'
    html=BeautifulSoup(req.text,'html.parser')

    title=html.select('h1')[0].get_text()
    content=html.select('.abstrat_text')[0].find(text=True)

    with open('espeon.txt','a',encoding='utf-8') as f:
        f.write(title+'\n')
        f.write(content+'\n\n')