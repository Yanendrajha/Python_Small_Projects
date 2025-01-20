import requests
from bs4 import BeautifulSoup

# Getting response through api of the amazon product I want to check the price of.
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
Accept_Language = "en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-US;q=0.6,en-GB;q=0.5"
headers = {'Accept-Language': Accept_Language,
           'User-Agent': User_Agent}

response = requests.get(url, headers=headers)
site_data = response.text  # Getting the html text out of the api call


# Using BeautifulSoap to get the data for scrapping. Using find method to get the exact price amount needed
soup = BeautifulSoup(site_data, "lxml")
price1 = soup.find(name="span", class_="a-offscreen").getText()
price = float(price1.split("$")[1])
print(price)
print(type(price))
