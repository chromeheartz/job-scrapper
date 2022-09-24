def save_to_file(file_name, jobs):
    #built-in함수
    file = open(f"{file_name}.csv", "w")

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