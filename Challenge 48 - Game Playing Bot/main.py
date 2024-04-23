import schedule
import time
from selenium.webdriver.common.by import By
from game_functions import GameFunctions

new_game = GameFunctions()

new_game.driver.get('http://orteil.dashnet.org/experiments/cookie/')

new_game.check_store()

cookie = new_game.driver.find_element(By.ID, value='cookie')

game_continues = True

minutes = 5
abort_after = minutes * 60
start = time.time()

while game_continues:

    delta = time.time() - start
    if delta >= abort_after:
        game_continues = False

    cookie.click()
    new_game.scheduler()
    new_game.check_store()


