import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


print('サイトを選択してください\n1: 英語入力\n2: ホームポジション\n3: 日本語入力')
category = int(input('番号を入力してください: '))
print('時間は1~5分です.')
type_time = int(input('時間を入力してください(単位は分): ')) -1

#サイトを判別
if category == 1:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'
elif category == 2:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/homeposition.html'
elif category == 3:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html'
else:#その他はとりあえず英語で実行
    print("1,2,3以外の数字（文字）が入力されました。なので英語で実行します。")
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'

#Chromeを開く部分
chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);#「自動テストソフトソフトウェアによって制御されています」を非表示にする。
driver = webdriver.Chrome(options=chrome_options);
driver.get(website)

driver.maximize_window()

#スタートってとこを押す
driver.find_element_by_id('goSettingButton').click()

#3分のところを押す(他の分数は座標のためなし)
driver.find_element_by_id('timeLimitProgress').click()

#3回左キー 1分のとこ
for i in range(3):
    pyautogui.hotkey('left')
#そこから選ばれた回数文移動。
for i in range(type_time):
    pyautogui.hotkey('right')

#タイピングを開始する。
driver.find_element_by_class_name('typingButton').click()

#サイトを少し長く表示し見やすくする。
time.sleep(0.5)

#"space"キーでスタート
driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

#3秒後にスタート(3 2 1)
time.sleep(3)

while True:
    driver.find_element_by_tag_name("body").send_keys(driver.find_element_by_id('remaining').text)#自動タイピング
