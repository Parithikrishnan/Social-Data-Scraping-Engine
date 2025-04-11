import time as t
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests 
from bs4 import BeautifulSoup
import os 


driver = webdriver.Firefox()
url = input("Enter the name to scrape   : ")
url_1 = 'https://www.threads.net/search?q='+url+'&serp_type=default&hl=en'
driver.get(url_1)
t.sleep(7)
links_results = driver.execute_script("return Array.from(document.querySelectorAll('a')).map(a => a.href);")
post_links = []
count = 0
for link in links_results:
        if "/post/" in link:
            try:
                parts = link.split("/")
                idx = parts.index("post")
                clean_link = "/".join(parts[:idx + 2])  
                if clean_link not in post_links:
                    post_links.append(clean_link)
                    count += 1
            except ValueError:
                continue 
count_1 = 0
for i in post_links:
     driver.get(i)
     t.sleep(3)
     content = driver.title
     current_time = datetime.now()
     formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
     data = 'Date:time : '+formatted_time+"\nContent : "+str(content)+"\nLink : "+str(i)
     with open('threads_data.txt', 'a') as f:
         f.write(data+'\n\n')
         print(data)
         t.sleep(1)
         os.system('clear')
         count_1 += 1
print("The total data got is ",count_1)
t.sleep(2)
driver.quit()