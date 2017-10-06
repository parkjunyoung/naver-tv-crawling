from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 데이터를 닮을 변수

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('/Users/ME/Desktop/chromedriver')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

driver.get('http://datalab.naver.com/keyword/realtimeList.naver?datetime=2017-09-28T22:34:00')



# 데이터를 닮을 변수
result = {}

for i in range( 0, 2):
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    #마지막 클래스를 받아온
    rank_inner = soup.select(
            '.keyword_rank'
        )[3].find("div", {"class" : "rank_inner"})


    # 일정 받아오기

    
    rank_title = rank_inner.find("strong", {"class" : "rank_title"})
    date = rank_title.text.replace(' 기준', '').strip()
    print("date : ", date)
    

    # 랭크 리스트 받아오기
    rank_scroll = rank_inner.find("div", {"class" : "rank_scroll"})
    rank_list = rank_scroll.find("ul", {"class" : "rank_list"})

    temp = []    
    for li in rank_list.findAll("li", {"class" : "list"}) :
        temp.append(li.find("span", {"class" : "title"}).text.strip())

    result[date] = temp

    date = ""


    driver.find_element_by_css_selector('.keyword_btn_next').click()
    time.sleep(5)


print(result)

