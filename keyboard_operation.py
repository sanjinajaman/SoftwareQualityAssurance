import time
from selenium import webdriver
from selenium.webdriver import Keys #for special key
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chromeservice

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains #normall key


driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
driver.get("https://google.com")

#driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
googleSearchBox=driver.find_element(By.ID,"APjFqb" )
googleSearchBox.send_keys("Automation")
act=ActionChains(googleSearchBox)
#act.send_keys(Keys.TAB).perform()
act.key_down((Keys.CONTROL).send_keys('a').perform()) #single key
#act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform() #multiple key or combination
time.sleep(20)