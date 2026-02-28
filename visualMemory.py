import pyautogui as pag
import keyboard
import time
import mss
import mss.tools
import cv2 as cv
import numpy as np

WHITE = np.array([255, 255, 255])

x_start = 700
y_start = 320
width = 520
height = 520

while True:
    time.sleep(0.5)

    if keyboard.is_pressed('q'):
        break

    with mss.mss() as sct:
        region = {"top": y_start, "left": x_start, "width": width, "height": height}
        #region = {"top": y_start, "left": x_start, "width": width, "height": 415}
        screenshot = sct.grab(region)

        # Save to file
        output = "grid.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=output)

    grid_img = cv.imread('grid.png')

    grid_gray_img = cv.cvtColor(grid_img, cv.COLOR_BGR2GRAY)

    _, binary_image = cv.threshold(grid_gray_img, 128, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    contours, _ = cv.findContours(binary_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cells = []
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)

        area = cv.contourArea(cnt)

        # Filter by area and aspect ratio to identify cells
        aspect_ratio = w / h
        if 0.5 < aspect_ratio < 2.0 and area > 500:  # Tune these thresholds
            cells.append((x, y, w, h))

    click_positions = []
    for cell in cells:
        x, y, w, h = cell
        center_x = x + int(w / 2)
        center_y = y + int(h / 2)
        color = grid_img[center_y, center_x]
        if np.array_equal(color, WHITE):
            click_positions.append([x_start + center_x, y_start + center_y])

    time.sleep(1)
    for pos in click_positions:
        pag.click(pos[0], pos[1])

