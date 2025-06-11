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



query_string = input("Enter the name to scrape :")
query_list = query_string.split(" ")
query_temp = query_list[0]
for i in range(1,len(query_list)):
    query_temp += '+'
    query_temp += query_list[i]
target_url = "https://www.youtube.com/results?search_query="+query_temp
if(target_url[len(target_url)-1] == '+'):
    temp_url = target_url
    target_url = temp_url[0:(len(temp_url)-1)]


with open ('Storing_file.txt','a') as f:
    f.write('\nYoutube Data')


driver = webdriver.Firefox()
driver.get(target_url)


t.sleep(5)                              # Adjust the value based on the network speed 



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
extracted_links = [a['href'] for a in soup.find_all('a', href=True)]
target_links = []
count = 1
counter_value = 5                      # Count of url's that are taken to extract data
for i in extracted_links:
    if("/watch?v=" in i) and (count <= counter_value) and (i not in target_links):
        target_links.append(i)
        count += 1
total_usable_links = []
for i in target_links:
    removing_index = i.index('&')
    temp_links = i[0:(removing_index)]
    total_usable_links.append(temp_links)

for i in total_usable_links:
    
    try:
        total_url_video = 'https://youtube.com'+i
        driver.get(total_url_video)
        t.sleep(5)
        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'html.parser')
        Video_title = soup.find('title').text
        url_of_video = total_url_video

        div_details = soup.find('div',id='info-container')

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        current_date_time = formatted_time

        clean_div_data = div_details.text.strip()

        view_index = clean_div_data.index("views")
        Views = clean_div_data[0:view_index+5]

        upload_index = clean_div_data.index('ago')
        upload_time = clean_div_data[view_index+5:upload_index+3]

        complete_data = '\n\nTitle : '+Video_title+'\nURL   : '+url_of_video+'\nTime  : '+current_date_time+'\nViews : '+Views+'\nUpload Time : '+upload_time+'\n'
        with open('Storing_file.txt','a') as f:
            f.write(complete_data)

    except:
        print("\nError in loading the above program\n")
        break

driver.quit()
