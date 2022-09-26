"""
  request에 대한 정보를 접근 
  request 는 브라우저가 웹사이트에가서 콘텐츠를 요청하는것을 말한다. 많은정보를 담고있음. 
  요청하고있는 URL이 무엇인지, IP주소, Cookies를 담고있는지 등등
"""
from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

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

db = {}

@app.route("/search")
def search():
    # print(request.args)
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
      jobs = db[keyword]
    else:
      wwr = extract_wwr_jobs(keyword)
      jobs = wwr
      db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        # keyword 저장위해 먼저 search로 보내기
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    """
      send_file은 첫번째 argument로 파일의 이름이 필요
      다운로드가 되도록 as_attachment=True로 지정
    """
    return send_file(f"{keyword}.csv", as_attachment=True)


"""
  app.run을 호출하면 flask application을 만듬
  네개의 0을 넣어주면 Replit이 웹서버를 만들려고하는것을 인식해서
  브라우저창이랑 서버 console을 열어준다
"""
app.run("0.0.0.0")
