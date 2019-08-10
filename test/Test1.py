from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\blher\MyProjects\FirstSeleniumTest\drivers\chromedriver.exe")
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("http://google.com")
# name of Google Search bar is "q"
driver.find_element_by_name("q").send_keys("Lebron James")

# name of Google Search button is "btnK"
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
