import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")

#work on drop down
obj=Select(driver.find_element(By.NAME,"name"))
obj.select_by_index(1)










