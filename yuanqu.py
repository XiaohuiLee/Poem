#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#%%
url = 'https://www.gushiwen.org/gushi/yuanqu.aspx'
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'html5lib')

#%%
def clean(text):
    return text.replace(' ', '')

#%%
span = soup.find_all('span')
f = open('yaunqu.txt', 'w', encoding='utf-8-sig')
rubbishPattern = re.compile(r"<.*?>")
for sp in span:
    son = sp.find('a')
    f.write(clean(son.text))
    poemUrl = son['href']
    sess = requests.session()
    content = sess.get(poemUrl).text
    poemSoup = BeautifulSoup(content, 'html5lib')
    poem = poemSoup.find('div', attrs={"class" : 'contson'}).get_text()
    poem_ = re.sub(rubbishPattern,'', poem)
    # print(poem_)
    f.write(clean(poem_))
    f.write('\n')
f.close()
