import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
#work on checkbox
#driver.find_element(By.XPATH,"//input[@class='checkbox']").click()
#work on button
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
#work on link

#driver.find_element(By.LINK_TEXT,"LogIn Now").click()


time.sleep(20)