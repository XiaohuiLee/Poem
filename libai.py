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
def getpoem(soup):
    title = soup.find_all('h3')
    for ti in title:
        f.write(clean(ti.a.text))
        href = ti.find('a')['href']
        poemURL = prefix + href
        sess = requests.Session()
        poemContent = sess.get(poemURL).content
        poemSoup = BeautifulSoup(poemContent, 'html5lib')
        poem = poemSoup.find('div', attrs={'class':'shici-content'})
        f.write(clean(poem.text))


#%%
def scrapper(url):
    soup = getPage(url)
    getpoem(soup)



#%%
f = open('libai.txt', 'w', encoding = 'utf-8-sig')
scrapper(url)
for i in np.arange(2, 26, 1):
    scrapper(nextPage.format(i))
f.close()