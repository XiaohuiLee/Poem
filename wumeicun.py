#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


#%%

url = 'https://zh.wikisource.org/zh/%E5%90%B3%E6%A2%85%E6%9D%91%E9%9B%86'
sess = requests.session()
content = sess.get(url).content
soup = BeautifulSoup(content, 'html5lib')


#%%
r = 'mw-headline'

