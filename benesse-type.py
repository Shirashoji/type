#モジュール
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


#モードと時間を選択
print('モードを選択してください\n1: 英語入力\n2: ホームポジション\n3: 日本語入力')
category = int(input('番号を入力してください: '))
print('時間は1~5分です.')
type_time = int(input('時間を入力してください(単位は分): ')) -1

#サイト（モード）を入力を元に選択
if category == 1:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'
elif category == 2:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/homeposition.html'
elif category == 3:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html'
else:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'


#Chromeの設定・起動
chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);
driver.get(website)

driver.maximize_window()

#「スタート」を押す
driver.find_element_by_id('goSettingButton').click()

#3分のところを押す(他の分は座標のためなし)
driver.find_element_by_id('timeLimitProgress').click()
#2回左キー 1分のとこ
for i in range(2):
    pyautogui.hotkey('left')

#質問した時間に移動（入力された時間から-1に移動）
for i in range(type_time):
    pyautogui.hotkey('right')

#タイピングを開始する
driver.find_element_by_class_name('typingButton').click()

#見やすくするだけ
time.sleep(0.5)

#"space"キーでスタート
driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

#3秒後にスタート(3 2 1)
time.sleep(3)

#繰り返し
while True:
    driver.find_element_by_tag_name("body").send_keys(driver.find_element_by_id('remaining').text)
    #要素（remaining）の取得と入力（body）
