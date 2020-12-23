import pyautogui
import time

# 참고!!!! chrome 100% 기준이다 이거야

c=0
while c<50:

    time.sleep(3)
    # 내려받기 클릭
    pyautogui.click(1490,639)
    time.sleep(0)
    pyautogui.click(1490,787)
    # late download 클릭
    pyautogui.click(1490,823)

    # 다음 강의 클릭
    pyautogui.click(1490,873)
    time.sleep(5)

    pyautogui.click(42,339)
    time.sleep(3)

    pyautogui.click(42,427)
    time.sleep(5)


    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')

    time.sleep(0)

    c+=1