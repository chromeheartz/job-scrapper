from requests import get
from bs4 import BeautifulSoup
# extractors라는 폴더의 wwr 에서 extract_wwr_jobs를 import하라고함
from extractors.wwr import extract_wwr_jobs

jobs = extract_wwr_jobs("react")
print(jobs)