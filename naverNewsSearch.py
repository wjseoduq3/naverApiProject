# import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from naverSearchApi import *

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










app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())