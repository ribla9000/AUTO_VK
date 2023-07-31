from core.settings import start
import random
import time
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class VKRepository:
    
    @staticmethod
    def run_browser(profile: str = "Profile 1", proxy: bool = False):
        browser = start(profile, proxy)
        browser.get("https://google.com/")
        time.sleep(2)
        browser.execute_script("window.open('https://vk.com/feed')")
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(2)
        return browser

    @staticmethod
    def open_friends(browser: Chrome):
        time.sleep(5)
        friends = browser.find_element(By.XPATH, '/html/body/div[11]/div/div/div[2]/div[1]/div/div[1]/div/div/nav/ol/li[5]/a')
        friends.click()
        time.sleep(2)
        return browser
        
    @staticmethod
    def get_count_friends(browser: Chrome):
        friends_value = browser.find_element(By.XPATH, "/html/body/div[11]/div/div/div[2]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[1]/h2[1]/ul/li[1]/a/span[2]")
        return friends_value.text
        
    @staticmethod
    def get_friends(browser: Chrome, value: int):
        friends_box = {
            "friends":
                [],
            "count": value,
        }
        friends_list = browser.find_elements(By.CLASS_NAME, 'friends_user_row')
        id = 0
        for _friend in friends_list:
            id += 1
            friend = _friend.find_element(By.CLASS_NAME, "friends_field_title")
            friend_name = friend.text
            data = {"id": id, "browser_object": _friend, "name": friend_name}
            friends_box['friends'].append(data)
        time.sleep(2)
        return friends_box
    
    @staticmethod
    def scroll_page_down(browser: Chrome, friends_count: int = 20):
        for i in range(friends_count//4 + 1):
            html = browser.find_element(By.TAG_NAME, 'html')
            html.send_keys(Keys.PAGE_DOWN)
        return
    
    @staticmethod
    def choose_friend(browser: Chrome, friend_box: dict, friend_id: int):
        friend_name = ""
        for friend_in_box in friend_box["friends"]:
            if friend_in_box["id"] == friend_id:
                link = friend_in_box["browser_object"].find_element(By.TAG_NAME, "a")
                browser.get(link.get_attribute("href"))
                friend_name += friend_in_box["name"]
        return friend_name
    
    @staticmethod
    def get_profiles():
        profiles = []
        for profile in os.listdir(os.path.join("user_data/")):
            if "_" in profile[0]:
                profiles.append(profile)
        return profiles
    
    @staticmethod
    def is_authorized(browser: Chrome):
        if "login" in browser.current_url:
            return False
        return True
    
    @staticmethod
    def vk_login(browser: Chrome, login: str = "375297760462", password: str = "13123851"):
        time.sleep(3)
        login_bar = browser.find_element(By.XPATH, "/html/body/div[10]/div/div/div[2]/div[2]/div[3]/div/div[1]/form/input[1]")
        for i in login:
            login_bar.send_keys(i)
            time.sleep(random.uniform(0.113, 0.311))
        time.sleep(1)
        submit_btn = browser.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/div[2]/div[3]/div/div[1]/form/button")
        submit_btn.click()
        time.sleep(2)
        login_wid_password = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div/button[2]")
        login_wid_password.click()
        time.sleep(2)
        password_bar = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input")
        for j in password:
            password_bar.send_keys(j)
            time.sleep(random.uniform(0.113, 0.311))
        time.sleep(1)
        continue_btn = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/button")
        continue_btn.click()
        return browser
        
            
    