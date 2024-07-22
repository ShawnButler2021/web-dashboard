import project_funcs as pf
import pyautogui as pag
import os
import time
from selenium import webdriver
from datetime import datetime




path = os.getcwd() + '\\webpage\\index.html'
path = path.replace('\\','/')
flag = 0


# application loop
while True:
	if ( datetime.now().hour == 7 and flag == 0 ) or ( datetime.now().hour == 20 and flag == 0 ):
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(path)
		pag.press('f11')
		time.sleep(3600)
		driver.close()
		flag = 1
	elif ( datetime.now().hour != 7 and flag == 1 ) or ( datetime.now().hour != 20 and flag == 1 ):
		flag = 0

	else:
		print('running...')
		time.sleep(60)


	