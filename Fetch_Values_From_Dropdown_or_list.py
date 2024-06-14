import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
#driver.get("https://firefox.com")
driver.maximize_window()

print("**************************************************************")
#Fetching Element Text

#print("Text on Link is : -"+driver.find_element(By.CLASS_NAME,"pra_1").text)
#Fetching Attribute value of element

#print("Value of Button is:- "+ driver.find_element(By.XPATH,"//button[@type='submit']").get_attribute("value"))

#work on drop down
obj=Select(driver.find_element(By.NAME,"name"))
#obj.select_by_index(1)
#obj.select_by_value("admin")
#obj.select_by_visible_text("Customer")
print(obj.first_selected_option)

print(obj.first_selected_option.text)
print(obj.options)
for op in obj.options:
    print(op.text)
#print(obj.options)
time.sleep(20)
driver.close()
driver.quit()
print("Done")





