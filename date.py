from selenium import webdriver
from bs4 import BeautifulSoup
import time,datetime


def transDateFormat(dateData):
    weekDay = ['월', '화', '수', '목', '금', '토', '일']
    date = dateData.split('T')[0].split('-')
    getWeekDay = datetime.date( int(date[0]) , int(date[1]) ,int(date[2]) ).weekday()
    return dateData.replace('T', ' (' + weekDay[getWeekDay] + ') ' )

# 2017-09-28T22:34:00

print(transDateFormat("2017-09-28T22:34:00"))

