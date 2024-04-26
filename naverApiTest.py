# 네이버 검색 API 예제 - 뉴스 검색
import os
import sys
import urllib.request
client_id = "ObWMjVg0pDkE2qP1ThA_"
client_secret = "Zagi_qOOA3"
encText = urllib.parse.quote("이란")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)  # 기본값이 최근 10개



