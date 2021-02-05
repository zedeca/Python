from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


# USERNAME = " "     #YOUR TYPERACER ACCOUNT EMAIL-ID [OPTIONAL]
# PASSWORD = " "     #YOUR TYPERACER ACCOUNT PASSWORD [OPTIONAL]

PATH = " "         #YOUR CHROMEDRIVER PATH/ADDRESS IN YOUR DEVICE


TYPERACER_WEBSITE_URL = 'https://play.typeracer.com/?universe=accuracy'
driver = webdriver.Chrome(PATH)

def login():
    driver.implicitly_wait(10)
    # time.sleep(10)

    login_btn = driver.find_element_by_link_text('Sign In')
    login_btn.click()

    inp_username = driver.find_element_by_name('username')
    inp_username.send_keys(USERNAME)

    inp_password = driver.find_element_by_name('password')
    inp_password.send_keys(PASSWORD)
    inp_password.send_keys(Keys.RETURN)

def enter_match():
    # driver.implicitly_wait(10)
    time.sleep(2)
    enter_match_btn = driver.find_element_by_link_text("Enter a Typing Race")
    enter_match_btn.click()

def cheat():
    driver.implicitly_wait(20)
    
	paragraph = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')
    print(paragraph.text)

    inp_type = driver.find_element_by_class_name('txtInput')
    while True:
        try:
            for word in paragraph.text.split():
                
                if word != paragraph.text.split()[-1]:
                    inp_type.send_keys(word+' ')
                
                else: inp_type.send_keys(word)
                
                time.sleep(0.66)  #DECREASE THIS NUMBER TO INCREASE BOT'S TYPING SPEED
            break
            
        except: continue

def re_match():
    time.sleep(2)
    rematch_btn = driver.find_element_by_link_text('Race again')
    rematch_btn.click()
    time.sleep(5)

def main():
    
    #login()	# [OPTIONAL IF NO ACCOUNT]
    enter_match()
    
    while True:
      cheat()
      re_match()


if __name__ == '__main__':
    main()
