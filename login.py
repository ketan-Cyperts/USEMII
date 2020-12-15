from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver")
driver.get("http://13.235.113.235:4200/")
driver.maximize_window()
print(driver.title)
driver.find_element_by_xpath("//input[@formcontrolname='username']").send_keys("AF-FAR775PANDI.0")
driver.find_element_by_xpath("//input[@formcontrolname='password']").send_keys("Rathods#07")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("//*[contains(text(),'Owner']").click()
#//*[contains(text(),'here')]