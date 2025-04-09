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

driver = webdriver.Firefox()
driver.get('https://x.com/i/flow/login')
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Website opened")
t.sleep(5)
input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")))
t.sleep(3)
input_field.send_keys("parithikris@gmail.com")
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
t.sleep(2)
username = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Username filled\n")
t.sleep(2)
username.send_keys("s1monri") #Optional because it is filled only when the account is into suspicious activity 
t.sleep(3)
username.send_keys(Keys.RETURN)
t.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Password filled\n")
t.sleep(2)
password.send_keys("zA3&Bz95y0[]H~rgi")
t.sleep(3)
password_click = driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
t.sleep(1)
password_click.click()
t.sleep(10)
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_time} # Website loged in\n")
cookies = driver.get_cookies()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])
headers = {'User-Agent': driver.execute_script("return navigator.userAgent;")}
session.headers.update(headers)
name_s = input("Enter the name you want to scrape     : ")
url_1 = 'https://x.com/search?q='+name_s+'&src=typed_query'
response = session.get(url_1)
if(response.status_code == 200):
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    tweet_links = []
    for link in links:
        href = link['href']
        if '/status/' in href:
            tweet_links.append(href)
            print(href)
    for i in tweet_links:
        url_2 = 'https://x.com/'+i
        print(url_2)
        tweet = session.get(url_2)
        soup1 = BeautifulSoup(tweet.content, 'html.parser')
        title_tweet = soup1.title.string
    print(tweet_links,'\n')
else:
    print("Error: ", response.status_code)
print("Website closed")
driver.quit()
