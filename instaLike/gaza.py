from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from instaIDPW import ID,PW
import time
import datetime
from random import randint

instaID= ID #인스타그램 ID
instaPW = PW  #인스타그램 PW

#좋아요 기다리는 시간
random_wait_min = 3
random_wait_max = 10
#다음 게시물 팅굼
random_next_min = 1
random_next_max = 5

#새로고침 수
refresh_count = 40
#좋아요 누를 수
onetime_count = 20
# Total Like Count is refesh_count * onetime_count

# 검색할 태그
tag = "#travel"




#한국어 설정 후 화면 띄우기
options = webdriver.ChromeOptions()
options.add_argument("lang=ko_KR")

browser = webdriver.Chrome('./chromedriver', chrome_options=options)
browser.get("https://instagram.com")

#로딩하는 시간 기다리기
time.sleep(2)

#Login ID 속성값 찾고 입력하기
login_id = browser.find_element_by_name('username')
login_id.send_keys(instaID)

#Login PW 속성값 찾기 입력하기
login_pw = browser.find_element_by_name('password')
login_pw.send_keys(instaPW)

# 엔터 푸쉬
login_pw.send_keys(Keys.RETURN)

time.sleep(5)

# 정보 저장 팝업 닫기
popup = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
popup.send_keys(Keys.ENTER)

time.sleep(2)

# 알림 설정 팝업 닫기
popup = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
popup.send_keys(Keys.ENTER)

# 태그 검색 하기
search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(tag)

time.sleep(2)

# 최상위 검색 결과로 진입하기 Enter 두번으로 수행 
search.send_keys(Keys.RETURN) #최상위 검색결과로 Focus 이동
search.send_keys(Keys.RETURN) #검색결과 새로운 창으로 이동

# 현재 url 저장
prev_url = browser.current_url

# 새로고침할 수
for b in range(refresh_count):
    # 최근 게시물 중 첫번쨰 게시물 선택하기
    time.sleep(5)
    feed = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a')
    feed.send_keys(Keys.ENTER)
    time.sleep(1)
    # 다음 버튼 클릭
    nextFeed = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
    nextFeed.click() 

    for a in range(onetime_count):
        time.sleep(3)

        # 좋아요 누르기 랜덤 초 뒤에
        time.sleep(randint(random_wait_min, random_wait_max))
        try:
            like_list = browser.find_elements_by_xpath('//article//section/span/button')
            Log("라이크 리스트 불러움")
            likeBtnTxt = browser.find_elements_by_class_name('_8-yf5 ')
            Log("버튼 불러옴")

            if likeBtnTxt[5].get_attribute("aria-label") != 'Unlike': # or '좋아요'
                Log("if 문 통과")
                like_list[0].click()  # list 중 0번째 버튼을 선택  1=덧글 2=메세지
                like_count += 1
                print("like count = ", like_count)
            else:
                print(likeBtnTxt[5].get_attribute("aria-label"), "Pass like")
        except:
            print("exception!")
            Log("에러남")

        # 다음 피드로 이동하기 랜덤으로 띄어 넘어감
        for b in range(randint(random_next_min, random_next_max)):
            time.sleep(1)
            nextFeed = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
            nextFeed.click()
    # 리프레쉬 ㄱㄱ싱~
    browser.get(prev_url)
    print ("refresh!")

print("종료됬어요!")
    


def Log(msg):
    base_dir=os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(base_dir,'auto.log'),'a')
    f.write('[%s] %s\n' %(str(datetime.datetime.now())[:19],msg))
    f.close
