#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np


#%% 
url = 'http://www.shicimingju.com/chaxun/zuozhe/1.html'
nextPage = 'http://www.shicimingju.com/chaxun/zuozhe/1_{}.html'
prefix = "http://www.shicimingju.com"


#%%
def clean(text):
    return text.replace(' ', '')


def getPage(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html5lib')
    return soup


#%%
def getPoet(soup):
    title = soup.find_all('h3')
    for ti in title:
        f.write(clean(ti.a.text))
        href = ti.find('a')['href']
        poetURL = prefix + href
        sess = requests.Session()
        poetContent = sess.get(poetURL).content
        poetSoup = BeautifulSoup(poetContent, 'html5lib')
        poet = poetSoup.find('div', attrs={'class':'shici-content'})
        f.write(clean(poet.text))


#%%
def scrapper(url):
    soup = getPage(url)
    getPoet(soup)



#%%
f = open('libai.txt', 'w', encoding = 'utf-8-sig')
scrapper(url)
for i in np.arange(2, 26, 1):
    scrapper(nextPage.format(i))
f.close()