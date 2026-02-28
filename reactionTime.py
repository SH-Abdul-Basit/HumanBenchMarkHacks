# Green #4bdb6a
# Red #ce2636
# Blue #2b87d1
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import mss
import mss.tools
import cv2 as cv
import pyautogui
import numpy as np
import time

# from selenium.webdriver.common.by import By
# BLUE = (43, 135, 209)
# B G R
GREEN = np.array([106, 219, 75])
RED = np.array([54, 38, 206])

URL = "https://humanbenchmark.com/tests/reactiontime"

# firefox_options = Options()
# firefox_options.page_load_strategy = "eager"
# firefox_options.set_preference("permissions.default.image", 2)
#
# driver = webdriver.Firefox(options=firefox_options)
#
#
# driver.fullscreen_window()
#
# driver.get(URL)
#
# driver.implicitly_wait(1)

color_x = 150
color_y = 180

click_x = 170
click_y = 200

# Always click once to start the game
pyautogui.click(click_x, click_y)

time.sleep(2)

# Taking the screenshot
region = {"top": 100, "left": 0, "width": 210, "height": 210}

while True:
    with mss.mss() as sct:
        screenshot = sct.grab(region)

        mss.tools.to_png(screenshot.rgb, screenshot.size, output="screenshot.png")

    img = cv.imread("screenshot.png")

    color = img[color_y, color_x]

    if np.array_equal(color, GREEN):
        pyautogui.click(click_x, click_y)

#driver.quit()


