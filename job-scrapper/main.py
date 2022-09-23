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

# from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("what do you want to search for?")

# inddeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

# jobs = indded + wwr
jobs = wwr

#built-in함수
file = open(f"{keyword}.csv", "w")

file.write("Position,Company,Location\n")

for job in jobs:
    file.write(f"{job['position'],{job['company']},{job['location']}}\n")

file.close()


"""
  파일을 열고 내용을 쓰는것
  
  open함수 사용
  열거나 만들려는 파일의 이름을 적는다
  csv는 comma-separated-value 라는 뜻
  맥, 윈도우, 엑셀, 구글문서 등 모두가 csv를 이해할수있다
  ,를 찍고 파일을 열고싶은 모드를 지정해주어야한다.
  예를들어 read-only현재는 "w"로 쓰기전용으로 구현

  csv가 엑셀과 비슷하기때문에 액셀테이블이 가지고있는 열을 작성
  ,로 구분할것이다 그래서 csv라고 함.

  간혹데이터 자체에 , 가 넣어있는것들이있다. csv에서 , 는 엄청 중요하기때문에 가공이필요하다
  그래서 기록전에 , 를 없애주어야함.
"""