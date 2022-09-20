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

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    if pagination == None:
      return 1
    pagination = soup.find("div", class_="pagination-list")
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
      return 5
    else:
      return count


get_page_count("python")


def extract_indeed_jobs(keyword):
    #range 는 순서객체를 return해주는 함수, 즉 list같은것을 즉석으로 만들수있다(튜플?)
    pages = get_page_count(keyword)
    for page in range(pages):
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
                  'link': f"https://kr.indeed.com{link}",
                  'company': company.string,
                  'location ': location.string,
                  'position': title
              }
              results.append(job_data)

      for result in results:
          print(result)
