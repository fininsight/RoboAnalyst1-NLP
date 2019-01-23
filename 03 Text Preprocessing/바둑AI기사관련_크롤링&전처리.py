
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
from konlpy.tag import Okt


# In[56]:


# 크롤링
url = 'https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&oid=417&aid=0000370268'
response = requests.get(url)
# response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'html.parser')
news = soup.select('div[id="articleBodyContents"]')
for s in soup('script'):
    s.extract() 


# In[ ]:


# 토큰화
for newsText in news:
    token = Kkma().sentences(newsText.text)


# In[70]:


# 형태소분석
oktTag = []
okt = Okt()
for sentence in token:
    oktTag += okt.pos(sentence)

print(oktTag)


# In[103]:


# 불용어(어미, 구두점, 조사 , 외국어, 알파벳, 숫자등과 최빈어)제거
word = []
stopPos = ['Suffix','Punctuation','Josa','Foreign','Alpha','Number','ScreenName']
stopWord = ['사진','엔터테인먼트','음','때문','한편','무단','칼','럼','했다','라며','있다',
            '이어','졌으나','덧붙였다','않았다','고수','재테크','배포','이','재','및','금지']
for tag in oktTag:
    if tag[1] not in stopPos:
        if tag[0] not in stopWord:
            word.append(tag[0])

print(word)


# In[102]:


#최빈어 검색(불용어 제거를 위함)
from collections import Counter 
Counter(word).most_common() 

