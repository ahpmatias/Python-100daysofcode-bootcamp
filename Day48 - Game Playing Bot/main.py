from selenium import webdriver
from selenium.webdriver.common.by import By
from game_functions import GameFunctions
import time
import threading

new_game = GameFunctions()

new_game.driver.get('http://orteil.dashnet.org/experiments/cookie/')

new_game.check_store()

cookie = new_game.driver.find_element(By.ID, value='cookie')

game_continues = True

minutes = 5
abort_after = 20
start = time.time()



while game_continues:

    # delta = time.time() - start
    # if delta >= abort_after:
    #     game_continues = False

    cookie.click()
    check_store_thread = threading.Timer(5, new_game.check_store())
    check_store_thread.start()