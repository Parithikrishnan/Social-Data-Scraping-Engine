import requests as r

urls = []
user_name = input("Enter the username of the user: ")

for i in range(0,1):
    url = "https://instagram.com/"+user_name+"/"
    urls.append(url)
    url = "https://x.com/"+user_name
    urls.append(url)
    url = "https://threads.com/@"+user_name
    urls.append(url)
    url = "https://reddit.com/r/"+user_name
    urls.append(url)
    
print(urls)
for i in urls:
    response = r.get(i)
    print(i,response.status_code)
