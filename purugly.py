import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
url='https://baike.baidu.com/item/%E7%8C%AB/22261'

req=requests.get(url=url,headers=headers)
req.encoding='utf-8'

html=BeautifulSoup(req.text, 'html.parser')


dts=html.select('.basic-info dt')
dt_text=[]
for dt in dts:
    t1=dt.get_text()
    dt_text.append(t1)
print(dt_text)

dds=html.select('.basic-info dd')

dd_text=[]
for dd in dds:
    t2=dd.get_text().strip()
    dd_text.append(t2)
print(dd_text)

f=open('espeon.txt','a',encoding='utf-8')
for x in dt_text:
    f.write(x+'\n')

for y in dd_text:
    f.write(y+'\n')
f.close

