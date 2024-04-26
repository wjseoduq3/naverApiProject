# import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from naverSearchApi import *

import webbrowser

form_class = uic.loadUiType("ui/naverNewsSearchAppUi.ui")[0]
# 외부에서 ui 불러올 때 [0]/ 내부 [1]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("네이버 뉴스 검색 앱")
        self.setWindowIcon(QIcon("img/news.png"))
        self.statusBar().showMessage("Naver News Search App v1.0")

        self.searchBtn.clicked.connect(self.searchBtn_clicked)
        self.result_table.doubleClicked.connect(self.link_doubleClicked)
        # 테이블 항목이 더블클릭되면 이 함수 호출

    def searchBtn_clicked(self):
        keyword = self.input_keyword.text()

        if keyword == "":
            QMessageBox.warning(self, "입력 오류!", "검색어는 필수 입력 사항입니다.")
        else:
            naverApi = NaverApi()  # import된 naverSearchApi 내의 NaverApi 클래스로 객체생성
            searchResult = naverApi.getNaverSearch("news", keyword, 1, 50)
            # print(searchResult)
            newsResult = searchResult['items']
            self.outputTable(newsResult)

    def outputTable(self, newsResult):  # 뉴스 검색결과를 테이블 위젯에 출력하는 함수
        self.result_table.setSelectionMode(QAbstractItemView.SingleSelection)  # 무조건 들어가는 부분
        # 몇행, 몇열인지 정하는 부분 -->3열, 행은 가변적
        self.result_table.setColumnCount(3)
        self.result_table.setRowCount(len(newsResult))  # 뉴스의 갯수만큼 행 설정

        # 첫 행,열의 이름 결정
        self.result_table.setHorizontalHeaderLabels(["기사제목","기사링크","게재일시"])
        # 열의 길이 설정(총길이 620을 3등분)
        self.result_table.setColumnWidth(0, 220)
        self.result_table.setColumnWidth(1, 220)
        self.result_table.setColumnWidth(2, 180)
        # 테이블에 출력되는 검색결과를 더블클릭해도 수정 못하게 함
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, news in enumerate(newsResult):  # i -> 0~9
            newsTitle = news['title']
            newsTitle = newsTitle.replace('&quot','').replace(';','').replace('<b>','').replace('</b>','')
            newsLink = news['originallink']
            newsDate = news['pubDate']
            newsDate = newsDate[0:25]

            self.result_table.setItem(i,0, QTableWidgetItem(newsTitle))
            self.result_table.setItem(i,1, QTableWidgetItem(newsLink))
            self.result_table.setItem(i,2, QTableWidgetItem(newsLink))

    # 해당기사 더블클릭시 해당 사이트 연결 기능
    def link_doubleClicked(self):
        selectedRow = self.result_table.currentRow()  # 현재 더블클릭된 행의 인덱스 가져오기
        selectedLink =  self.result_table.item(selectedRow, 1).text()  # 현재 더블클릭된 셀의 텍스트 가져오기
        webbrowser.open(selectedLink)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())