#必要なモジュールをインポートする。
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


driver = webdriver.Chrome()  #Chromeを開く

driver.get("https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html")  #ベネッセのタイピングサイトを開く

pyautogui.hotkey('command', 'ctrl', 'f')  #Chromeの大画面化
driver.find_element_by_id('goSettingButton').click()  #「スタート」を押す

#タイピング練習時間のスライダーを1分に設定する。
driver.find_element_by_id('timeLimitProgress').click()  #3分のところを押す(他の分は押せないため)。
for _ in range(2): #2回繰り返す。
    pyautogui.hotkey('left')  # 左キーを押す。

driver.find_element_by_class_name('typingButton').click()  #「タイピングを開始する」を押す。

#"space"キーでスタート PyAutoGUIでスペースキーを押す。
pyautogui.hotkey('space')

#3秒後にスタート 3秒間待つ
time.sleep(3)

#入力をする部分
while True: #繰り返し
    typetext = driver.find_element_by_id('remaining').text #上に表示される文字
    pyautogui.typewrite(typetext) #PyAutoGUIによる入力
