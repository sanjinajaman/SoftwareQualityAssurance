import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
#driver.get("https://firefox.com")
driver.maximize_window()

print("**************************************************************")
#Fetching Element Text

print("Text on Link is : -"+driver.find_element(By.CLASS_NAME,"pra_1").text)
#Fetching Attribute value of element

#print("Value of Button is:- "+ driver.find_element(By.XPATH,"//button[@type='submit']").get_attribute("value"))

time.sleep(20)
driver.close()
driver.quit()
print("Done")





