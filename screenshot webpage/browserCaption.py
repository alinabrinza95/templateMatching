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
#exit the browser page opened
driver.quit()