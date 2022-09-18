from requests import get
from bs4 import BeautifulSoup
# extractors라는 폴더의 wwr 에서 extract_wwr_jobs를 import하라고함
from extractors.wwr import extract_wwr_jobs

base_url = "https://kr.indeed.com/jobs?q="
search_term = "react"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("can't request page")
else:
  soup = BeautifulSoup(response.text, "html_parse")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  # 바로 밑에있는 li만 찾아주기위해 recursive를 False로 지정
  jobs = job_list.find_all('li', recursive=False)
  for job in jobs:
    print(job)
    print("//////////")