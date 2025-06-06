import requests
# import time
# from fake_useragent import UserAgent

url = "https://www.flipkart.com/refrigerator-store?otracker=nmenu_sub_TVs%20%26%20Appliances_0_Refrigerators"

# headers = {
#     'User-Agent': UserAgent().random,
#     'Accept-Language' : 'en-US,en;q=0.9',
#     'Accept-Encoding' : 'gzip, deflate, br',
#     'Connection' :'keep-alive',
#     'Referer' : 'https://www.google.com'
# }

r = requests.get(url)

with open("file.html", 'w') as f:
    f.write(r.text)
