"""
    사용한 라이브러리
    requsets
    beautifulSoup
"""
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

  category of arguments

  class_="jobs"는 keyword argument라고 한다
  우리한테 익숙한것은 positional argument이다.

  positional argument은 위치에 따라 무엇이 올지 아는것
  keyword argument는 자리에 더이상 신경쓰지않을때 중요해진다
  자리에 신경안쓰는대신 argument이름에 신경을쓰는것
  변수명="넘겨줄인자" 이런식으로 써줌. 순서는 신경안써도괜찮음
"""

"""

  dictionary's short cut

  python에서 object list를 가지고있고 list의 길이를 안다면
  list에서 object를 가져오는 코드가있다

  list_of_numbers = [1,2,3]
  # 이런씩으로 하나하나 가져오는것이 아닌
  first = list_of_numbers[1]
  # 각 위치에맞게 변수지정가능. 하지만 길이를 알아야함
  first, second, third = list_of_numbers
"""