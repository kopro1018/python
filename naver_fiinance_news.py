from bs4 import BeautifulSoup
import requests

# 웹 페이지 가져오기
url = 'https://finance.naver.com/'
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 특정 태그에서 데이터 추출
title = soup.title.text
print("웹 페이지 제목:", title)

# 클래스 이름을 기반으로 요소 선택
articles = soup.find_all('div', class_='news_area')
for article in articles:
    print(article.text)

