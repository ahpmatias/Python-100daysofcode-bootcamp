from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&locatio'
                  'n=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

driver.maximize_window()
time.sleep(2)
reject_cookie = driver.find_element(By.CSS_SELECTOR, 'button[action-type="DENY"]')
reject_cookie.click()

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

time.sleep(2)
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(PASSWORD)

sign_in = driver.find_element(By.CSS_SELECTOR, 'button[type=Submit]')
sign_in.click()

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&locatio'
                  'n=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

for number in range(1,5):
    time.sleep(10)
    listed_job = driver.find_element(By.CSS_SELECTOR, f'.job-card-list[{number}]')
    listed_job.click()
    save_button = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    save_button.click()




