#from selenium.webdriver import Chrome
# path="C:\\Users\\user\\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)
# driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver import Chrome
#path="C:\\Users\\user\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
# driver=Chrome(executable_path=path)
#river=Chrome(executable_path=path)
#driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
driver.get("https://google.com")
driver.maximize_wi

ndow()
time.sleep(20)
driver.close()
driver.quit()
print("Done")






