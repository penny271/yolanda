#! 再現できなかったが、次の商品詳細のページに遷移するタイミングで認証が起きている模様
from ast import keyword
from concurrent.futures import thread
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import random
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from tqdm import tqdm


user_agent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15']

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
options.add_argument('--incognito')
options.add_experimental_option('detach', True)

options.add_experimental_option('excludeSwitches', ['enable-logging'])

#! Change executable path according to your chrome webdriver location

service = Service("/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver")
# service = Service("C:\\chromedriver")
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()

#you can change the search keyword from here
searchKeyword = 'nike'
driver.get('https://www.2ndstreet.jp/search?category=950001&keyword=%s&sortBy=arrival&page=1'% (searchKeyword))

#To find the total number of pages
page_number = driver.find_element(By.CLASS_NAME, 'pager').text[4]

#For storing products links
product_link_list= []

#For storing all the products images link
img_links_list=[]

#Page numbers range LOOP. Change it if you want to visit less or more pages.
for i in range(1,int(page_number)+1):

    #This line will open chrome with provided page number url
    driver.get('https://www.2ndstreet.jp/search?category=950001&keyword=%s&sortBy=arrival&page=%i'% (searchKeyword,i))
    driver.implicitly_wait(3)

    #This will get the whole div in which the products are present
    products_list = driver.find_element(By.CLASS_NAME, 'itemList')

    #This will find all the link tag in the div
    products_links = products_list.find_elements(By.TAG_NAME, 'a')

    #Variable to hold Products links on a specific page
    products_page=[]

    #Looping through all the products to get the images
    for product_link in products_links:

        #After visiting each product the website asks for login so in order to bypass that
        if product_link.get_attribute('href') == 'https://www.2ndstreet.jp/user/login':
            pass
        else:
            products_page.append(product_link.get_attribute('href'))

    for product in products_page:
        driver.get(product)
        sleep(2)
        page_soup = BeautifulSoup(driver.page_source, 'lxml')
        zoom_pictures = []
        pictures = page_soup.select('div[class="goods_popname"] > ul > li')

        for i, picture in enumerate(pictures):
            picture = picture.select_one('img').get('data-src')
            zoom_pictures.append(picture)
        img_links = '|'.join(zoom_pictures)
        img_links_list.append([img_links])
        print(img_links_list)

#It will create a new file inside the project
with open('new_file.csv', 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['PicURL'])
    writer.writerows(img_links_list)
