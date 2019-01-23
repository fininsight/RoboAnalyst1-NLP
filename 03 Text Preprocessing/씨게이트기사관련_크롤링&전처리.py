
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
from konlpy.tag import Okt


# In[3]:


# 크롤링
url = 'https://news.v.daum.net/v/20181020130619303'
response = requests.get(url)
# response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'html.parser')
news = soup.select('div[class="news_view"]')


# In[4]:


# 토큰화
for newsText in news:
    token = Kkma().sentences(newsText.text)


# In[7]:


# 형태소 분석
okt = Okt()
oktTag = []

for sentence in token:
    oktTag += okt.pos(sentence)

print(oktTag)


# In[8]:


# 불용어(어미, 구두점, 조사 , 외국어, 알파벳, 숫자등과 최빈어)제거
word = []
stopPos = ['Suffix','Punctuation','Josa','Foreign','Alpha','Number','Email']
stopWord = ['있도록','기자','있다','및','의','했다고','했다는','할','수']

for tag in oktTag:
    if tag[1] not in stopPos:
        if tag[0] not in stopWord:
            word.append(tag[0])

print(word)


# In[14]:


#최빈어 검색(불용어 제거를 위함)
from collections import Counter 
Counter(word).most_common() 

