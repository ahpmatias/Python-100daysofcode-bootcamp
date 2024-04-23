from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule


class GameFunctions:

    def __init__(self):
        self.STORE_IDS = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory',
                          'buyGrandma', 'buyCursor']
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.SECONDS = 5

    def get_store_values(self):
        buy_cursor = self.driver.find_element(By.CSS_SELECTOR, value='#buyCursor b').text
        buy_cursor = buy_cursor.split(' ')
        buy_cursor = int(buy_cursor[2])

        buy_grandma = self.driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b').text
        buy_grandma = int(buy_grandma.split(' ')[2])

        buy_factory = self.driver.find_element(By.CSS_SELECTOR, value='#buyFactory b').text
        buy_factory = int(buy_factory.split(' ')[2])

        buy_mine = self.driver.find_element(By.CSS_SELECTOR, value='#buyMine b').text
        buy_mine = buy_mine.split(' ')
        buy_mine = int(buy_mine[2].split(',')[0] + buy_mine[2].split(',')[1])

        buy_shipment = self.driver.find_element(By.CSS_SELECTOR, value='#buyShipment b').text
        buy_shipment = buy_shipment.split(' ')
        buy_shipment = int(buy_shipment[2].split(',')[0] + buy_shipment[2].split(',')[1])

        buy_lab = self.driver.find_element(By.CSS_SELECTOR, value='div[id="buyAlchemy lab"] b').text
        buy_lab = buy_lab.split(' ')
        buy_lab = int(buy_lab[3].split(',')[0] + buy_lab[3].split(',')[1])

        buy_portal = self.driver.find_element(By.CSS_SELECTOR, value='#buyPortal b').text
        buy_portal = buy_portal.split(' ')
        buy_portal = int(
            buy_portal[2].split(',')[0] + buy_portal[2].split(',')[1] + buy_portal[2].split(',')[2])

        buy_tmachine = self.driver.find_element(By.CSS_SELECTOR, value='div[id="buyTime machine"] b').text
        buy_tmachine = buy_tmachine.split(' ')
        buy_tmachine = int(buy_tmachine[3].split(',')[0] + buy_tmachine[3].split(',')[0] + buy_tmachine[3].split
        (',')[0])

        store_values = [buy_cursor, buy_grandma, buy_factory, buy_mine, buy_shipment, buy_lab, buy_portal,
                        buy_tmachine]
        return store_values

    def get_money_amount(self):
        money = self.driver.find_element(By.CSS_SELECTOR, value='#money').text

        if money == '0':
            return 0

        if ',' in money:
            money = money.split(' ')
            money = int(money[-1].split(',')[0] + money[-1].split(',')[1])
        else:
            money = money.split(' ')
            money = int(money[-1])

        return money

    def check_store(self):

        money = self.get_money_amount()
        store_values = self.get_store_values()
        store_values.reverse()

        for index, item in enumerate(store_values):

            if money > item:
                click_on = self.driver.find_element(By.CSS_SELECTOR, value=f'div[id="{self.STORE_IDS[index]}"]')
                click_on.click()

    def scheduler(self):
        schedule.every(self.SECONDS).seconds.do(job_func=self.check_store())
