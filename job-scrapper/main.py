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
from flask import Flask, render_template

app = Flask("jobScrapper")
"""
  @가 있는 코드를 함수의 위에 위치
  decorator라고도 함. syntactic sugar
  decorator를 함수위에 두면 Flask는
  user가 이 주소의 page를 방문했을 때
  함수를 호출해야하는것을 알게된다
"""


@app.route('/')
def home():
    # python은 백엔드다. bibi라는 데이터,문자열은 백엔드에서부터 전달되고있다.
    return render_template("home.html", name="bibi")


@app.route("/hello")
def hello():
    return 'hello you!'


app.run("0.0.0.0")
