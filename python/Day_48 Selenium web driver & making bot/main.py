from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after running selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event = {}

for n in range(len(event_times)):
    event[n] = {"time" : event_times[n].text,
                "name" : event_name[n].text}

print(event)
driver.quit()

# # Using find_element & name to search through the site & create search bar.
# # We can find element by Name, ID, Class, CSS Selector or even Xpath (Most powerful).

# driver.get("https://python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# button = driver.find_element(By.ID, value="submit")
#
# print(search_bar.get_attribute("placeholder"))
# print(button.size)
#
# driver.quit()

# # Getting price for an item on amazon
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
#
# # find_element create an element of html. To access the data with in use .text
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"the price is : {price_whole.text}.{price_fraction.text}")
#
# driver.quit()
#
# # driver.close()
