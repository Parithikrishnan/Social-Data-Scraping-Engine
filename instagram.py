import time as t
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests 
from datetime import datetime
from bs4 import BeautifulSoup
import json
import os 


driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')
t.sleep(3)
username = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Phone number, username, or email']")
username.send_keys("USERNAME")   # Username needs to be added
username.send_keys(Keys.TAB)
t.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Password']")
t.sleep(1)
password.send_keys("PASSWORDE")    # Password needs to be added 
password.send_keys(Keys.RETURN)
t.sleep(5)
name_s = input()
searching_url = 'https://www.instagram.com/explore/search/keyword/?q=%23'+name_s
driver.get(searching_url)
response = driver.page_source
t.sleep(7)
search_results = driver.execute_script("return Array.from(document.querySelectorAll('a')).map(a => a.href);")
opening_links = []
for link in search_results:
    if link and "https://www.instagram.com/p/" in link:
        opening_links.append(link)
count = 0


for post_url in opening_links:
    driver.get(post_url)
    t.sleep(2)
    post_html = driver.page_source
    post_soup = BeautifulSoup(post_html, 'html.parser')
    meta_tag = post_soup.find('meta', attrs={'property': 'og:description'})
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    data = 'Date:time : '+formatted_time+"\nContent : "+str(meta_tag)+"\nDetails : "+str(meta_tag['content'])+"\nLink : "+str(post_url)
    with open('Storing_file.txt', 'a') as f:
        f.write(data+'\n\n')
        print(data)
        t.sleep(1)
        os.system('clear')
        count += 1
print("\nData saved to instagram_data.txt and total posts scraped are : "+str(count))
t.sleep(5)
driver.quit()
