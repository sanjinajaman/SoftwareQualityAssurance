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
#fetch title
print(driver.title)

#fetch url

print(driver.current_url)
#fetch page HTML source code
print("**************************************************************")

print(driver.page_source)

time.sleep(20)
driver.close()
driver.quit()
print("Done")





