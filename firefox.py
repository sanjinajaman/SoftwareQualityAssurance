import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.firefox.service import Service as Firefoxservice

#from webdriver_manager.chrome import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

#driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
#driver.get()
driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
driver.maximize_window()
print(driver.title)
#work on drop down
#obj=Select(driver.find_element(By.NAME,"name"))
#obj.select_by_index(1)
#obj.select_by_value("admin")
#obj.select_by_visible_text("Customer")
time.sleep(20)