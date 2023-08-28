from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By


start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("/Users/anugu/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(start_url)
time.sleep(10)
scraped_data=[]


def scrape():
    headers = ["STAR-NAME","DISTANCE","MASS","RADIUS","LUMINOSITY"]
    planets_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for th_tag in soup.find_all("th",attrs={"class","exoplanet"}):
            td_tag = td_tag.find_all("td")
            tempt_list = []
            for index,td_tag in enumerate(td_tag):
                if index == 0:
                    tempt_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempt_list.append(td_tag.contents[0])
                    except:
                        tempt_list.append("")
            planets_data.append(tempt_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper_2.csv","w") as z:
        csv_writer = csv.writer(z)
        csv_writer.writerow(headers)
        csv_writer.writerows(planets_data)
