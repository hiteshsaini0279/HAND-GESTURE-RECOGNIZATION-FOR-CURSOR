import pyautogui
import numpy as np
import math
import time

pyautogui.FAILSAFE = False   # Disable corner emergency stop

class CursorController:
    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()

    def mapToScreen(self, x, y, cam_w, cam_h):
        screen_x = np.interp(x, (0, cam_w), (0, self.screen_w))
        screen_y = np.interp(y, (0, cam_h), (0, self.screen_h))
        return screen_x, screen_y

    def move(self, x, y):
        pyautogui.moveTo(x, y)

    def distance(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def click_if_needed(self, d):
        if d < 30:
            pyautogui.click()
            time.sleep(0.2)
