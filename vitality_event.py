# https://www.powerofvitality.com/v3/employee-portal/home/activities/Wellbeing/Fitness%20activities?activityType=Fitness%20activities


#https://www.powerofvitality.com/v3/employee-portal/home/activities/Wellbeing/Fitness%20activities?activityType=Fitness%20activities

# css selector
# button.w-full

#crhome driver location
#C:\Users\kmarx-levi\chromedriver_win32

# from selenium.webdriver import Chrome
# from selenium.webdriver.chromium.options import ChromiumOptions
# opts = ChromiumOptions()
# opts.set_headless()
# assert opts.headless
# browser = Chrome(options=opts)
# browser.get('https://duckduckgo.com')

from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(
options=options)


driver.get("https://www.powerofvitality.com/v3/employee-portal/home/activities/Wellbeing/Fitness%20activities?activityType=Fitness%20activities")
driver.implicitly_wait(15)

username = driver.find_element(By.NAME, "username")
username.send_keys("bminagutierrez")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


password = driver.find_element(By.NAME, "password")
password.send_keys("Number161718!")


submit_button = driver.find_element(By.ID, "okta-signin-submit")
submit_button.click()
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
driver.quit()