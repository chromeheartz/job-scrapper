"""
    사용한 라이브러리
    requsets
    beautifulSoup
"""
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "react"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("cant't request website")
else:
  # beautifulsoup한테 html을 보내준다고말함
  soup = BeautifulSoup(response.text, "html.parser")
  # class=""이 아닌 class_="" 가 중요하다
  print(soup.find_all('section', class_="jobs")) 