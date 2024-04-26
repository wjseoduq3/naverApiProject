# 네이버 검색 API 예제 - 뉴스 검색
# import os
# import sys
from urllib.request import *
from urllib.parse import quote
import json
import datetime

class NaverApi:
    def getRequestUrlCode(self, url):
        requestUrl = Request(url)

        client_id = "JkLI65jPvG0LGIvTm2b7"
        client_secret = "API_key"

        requestUrl.add_header("X-Naver-Client-Id", client_id)
        requestUrl.add_header("X-Naver-Client-Secret", client_secret)

        naverResult = urlopen(requestUrl)  # 네이버에서 요청에 의한 응답 반환

        if naverResult.getcode() == 200:  # 응답결과가 정상이면 아래 수행
            print(f"네이버 api 요청 정상 진행: {datetime.datetime.now()}")
            return naverResult.read().decode('utf-8')
        else:
            print(f"네이버 api 요청 실패: {datetime.datetime.now()}")
            return None

    # 검색어 입력함수
    def getNaverSearch(self, node, keyword, start, display):
        baseUrl = "https://openapi.naver.com/v1/search/"  # naver Api 기본 url
        node = f"{node}.json"  # 검색 주제어 입력 부분
        params = f"?query={quote(keyword)}&start={start}&display={display}"
        # 한글처리때문에 quote 사용

        url = baseUrl + node + params

        result = self.getRequestUrlCode(url)

        if result != None:  # 네이버에서 결과가 무엇인가가 정상적으로 도착
            return json.loads(result)
        else:
            print("네이버 응답 실패! 에러 발생!")
            return None