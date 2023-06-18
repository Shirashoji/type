import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_binary


print('サイトを選択してください\n1: 英語入力\n2: ホームポジション\n3: 日本語入力')
category = int(input('番号を入力してください: '))
print('時間は1~5分です.')
type_time = int(input('時間を入力してください(単位は分): ')) - 1

# サイト
if category == 1:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'
elif category == 2:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/homeposition.html'
elif category == 3:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html'
else:
    website = 'https://manabi.benesse.ne.jp/gakushu/typing/eigonyuryoku.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)

driver.maximize_window()

# スタートってとこ
driver.find_element(By.ID, 'goSettingButton').click()

# 3分のところを押す(他の分数は座標のためなし)
driver.find_element(By.ID, 'timeLimitButton').click()

# 時間調整
for i in range(4-type_time):
    driver.find_element(By.ID, 'timeLimitButton').send_keys(Keys.LEFT)

# タイピングを開始する
driver.find_element(By.CLASS_NAME, 'typingButton').click()

# 見やすくするだけ
time.sleep(0.5)

# "space"キーでスタート
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)

# 3秒後にスタート(3 2 1)
time.sleep(3)

while True:
    driver.find_element(By.TAG_NAME, "body").send_keys(
        driver.find_element(By.ID, 'remaining').text.replace("'", "&"))
