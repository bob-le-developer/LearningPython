import requests
from bs4 import BeautifulSoup

from vpscrapy import SL

sl=SL()

url='https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml'

sl.get(url)

print=('bruh')