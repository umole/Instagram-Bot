from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

INSTAGRAM_UN = ""
INSTAGRAM_PASS = ""


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        self.driver.get("http://www.instagram.com")

        # Input the login parameters
        username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username.send_keys(INSTAGRAM_UN)

        password = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password.send_keys(INSTAGRAM_PASS)
        password.send_keys(Keys.ENTER)

        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._ac8f button._acan'))).click()
        except NoSuchElementException:
            pass
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._a9-z button._a9_1'))).click()
        except NoSuchElementException:
            print("Pass")
            pass

    def find_following(self):
        time.sleep(3)
        self.driver.find_elements(By.CSS_SELECTOR, "svg._ab6-")[2].click()
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button._acat"))).click()
        search_user = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_user.send_keys("")
        search_user.send_keys(Keys.ENTER)
        users_popup = \
            self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div div._abm4 a.x1i10hfl")))[0]
        users_popup.click()

        user_followers = \
            self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.xieb3on li.x2pgyrj a._a6hd")))[
                1].click()

        # followers = self.wait.until(EC.visibility_of_element_located((By.XPATH, )))
        # followers.click()

    def follow(self):
        scrollable_popup = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._aano")))

        for i in range(5):
            user_following = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="f1814aafaa1752c"]/button/div/div')))
            for users in user_following:
                users.click()
                time.sleep(2)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)
        # except NoSuchElementException:
        #     cancel_unfollow = self.wait.until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "div._a9-z button._a9_1")))
        #     cancel_unfollow.click()
        self.driver.switch_to.default_content()

instagram = InstaFollower()
instagram.login()
instagram.find_following()
instagram.follow()
