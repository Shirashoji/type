import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


print('サイトを選択してください\n1: 英語入力\n2: ホームポジション\n3: 日本語入力')
category = int(input('番号を入力してください: '))
print('時間は1~5分です.')
type_time = int(input('時間を入力してください(単位は分): ')) -1

#サイト
if category == 1:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'
elif category == 2:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/homeposition.html'
elif category == 3:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html'
else:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);
#driver = webdriver.Chrome('/Users/rockmankun/Selenium/chromedriver')
driver.get(website)

driver.maximize_window()

if(driver.current_url==website):
    #スタートってとこ
    driver.find_element_by_id('goSettingButton').click()

    #3分のところを押す(他の分数は座標のためなし)
    driver.find_element_by_id('timeLimitProgress').click()
    #3回左キー 1分のとこ
    for i in range(3):
        pyautogui.hotkey('left')
    for i in range(type_time):
        pyautogui.hotkey('right')

    #タイピングを開始する
    driver.find_element_by_class_name('typingButton').click()

    #見やすくするだけ
    time.sleep(0.5)

    #"space"キーでスタート
    pyautogui.hotkey('space')

    #3秒後にスタート
    time.sleep(3)

    while True:
        typetext = driver.find_element_by_id('remaining').text #上に表示される文字
        pyautogui.typewrite(typetext) #PyAutoGUIによる入力
