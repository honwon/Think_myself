from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from openpyxl import Workbook

driver = webdriver.Chrome("./chromedriver")
datafile = open("nicknames.txt", "w")
wb = Workbook()
ws = wb.create_sheet("nick")
driver.get("http://afevent2.afreecatv.com:8120/app/rank/index.php")

elem = driver.find_element_by_id("wideArea")

nicknames = elem.find_elements_by_class_name("nick")

for name in nicknames:
    ws.append([name.text])
    datafile.write(name.text+"\n")

wb.save("kkk.xlsx")
