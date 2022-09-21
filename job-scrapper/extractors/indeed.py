from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
      print("cant't request website")
  else:
      # 빈 배열을 만들어 결과물들을 넣어줄것
      results = []
      soup = BeautifulSoup(response.text, "html.parser")
      jobs = soup.find_all('section', class_="jobs")
      # built-in function len은 list나 tuple의 크기를 준다
      # print(len(jobs))
      for job in jobs:
          job_posts = job.find_all('li')
          #pop은 list에서 한 항목을 제거. -1로 마지막 제거
          job_posts.pop(-1)
          for post in job_posts:
              anchors = post.find_all('a')
              anchor = anchors[1]
              link = anchor['href']
              company, kind, region = anchor.find_all('span', class_="company")
              # print(company)
              title = anchor.find('span', class_="title")            
              job_data = {
                # 태그안에 있는 문자열 출력
                'company' : company.string,
                'location' : region.string,
                'position' : title.string
              }
              # loop가 한번 돌아 job을 추출할때마다 그것들을 for loop의 밖에서 저장해낼것이다
              results.append(job_data)
  
      #print만 하는것이 아닌 다른파일에도 적용을 위해 return으로 빼준다
      return results