# from requests import get

websites = ("https://google.com", "airbnb.com", "https://twitter.com",
            "facebook.com")

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)

    if response.status_code == 200:
        results[website] = "OK"  #새로운 키를 dictionary에 추가
    else:
        results[website] = "FAILED"

print(results)

"""
  get이라는 함수를 써서 response를 받아와서
  서버상태코드가 200일경우에 result라는 dictionary에 추가
"""