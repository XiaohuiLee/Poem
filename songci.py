#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#%%
url = 'https://www.gushiwen.org/gushi/songci.aspx'
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'html5lib')

#%%
def clean(text):
    return text.replace(' ', '')

#%%
span = soup.find_all('span')
f = open('songci.txt', 'w', encoding='utf-8-sig')
rubbishPattern = re.compile(r"<.*?>")
for sp in span:
    son = sp.find('a')
    f.write(clean(son.text))
    poetUrl = son['href']
    sess = requests.session()
    content = sess.get(poetUrl).text
    poetSoup = BeautifulSoup(content, 'html5lib')
    poet = poetSoup.find('div', attrs={"class" : 'contson'}).get_text()
    poet_ = re.sub(rubbishPattern,'', poet)
    # print(poet_)
    f.write(clean(poet_))
    f.write('\n')
f.close()
