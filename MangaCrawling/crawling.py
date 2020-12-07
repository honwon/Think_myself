from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request
import datetime

try:
    driver = webdriver.Chrome("./chromedriver")
    # 마나토끼 주소
    driver.get("https://manatoki88.net/comic/198920")

    counter = 0

    elem = driver.find_element_by_class_name("toon-title")
    title = elem.get_attribute("title")

    if not os.path.exists(title):
        os.mkdir(title)

    # for _ in range(500):
    #     # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    #     driver.execute_script("window.scrollBy(0,10000)")

    Log("스크롤 완료")
            
    elem =driver.find_elements_by_xpath("//article//img")

    for img in elem:
        counter += 1
        imgurl = img.get_attribute("src")
        Log("이미지 url땀")
        if imgurl.endswith(".png"):
            raw_img = urllib.request.urlopen(imgurl).read()
            Log("이미지 소스 저장")
            File = open(os.path.join(title , title + "_" + str(counter) + ".png"), "wb")
            File.write(raw_img)
            File.close()
            print(imgurl)
   


except Exception as e:
    print(e)
finally:
    print("끝")
    #driver.quit()


def Log(msg):
    base_dir=os.path.dirname(os.path.realpath(__file__))
    
    f = open(os.path.join(base_dir,'auto.log'),'a')
    f.write('[%s] %s\n' %(str(datetime.datetime.now())[:19],msg))
    f.close