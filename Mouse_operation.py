import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chromeservice

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
driver.get("https://google.com")

#driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
act=ActionChains(driver)
#act.click().perform() #left click
#act.context_click().perform() #right click
act.click(driver.find_element(By.XPATH, ("//a[@text='YouTube']"))).perform()
#act.double_click().perform()
#act.double_click(driver.find_element(By.XPATH("//a[text()='Login']"))).perform() #for double click
time.sleep(20)