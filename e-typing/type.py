# -*- coding:utf-8 -*-

import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def browser_setting(Browser):
    global driver
    if Browser.lower()=='chrome':
        import chromedriver_binary
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        driver = webdriver.Chrome(options=chrome_options)
    elif Browser.lower()=='tor':
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('network.proxy.type', 1)
        firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
        firefox_profile.set_preference('network.proxy.socks_port', 9150)
        driver = webdriver.Firefox(firefox_profile=firefox_profile)
    elif Browser.lower()=='firefox':
        driver = webdriver.Firefox()
    elif Browser.lower()=='safari':
        driver = webdriver.Safari()
    else:
        print('Firefox, Tor, Safariの中から選択してください\n"Firefox" or "Tor" or "Safari"')

def login(Mail_address, Mail_password):
    driver.get('https://www.e-typing.ne.jp/')
    driver.maximize_window()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'mail')))
    driver.find_element_by_id("mail").send_keys(Mail_address)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id("password").send_keys(Mail_password)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'login_btn')))
    driver.find_element_by_id("login_btn").click()

def create_account():
    import random, string
    driver.get('https://www.e-typing.ne.jp/signup/signup.asp')
    driver.maximize_window()
    global Mail_address, Mail_password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'name')))
    driver.find_element_by_id("name").send_keys("tutsu☆jiji")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element_by_id("email").send_keys(Mail_address)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'email_re')))
    driver.find_element_by_id("email_re").send_keys(Mail_address)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'su_password')))
    driver.find_element_by_id("su_password").send_keys(Mail_password)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'target')))
    driver.find_element_by_id("target").send_keys("tutsu☆jiji")
    driver.execute_script("document.getElementById('regist_btn').scrollIntoView()")
    time.sleep(3)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'regist_btn')))
    driver.find_element_by_xpath("//button[@id='regist_btn']").click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'mh_btn')))
    driver.find_element_by_xpath("//img[@alt='会員ホームへ']").click()
    print('ログインのメールアドレス: '+Mail_address)
    print('ログインのパスワード: '+Mail_password)

def create_account_with_mail(Mail_address, Mail_password="pass",User_Name="NAMELESS"):
    import random, string
    driver.get('https://www.e-typing.ne.jp/signup/signup.asp')
    driver.maximize_window()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'name')))
    driver.find_element_by_id("name").send_keys(User_Name)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element_by_id("email").send_keys(Mail_address)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'email_re')))
    driver.find_element_by_id("email_re").send_keys(Mail_address)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'su_password')))
    driver.find_element_by_id("su_password").send_keys(Mail_password)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'target')))
    driver.find_element_by_id("target").send_keys("unknown user")
    driver.execute_script("document.getElementById('regist_btn').scrollIntoView()")
    time.sleep(3)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'regist_btn')))
    driver.find_element_by_xpath("//button[@id='regist_btn']").click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'mh_btn')))
    driver.find_element_by_xpath("//img[@alt='会員ホームへ']").click()
    print('ログインのメールアドレス: '+Mail_address)
    print('ログインのパスワード: '+Mail_password)


def typing(WAIT_SECOND = 0.03, ranking='off'):
    driver.get('https://www.e-typing.ne.jp/')
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="level_check_member"]/a')))
    driver.find_element_by_xpath('//*[@id="level_check_member"]/a').click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'typing_content')))
    driver.switch_to_frame('typing_content')
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'start_btn')))
    driver.find_element_by_id("start_btn").click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'start_msg')))
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
    time.sleep(3)
    for i in range(0, 15):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="sentenceText"]/div/span[2]''')))
        for key in driver.find_element_by_xpath('//*[@id="sentenceText"]/div/span[2]').text:
            driver.find_element_by_tag_name("body").send_keys(key)
            time.sleep(WAIT_SECOND)
    if ranking.lower() == 'on':
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'regist_btn')))
        driver.find_element_by_id("regist_btn").click()
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'yesBtn')))
            driver.find_element_by_id("yesBtn").click()
        except:
            print('点数が高すぎるため登録不可能')


def typing_first(WAIT_SECOND = 0.03, ranking='off'):
    driver.get('https://www.e-typing.ne.jp/')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="level_check_member"]/a')))
    driver.find_element_by_xpath('//*[@id="level_check_member"]/a').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'typing_content')))
    driver.switch_to_frame('typing_content')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'start_btn')))
    driver.find_element_by_id("start_btn").click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'start_msg')))
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
    time.sleep(3)
    for i in range(0, 12):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="sentenceText"]/div/span[2]''')))
        for key in driver.find_element_by_xpath('//*[@id="sentenceText"]/div/span[2]').text:
            driver.find_element_by_tag_name("body").send_keys(key)
            time.sleep(WAIT_SECOND)
    if ranking.lower() == 'on':
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'regist_btn')))
        driver.find_element_by_id("regist_btn").click()
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'yesBtn')))
            driver.find_element_by_id("yesBtn").click()
        except:
            print('点数が高すぎるため登録不可能')



if __name__ == '__main__':
    typing.browser_setting()
    typing.login()
    typing.typing()
