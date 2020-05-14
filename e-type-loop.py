# -*- coding:utf-8 -*-

import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary

WAIT_SECOND = 5

website = 'https://www.e-typing.ne.jp/roma/check/'

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);

while True:
    try:
        driver = webdriver.Chrome(options=chrome_options);
        #ブラウザを開くところ
        driver.get(website)
        driver.maximize_window()


        time.sleep(5)
        driver.find_element_by_id("mail").send_keys("example@example.com") #各自変更
        driver.find_element_by_id("password").send_keys("example_password") #各自変更
        driver.find_element_by_id("login_btn").click()

        driver.find_element_by_xpath('//*[@id="level_check_member"]/a').click()
        time.sleep(2)
        driver.switch_to_frame('typing_content')
        driver.find_element_by_id("start_btn").click()
        time.sleep(1.5)
        pyautogui.hotkey('space')
        time.sleep(3)

        for i in range(0, 15):
            time.sleep(1.3)
            WebDriverWait(driver, WAIT_SECOND).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sentenceText"]/div/span[2]')))
            driver.find_element_by_tag_name("body").send_keys(driver.find_element_by_xpath('//*[@id="sentenceText"]/div/span[2]').text)
        time.sleep(10)
        driver.find_element_by_id("regist_btn").click()
        time.sleep(2)
        try:
            driver.find_element_by_id("yesBtn").click()
        except:
                print('登録に失敗しました')
        else:
                print('登録できました')
        time.sleep(10)
        driver.quit()
    except:
            print('登録に失敗しました')
    else:
            print('登録できました')
    finally:
            driver.quit()
