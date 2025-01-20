from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 225
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'C:/Users/Yanen/.cache/selenium/chromedriver/win64/120.0.6099.109/chromedriver.exe'
TWITTER_EMAIL = "YANENDRAJHA37@GMAIL.COM"
TWITTER_PASSWORD = "YanNandani1507"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Class is nothing but a blueprint of items.
class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a .start-text")
        go_button.click()
        time.sleep(60)
        download_speed = (self.driver.find_element(By.CLASS_NAME, value="download-speed"))
        print("Download speed: ", download_speed.text)
        upload_speed = (self.driver.find_element(By.CLASS_NAME, value="upload-speed"))

        print("Upload_speed: ", upload_speed.text)

    # Due to Twitter issue of having multiple login attemt can'T do the twitter login part.
    # def tweet_at_provider(self):
    #     self.driver.get("https://twitter.com/login")
    #
    #     time.sleep(2)
    #     email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    #     email.send_keys(TWITTER_EMAIL)
    #     time.sleep(1)
    #     email.send_keys(Keys.ENTER)
    #     password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    #     password.send_keys(TWITTER_PASSWORD)
    #     time.sleep(1)
    #     password.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     tweet_compose = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
    #     tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    #     tweet_compose.send_keys(tweet)
    #     time.sleep(3)
    #
    #     tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
    #     tweet_button.click()
    #     time.sleep(2)
    #     self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed()
#bot.tweet_at_provider()
