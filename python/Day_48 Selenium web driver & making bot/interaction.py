from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first = driver.find_element(By.NAME, value="fName")
last = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first.send_keys("Yanendra", Keys.ENTER)
last.send_keys("Jha", Keys.ENTER)
email.send_keys("Yanendrajha37@gmail.com", Keys.ENTER)

# # Find item by link text
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # all_portals = driver.find_element(By.LINK_TEXT,value="content portals")
#
# # Find the "search" <input> by name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("python", Keys.ENTER)
#
# driver.quit()
# # Getting total article count from the wikipedia main page server. Use Click to click on the data.


# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
