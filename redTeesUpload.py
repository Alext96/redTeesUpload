import pyautogui


def copyTee():
    # make sure copy is visible 110% zoom in chrome
    # click the cogwheel
    pyautogui.click(749, 1085, interval=0.5)
    # open new tabs
    for i in range(25):
        pyautogui.keyDown('ctrl')
        pyautogui.click(521, 1356, interval=0.5)
        pyautogui.keyUp('ctrl')
        i += 1
        # uploadshirts
    for x in range(25):
        # interval 3 on everything is stable
        # tab to next shirt
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        # scroll down
        pyautogui.click(2548, 339, interval=1)
        # press replace all images
        pyautogui.click(498, 723, interval=1)
        # left click pic
        pyautogui.click(400, 256, interval=3)
        # deletePic
        pyautogui.press('delete', interval=1)
        # pyautogui.press("enter", interval=3)
        # left click pic
        pyautogui.click(411, 255, interval=1)
        # confirm pic(press enter)
        pyautogui.press("enter", interval=5)
        x += 1


copyTee()
