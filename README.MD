# 本库用于抓取唐诗（李白的）宋词以及元曲，并匹配木字旁的字

## 基本步骤
使用requests库抓取网页内容，分析实体（诗、词、曲）对应的页面链接，跳转到对应页面后使用BeautifulSoup匹配文本从而抓取目标内容

## 文件解释

|文件|什么东西|
|:---------- | :--- |
|libai.py|爬取李白诗词的爬虫|
|songci.py|爬取宋词的爬虫|
|yuanqu.py|爬取元曲的爬虫|
|libaiRecognition.py|识别李白诗词中包含木字旁的字的诗词解析代码|
|songciRecognition.py|识别宋词中包含木字旁的字的宋词解析代码|
|yuanquRecognition.py|识别元曲中包含木字旁的字的元曲解析代码|
|libai.txt|李白诗词|
|songci.txt|宋词|
|yaunqu.txt|元曲|
|yaunqu_notitle.txt|元曲（不包含标题）|
|name2chose_libai.txt|李白诗词中包含木字旁的字的诗词|
|name2chose_songci.txt|宋词中包含木字旁的字的宋词|
|name2chose_yuanqu.txt|元曲中包含木字旁的字的元曲|


## 使用方法

以爬取宋词为例
### 第一阶段：爬取宋词文本内容
```python
python songci.py
```
结果保存在songci.txt当中

### 第二阶段：匹配木字旁的字
整个过程是基于词典思想设计的，使用木字旁的词典并对宋词的每句诗进行文本匹配，将匹配到的诗句保存到name2chose_songci.txt中。

```
python songciRecognition.py
```
## 结果展示

宋词：

![](https://github.com/XiaohuiLee/Poem/blob/master/output/songci.png)



匹配到的宋词：

![](https://github.com/XiaohuiLee/Poem/blob/master/output/name2choose_songci.png)

## 后记

### 什么都可以碰，不要碰女人，去他妈恋爱