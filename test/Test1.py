from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\blher\MyProjects\FirstSeleniumTest\drivers\chromedriver.exe")
driver = webdriver.Firefox()
driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Lebron James")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()
