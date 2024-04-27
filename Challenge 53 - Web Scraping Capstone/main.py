import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

GOOGLE_FORM_LINK = os.environ.get('GOOGLE_FORM_LINK')
GOOGLE_FORM_RESPONSES_LINK = os.environ.get('GOOGLE_FORM_RESPONSES_LINK')
ZILLOW_WEBSITE = 'https://appbrewery.github.io/Zillow-Clone/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

response = requests.get(ZILLOW_WEBSITE)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

address_results = [listing.getText() for listing in soup.select('div a address')]

addresses = []
for item in address_results:
    addresses.append(item.strip())

links = [link.get('href') for link in soup.select('.property-card-link')]
price_results = [price.getText() for price in soup.select('.PropertyCardWrapper__StyledPriceLine')]

prices = []
for price in price_results:
    if '+' in price:
        price = price.split('+')
        price = price[0]
        prices.append(price)
    if '/' in price:
        price = price.split('/')
        price = price[0]
        prices.append(price)

for number in range(0, len(addresses)):
    driver.get(GOOGLE_FORM_LINK)
    driver.maximize_window()

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div'
                                                  '[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div'
                                                '[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
                                               'div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.click()
    address_input.send_keys(addresses[number])
    price_input.click()
    price_input.send_keys(prices[number])
    link_input.click()
    link_input.send_keys(links[number])
    submit_button.click()