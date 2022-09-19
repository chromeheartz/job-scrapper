"""
    사용한 라이브러리
    requsets
    python코드에서 웹사이트로 request를 보낼수있게 해준다
    get 은 function인데 이동한 다음에 website를 가져오는것

    beautifulSoup
    find_all같은 document에서 HTML태그를 찾게 해준다
    html을 첫번째 argument로 전해주고 html.parser라는 문자열을 전달해줌
    이것은 내가 beautifulSoup한테 html을 보내준다고 말하는것

    selenium
    selenium은 브라우저를 자동화 할수있는 프로그램
    webdriver는 파이썬에서 브라우저를 시작할 수 있는 방법
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#options의 instance라는것을 알려줌
options = Options()
# replit에서 동작시키기위함
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")


soup = BeautifulSoup(browser.page_source, 'html.parser')
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        results = []
        # h2를 찾고 a를 찾는 대신 select로 selector를 이용해찾음
        # beautifulSoup은 HTML태그들을 데이터구조로 가져온다 list,dictionary
        anchor = job.select_one(".jobTitle a")
        title = anchor['aria-label']
        link = anchor['href']
        # 정보와 위치 찾기
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        # 데이터 추출위해 정리
        job_data = {
          'link' : f"https://kr.indeed.com{link}",
          'company' : company.string,
          'location ' : location.string,
          'position' : title
        }
        results.append(job_data)

for result in results:
  print(result, "|n\\\\\\\")

"""
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "react"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("cant't request website")
else:
  # 빈 배열을 만들어 결과물들을 넣어줄것
  results = []
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
          anchors = post.find_all('a')
            anchor = anchors[1]
            # beautiful soup은 dictionary처럼 반환해주기 때문에 이렇게 찾는것도가능
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company")
            # print(company)
            title = anchor.find('span', class_="title")            
            job_data = {
              # 태그안에 있는 문자열 출력
              'company' : company.string,
              'region' : region.string,
              'position' : title.string
            }
            # loop가 한번 돌아 job을 추출할때마다 그것들을 for loop의 밖에서 저장해낼것이다
            results.append(job_data)

  for result in results:
  print(result)
  print("//////////////")
"""
