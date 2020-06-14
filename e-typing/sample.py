import type, time


type.browser_setting('tor')
type.create_account_with_mail(Mail_address="keroro-gunso@fanclub.pm",User_Name="ケロロ軍曹@ぁ〜ん")
#type.login('めあど',"pass")
wait_time = 0.08
#type.typing_first(WAIT_SECOND = wait_time, ranking='on')
for _ in range(80):
    wait_time -= 0.0005
    type.typing(WAIT_SECOND = wait_time, ranking='on')
    time.sleep(5)
    type.driver.get('https://www.e-typing.ne.jp/signup/signup.asp')
type.driver.quit()
