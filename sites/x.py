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


with open ('Storing_file.txt','a') as f:
    f.write("\n\nX Data\n")

driver = webdriver.Firefox()
driver.get('https://x.com/i/flow/login')
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Website opened")
t.sleep(5)
input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")))
t.sleep(3)
input_field.send_keys("Test118278")    # email needs to be added
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Filled\n")
t.sleep(2)
next_button = driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Email done\n")
t.sleep(1)
next_button.click()
t.sleep(10)
#username = driver.find_element(By.CSS_SELECTOR, "input[data-testid='ocfEnterTextTextInput']")
current_time = datetime.now()
#formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
#print(f"{formatted_time} # Username filled\n")
#t.sleep(3)
#username.send_keys("username") #Optional because it is filled only when the account is into suspicious activity 
#t.sleep(4)
#username.send_keys(Keys.RETURN)
t.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
#current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Password filled\n")
t.sleep(2)
password.send_keys("testing@1")             # Password needs to be added
t.sleep(3)
password_click = driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
t.sleep(1)
password_click.click()
t.sleep(10)
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Website loged in\n")
name_s = input()
url_1 = 'https://x.com/search?q='+name_s+'&src=typed_query'
response = driver.get(url_1)
tweet_links = []
count = 0
while True:
    search_results = driver.execute_script("return Array.from(document.querySelectorAll('a')).map(a => a.href);")
    for link in search_results:
        if "/status/" in link:
            try:
                parts = link.split("/")
                idx = parts.index("status")
                clean_link = "/".join(parts[:idx + 2])  
                if clean_link not in tweet_links:
                    tweet_links.append(clean_link)
                    count += 1
            except ValueError:
                continue  
    driver.execute_script("window.scrollBy(0, 500);")
    t.sleep(2)
    if count > 10:         # Number of tweets can be set here
        break
Tweet_counts = 0
for i in tweet_links:
    driver.get(i)
    t.sleep(6)
    content = driver.title
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    data = '\nDate:Time : '+formatted_time+"\nContent : "+str(content)+"\nLink : "+str(i)
    with open('Storing_file.txt', 'a') as f:
        f.write(data+'\n\n')
        print(data)
        t.sleep(3)
        Tweet_counts += 1
        os.system('clear')
t.sleep(4)
print("Website closed with total tweets scraped are : "+str(Tweet_counts))
driver.quit()