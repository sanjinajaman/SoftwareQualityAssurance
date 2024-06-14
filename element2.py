import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

driver.get("https://google.com")
img=driver.find_element(By.XPATH,"//a[@class='gb_E']")
img.send_keys("xyz")
time.sleep(20)


# driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
# driver.find_element(By.LINK_TEXT,"LogIn Now").send_keys("xyz")
#
# time.sleep(20)
# driver.close()