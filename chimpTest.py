from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://humanbenchmark.com/tests/chimp"

driver = webdriver.Firefox()

driver.fullscreen_window()

def play_game():

    while True:
        button = driver.find_element(By.CLASS_NAME, "css-1bnidmp")
        button.click()

        num_blocks = driver.find_elements(By.CLASS_NAME, "css-qicd9u")
        sorted_num_blocks = sorted(num_blocks, key=lambda x: int(x.text))

        for number in sorted_num_blocks:
            number.click()


driver.get(URL)

driver.implicitly_wait(1)

try:
    play_game()
except Exception as e:
    print(f"Error: {e}")


driver.quit()





