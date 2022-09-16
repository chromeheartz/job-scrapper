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
  # built-in function len은 list나 tuple의 크기를 준다
  # print(len(jobs))
  for job in jobs:
      job_posts = job.find_all('li')
      #pop은 list에서 한 항목을 제거. -1로 마지막 제거
      job_posts.pop(-1)
      for post in job_posts:
          print(post)
          print("/////////////////")

"""
  class_="jobs"는 keyword argument라고 한다
  우리한테 익숙한것은 positional argument이다.

  positional argument은 위치에 따라 무엇이 올지 아는것
  keyword argument는 자리에 더이상 신경쓰지않을때 중요해진다
  자리에 신경안쓰는대신 argument이름에 신경을쓰는것
  변수명="넘겨줄인자" 이런식으로 써줌. 순서는 신경안써도괜찮음
"""