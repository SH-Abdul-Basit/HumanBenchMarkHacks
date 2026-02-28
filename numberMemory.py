import time
import mss
import mss.tools
from PIL import Image, ImageOps
# import cv2
import pytesseract
import pyautogui

x = 0
y = 450
w = 1900
h = 210

time.sleep(2)
while True:
    time.sleep(0.05)
    with mss.mss() as sct:
        region = {"top": y, "left": x, "width": w, "height": h}
        screenshot = sct.grab(region)

        # Save to file
        output = "number.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=output)


    number_image = Image.open("number.png")

    config = r'--psm 6 -c tessedit_char_whitelist=0123456789' # custom uniform block of numbers

    number_text = pytesseract.image_to_string(number_image, config=config)
    #number_text = number_text.replace("\n", "")

    print(number_text)

    if number_text.strip():
        time.sleep(1)

        pyautogui.write(number_text)

        pyautogui.press('enter')
    else:
        break

    #  break

