import TM_COEFF_NORMED
import cv2, selenium

from selenium import webdriver

#set the driver for chrome
driver=webdriver.Chrome("C:\Users\myher\Downloads\chromedriver_win32\chromedriver.exe")
#set the windows size as full
dx, dy = driver.execute_script("var w=window; return [w.outerWidth - w.innerWidth, w.outerHeight - w.innerHeight];")
driver.set_window_size(1920 + dx, 1080 + dy)
#set the URL to screenshot
driver.get("http://www.google.com")
#save the screenshot as png file
driver.save_screenshot('google.png')
#calls the template Matching algorithm to match the button images
TM_COEFF_NORMED.templateMatchingTM_COEFF_NORMED(0.85,'google.png','searchBar.png')




#exit the browser page opened
driver.quit()

