
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
from konlpy.tag import Okt


# In[3]:


#크롤링
url = 'http://news.chosun.com/site/data/html_dir/2018/07/10/2018071004121.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'html.parser')
news = soup.select('div[class="par"]')


# In[ ]:


# 토큰화
for newsText in news:
    token = Kkma().sentences(newsText.text)


# In[4]:


# 형태소분석
oktTag = []

for sentence in token:
    oktTag += Okt().pos(sentence)

print(oktTag)


# In[17]:


# 불용어(어미, 구두점, 조사 , 외국어, 알파벳, 숫자와 최빈어)제거
word = []
stopPos = ['Suffix','Punctuation','Josa','Foreign','Alpha','Number']
stopword = ['했다','것','있는','한다','하는','그','있다','할','를','이','이런',
           '되기','해야','있게','여기']

for tag in oktTag:
    if tag[1] not in stopPos:
        if tag[0] not in stopword:
            word.append(tag[0])

print(word)


# In[14]:


#최빈어 검색(불용어 제거를 위함)
from collections import Counter 
Counter(word).most_common() 

