import pyautogui as pyautogui
#print (pyautogui.size())
screenWidth, screenHeight = pyautogui.size() 
pyautogui.moveTo(203, 316)

i = 0
a = 'y'

while a == 'y':
    i = 0
    while i < 20:
        i+=1
        r = pyautogui.locateCenterOnScreen
        #print(r)
        if r is not None:
            x = r[0]
            y = r[1]
            
            pyautogui.click(x/2,y/2)
        
        r = list(pyautogui.locateAllOnScreen
        if len(r) != 0:
            x = r[-1][0]
            y = r[-1][1]
            pyautogui.moveTo(x,y, duration= 0.1)
            pyautogui.click()