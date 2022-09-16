import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
url='https://baike.baidu.com/item/%E7%8C%AB/22261'

req=requests.get(url=url,headers=headers)
req.encoding='utf-8'

html=BeautifulSoup(req.text, 'html.parser')

title=html.find_all('h1')[0].get_text()
print(title)

content=html.find_all('div',class_='abstract')[0].get_text()
print (content)

ths=html.select('.basic-info J-basic-info cmn-clearfix th')

t_list=[]
for t in ths:
    t_text=t.get_text()
    t_list.append(t_text)

print(t_list)

ds=html.select('.basic-info J-basic-info cmn-clearfix .base-info-card-value')

d_list=[]
for d in ds:
    d_text=d.find(text=True).strip()
    d_list.append(d_text)
print(d_list)