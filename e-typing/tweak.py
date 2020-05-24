import type, time

type.browser_setting('firefox')
type.login('@gmail.comとかのメール',"pass")
wait_time = 0.057
for _ in range(25):
    type.typing(WAIT_SECOND = wait_time, ranking='off')
    time.sleep(5)
    point = int(type.driver.find_element_by_class_name("data").get_attribute("textContent"))
    if 698 <= point <= 704:
        type.WebDriverWait(type.driver, 15).until(type.EC.presence_of_element_located((type.By.ID, 'regist_btn')))
        type.driver.find_element_by_id("regist_btn").click()
        try:
            type.WebDriverWait(type.driver, 15).until(type.EC.presence_of_element_located((type.By.ID, 'yesBtn')))
            type.driver.find_element_by_id("yesBtn").click()
        except:
            print('点数が高すぎるため登録不可能')
    type.driver.get('https://www.e-typing.ne.jp/signup/signup.asp')
type.driver.quit()
