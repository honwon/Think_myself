from selenium import webdriver
from openpyxl import load_workbook
from openpyxl import Workbook

# 클래스 생성
wb = Workbook()

# 지정한 이름의 시트 생성
ws = wb["Sheet"]

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com")

# A열값 하나하나씩
for i in range(5):
    ws.append([i])

# 마지막으로 완료된 엑셀파일 저장
wb.save("인스타포스트.xlsx")