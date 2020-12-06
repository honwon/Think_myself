from selenium import webdriver


try:
    driver = webdriver.Chrome("./chromedriver")
    # 마나토끼 주소
    driver.get("https://manatoki88.net/comic/198920")

    elem =driver.find_elements_by_class_name("view-content scroll-viewer")
    print(elem)
    


except Exception as e:
    print(e)
finally:
    print("끝")
    #driver.quit()
