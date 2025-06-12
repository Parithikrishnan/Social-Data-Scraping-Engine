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


    

query_string = input("Enter the input to scrap: ")
query_list = query_string.split(" ")
query_temp = query_list[0]
for i in range(1,len(query_list)):
    query_temp += '+'
    query_temp += query_list[i]
target_url = "https://search.brave.com/search?q= "+query_temp
if(target_url[len(target_url)-1] == '+'):
    temp_url = target_url
    target_url = temp_url[0:(len(temp_url)-1)]
target_url1 = target_url+"+site%3Aquora.com"


driver = webdriver.Firefox()
driver.get(target_url1)


t.sleep(5)                              # Adjust the value based on the network speed 


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
extracted_links = [a['href'] for a in soup.find_all('a', href=True)]
target_links = []
count = 1
counter_value = 3                      # Count of url's that are taken to extract data
for i in extracted_links:
    if("https://www.quora.com/" in i) and (count <= counter_value) and (i not in target_links):
        target_links.append(i)
        count += 1

comments_number = 2             # Number of comments             

for i in target_links:
    driver.get(i)
    t.sleep(5)
    html1 = driver.page_source
    soup = BeautifulSoup(html1, 'html.parser')

    Content_name = soup.title.string
    url_of_page = i
    

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    current_date_time = formatted_time


    for j in range(1,comments_number+1):
        commenting_list = []
        users_list = []
        username_of_user = []
        all_divs = soup.find('div',class_=f'q-box dom_annotate_question_answer_item_{j} qu-borderAll qu-borderColor--raised qu-boxShadow--small qu-mb--small qu-bg--raised')
        all_p_tags = all_divs.find_all('p')

        may_user = [a['href'] for a in all_divs.find_all("a", href=True)]

        for k in may_user:
            if("https://www.quora.com/profile/" in k and k not in users_list):
                users_list = k
                username_of_user = k[30:len(k)]
                break
            

        commenting_data = ''
        for k in all_p_tags:
            commenting_data += k.text+"\n"
        if (commenting_data not in commenting_list):
            commenting_list.append(commenting_data)

        
    data_1 = f'\nTitle    :  {Content_name}\nURL      : {url_of_page}\nTime     :  {current_date_time}\nComments :'
    data_2 = ''
    for k in range(0,comments_number):
        data_2 += f'\n\tUsername  : {username_of_user}\n\tUserprofile : {users_list}\n\tContent  : {commenting_data}\n'
    
    print(data_1 + data_2)
        

      








        






        
        


