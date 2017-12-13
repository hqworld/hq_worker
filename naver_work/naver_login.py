from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def naver_work(naver_id, naver_pw):
    # 크롬드라이버 위치지정
    driver = webdriver.Chrome('/Users/HqPark/Desktop/naver_work/chromedriver')
    # 팬텀JS 위치지정
    #driver = webdriver.PhantomJS('/Users/HqPark/Desktop/naver_work/phantomjs-2.1.1-macosx 2/bin/phantomjs')
    # 대기시간 3초
    driver.implicitly_wait(3)

#로그인 로직----------->
    driver.get('https://nid.naver.com/nidlogin.login')
    # 아이디/비밀번호를 입력해준다.
    driver.find_element_by_name('id').send_keys(naver_id)
    driver.find_element_by_name('pw').send_keys(naver_pw)
    # 로그인버튼 클릭
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    print('{} 로그인 완료'.format(naver_id))

    return True
