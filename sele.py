from selenium import webdriver
from bs4 import BeautifulSoup
import time, datetime
import xlwt

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('/Users/ME/Desktop/chromedriver')

# 브라우저를 띄울 시간으로 3초까지 기다려 준다.
driver.implicitly_wait(3)

driver.get('http://datalab.naver.com/keyword/realtimeList.naver?datetime=2017-09-28T22:34:00')



# 데이터를 닮을 변수
result = {}

for i in range( 0, 121):
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    #마지막 클래스를 받아온
    rank_inner = soup.select(
            '.keyword_rank'
        )[3].find("div", {"class" : "rank_inner"})


    # 일정 받아오기
    rank_title = rank_inner.find("strong", {"class" : "rank_title"})
    date = rank_title.text.replace(' 기준', '').strip()

    # 랭크 리스트 받아오기
    rank_scroll = rank_inner.find("div", {"class" : "rank_scroll"})
    rank_list = rank_scroll.find("ul", {"class" : "rank_list"})

    temp = []    
    for li in rank_list.findAll("li", {"class" : "list"}) :
        temp.append(li.find("span", {"class" : "title"}).text.strip())

    result[date] = temp


    driver.find_element_by_css_selector('.keyword_btn_next').click()
    time.sleep(0.5) #클릭 후 마무리 하고 0.5초 쉬어줌
    print(i+1, " 번째 완료")

# 엑셀저장
wb = xlwt.Workbook()
ws = wb.add_sheet('크롤링 Data')

i = 0
for date, data in result.items():
    j = 1
    for value in data:
        if(j==1):
            ws.write(i, 0 , date)
            i += 1
        ws.write(i, 0 , j)
        ws.write(i, 1 , value)
        j += 1
        i += 1

wb.save('crawl.xls')