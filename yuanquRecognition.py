#%%
import re
splitPattern = re.compile(r'[。？]')
skipPattern = re.compile(r'《.*?》')
dictPattern = re.compile(r'、')


#%%
# 製作名字的詞典
diction = open('dictionary', 'r', encoding = 'utf-8-sig').read()
muDict = re.compile(re.sub(dictPattern, '|',diction))
print(muDict)


#%% 
def patternSearch(line):
    single = re.split(splitPattern, line)
    for si in single:
        if re.search(muDict, si):
            print(si)
            collection.writelines(si.replace(' ', ''))
            collection.write('\n')
        else:
            pass

#%%
poet = open('yaunqu_notitle.txt', 'r', encoding = 'utf-8-sig' )
collection = open('name2chose_yuanqu.txt','a+', encoding = 'utf-8-sig' )
line = poet.readline()
while line:
    if re.match(skipPattern, line) == None:
        patternSearch(line)
    line = poet.readline()
collection.close()
poet.close()



