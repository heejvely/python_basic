#!/usr/bin/env python
# coding: utf-8

# DOM(Document Object Model)의 정의
# - HTML, XML 문서의 프로그래밍 인터페이스 : 구조화된 표현 및 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
# - 트리 구조로 형성되어 있음 : 부모 노드(위쪽), 자식 노드(아래쪽)
# - HTML에서 노드는 \<head>, \<body>, \<h1>, \<script> 등의 태그뿐만 아니라 태그 내 텍스트나 속성 모두 노드에 속함
# - BeautifulSoup 모듈의 함수를 활용하여 노드를 기준으로 원하는 데이터 추출

# In[1]:


html="""
<html>
<head>
    <title>crawler</title>
</head>
<body>
    <p class="a" align="center"> text1</p>
    <p class="b" align="center"> text2</p>
    <p class="c" align="center"> text3</p>
    <div>
        <img src="/source" width="300" height="200">
    </div>
</body>
</html>
"""

from bs4 import BeautifulSoup

bs = BeautifulSoup(html,'html.parser')
contents = bs.find('body')

for child in contents.children:
    print(child)


# In[2]:


# body의 자손은 p, div, img
for d in contents.descendants:
    print(d)


# In[3]:


img_tag = contents.find('img')
print(img_tag)
print(img_tag.parent)


# In[5]:


contents = bs.find('body')
print(img_tag.find_parent('body'),'\n')
print(img_tag.find_parent('div'))


# In[6]:


p_tag = bs.find('p',class_='b')
print(p_tag)


# In[7]:


from urllib import request as req
from bs4 import BeautifulSoup

res = req.urlopen('https://naver.com')
bs = BeautifulSoup(res,'html.parser')
print(bs.find('a'),'\n')
print(bs.find(class_='link_newsstand'),'\n')
print(bs.find('a',{'class':'link_newsstand'}),'\n')

# 클래스가 여러개인 경우
eles = bs.find_all('a',{'class':['link_newsstand','btn_sort','btn_sort.sort_on']})
for e in eles:
    print(e.text)


# In[8]:


hlists = bs.findAll({'h1','h2','h3','h4','h5','h6'},limit = 3)
for h in hlists:
    print(h,'\n')


# In[9]:


# 정규표현식과 bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'html.parser')
images = bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])


# In[ ]:


# 한빛 네트워크 사이트 로그인 후 점수 가져오기

import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome('C:/tool/chromedriver.exe')
driver.get('https://www.hanbit.co.kr/')
element = driver.find_element_by_class_name('login')
element.click()
m_id = ''
m_passwd = ''

element = driver.find_element_by_id('m_id')
element.send_keys(m_id)
time.sleep(1)

element = driver.find_element_by_id('m_passwd')
element.send_keys(m_passwd)
time.sleep(1)

element = driver.find_element_by_class_name('btn_login')
element.click()

driver.get('https://www.hanbit.co.kr/myhanbit/myhanbit.html')
source = driver.page_source
bs = BeautifulSoup(source, 'html.parser')
a = bs.select_one('#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span')
print(a.text,'점')
time.sleep(3)
driver.close()


# header 확인: http://www.useragentstring.com/

# In[12]:


# 구글 플레이에서 인기 영화 제목 30개 출력(requests + bs4)
import requests
from bs4 import BeautifulSoup

headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

url = 'https://play.google.com/store/movies/top'

res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
movies = bs.find_all('div',class_='WsMG1c nnK0zc')

print(len(movies))
for m in movies:
    print(m.text)


# In[19]:


# Q. 구글 플레이에서 인기 영화 제목 200개 출력(selenium + bs4)
from selenium import webdriver

driver = webdriver.Chrome('C:/tool/chromedriver.exe')
driver.maximize_window()

url = 'https://play.google.com/store/movies/top'
driver.get(url)

# 1080 위치로 스크롤 내리기
# driver.execute_script('window.scrollTo(0,1080)') 
# 화면 가장 아래로 스크롤 내리기
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

import time

# 현재 문서 높이를 가져와서 저장
prev_height = driver.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # 페이지 로딩 대기
    driver.implicitly_wait(10) # 브라우저에서 파싱되는 지연 시간 기다려줌
    curr_height = driver.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    prev_height = curr_height
print('스크롤 완료')

bs = BeautifulSoup(driver.page_source,'html.parser')
movies = bs.find_all('div',attrs = {'class':'Epkrse '})

print(len(movies))
for m in movies:
    print(m.text)

