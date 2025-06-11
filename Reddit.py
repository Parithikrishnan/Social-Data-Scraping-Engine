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
target_url = "https://www.reddit.com/search/?q="+query_temp
if(target_url[len(target_url)-1] == '+'):
    temp_url = target_url
    target_url = temp_url[0:(len(temp_url)-1)]


with open ('Storing_file.txt','a') as f:
    f.write('\nReddit Data')


driver = webdriver.Firefox()
driver.get(target_url)


t.sleep(5)                              # Adjust the value based on the network speed 



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
extracted_links = [a['href'] for a in soup.find_all('a', href=True)]
target_links = []
count = 1
counter_value = 3                      # Count of url's that are taken to extract data
for i in extracted_links:
    if("/r/" in i) and (count <= counter_value*2) and (i not in target_links):
        target_links.append(i)
        count += 1

user_profile_link = []
reddit_post_link = []

for i in target_links:
    if("/comments/" in i):
        reddit_post_link.append(i)
    else:
        user_profile_link.append(i)

for i in range(0,len(reddit_post_link)):
    total_url = 'https://reddit.com'+reddit_post_link[i]
    driver.get(total_url)
    t.sleep(5)
    html1 = driver.page_source
    soup = BeautifulSoup(html1, 'html.parser')
    reddit_content_invalid = soup.title.string
    for i in reddit_content_invalid:
        r_index = reddit_content_invalid.index('r/')
        reddit_content_valid = reddit_content_invalid[0:r_index-1]
        Username = reddit_content_invalid[r_index:len(reddit_content_invalid)]

    url_of_post = total_url
    dateandtime = soup.find('time')
    ago_time = dateandtime.text
    Accurate_date_and_time = dateandtime['datetime']
    comments_of_reddits = soup.find_all('shreddit-comment')

    Arialabels = []
    user_profile_link = []
    Content_of_comments = []
    counting_comments = 1
    counter_setter = 2                              # Number of comments

    for i in comments_of_reddits:
        if(counting_comments > counter_setter):
            break
        Arialabels.append(i['arialabel'])
        para_holder = i.find('p').text
        Content_of_comments.append(para_holder)
        user_profile_link.append('https://reddit.com/user/'+i['author']+'/')
        counting_comments += 1

    big_data = ''
    for i in range(0,len(Arialabels)):
        big_data += f"\n\t{Arialabels[i].strip()}\n\tUser Profile : {user_profile_link[i].strip()}\n\tContent : {Content_of_comments[i].strip()}\n\t"    
    Complete_data = "\n\n\nContent : "+reddit_content_valid+"\nUsername : "+Username+"\nURL      : "+url_of_post+"\nTime     : "+Accurate_date_and_time+"\nComments : "+"\n\t"+big_data.strip()
    
    with open('Storing_file.txt','a') as f:
        f.write(Complete_data)
    

driver.quit()