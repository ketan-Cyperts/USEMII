from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver")
driver.get("http://13.235.113.235:4200/")
driver.maximize_window()
print(driver.title)
wait = WebDriverWait(driver, 10)
driver.find_element_by_xpath("//input[@formcontrolname='username']").send_keys("AF-FAR775PANDI.0")
driver.find_element_by_xpath("//input[@formcontrolname='password']").send_keys("Rathods#07")
driver.find_element_by_xpath("//button[@type='submit']").click()
# driver.find_element_by_xpath("//*[contains(text(),'Owner')]").click()#Owner
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Branch Manager')]")))
driver.find_element_by_xpath("//*[contains(text(),'Branch Manager')]").click()  # Branch Manager
# driver.find_element_by_xpath("//input[@formcontrolname='username']").send_keys("AF-FAR3341ARA.JAD")#Owner
driver.find_element_by_xpath("//input[@formcontrolname='username']").send_keys("AF-FAR6750SMI.PAN")  # Branch Manager
driver.find_element_by_xpath("//input[@formcontrolname='password']").send_keys("Rathods#07")
driver.find_element_by_xpath("//button[@type='submit']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Pin']")))
driver.find_element_by_xpath("//input[@placeholder='Enter Pin']").send_keys("123456")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-round btn-block btn-success']")))
driver.find_element_by_xpath("//button[@class='btn btn-round btn-block btn-success']").click()
# driver.find_element_by_xpath(By.XPATH("//button[@class='btn btn-round btn-block btn-success']"))
# driver.find_element_by_class_name("btn btn-round btn-block btn-success").click()
# driver.find_element_by_class_name("").click()
print("Login Successful to business user")
# wait.until(EC.element_to_be_clickable((By.ID, "dropdownBasic1")))
# sleep(3)
# #wait.until(EC.NoAlertPresentException)
# #wait.until(EC.visibility_of_element_located((By.ID, "dropdownBasic1")))
# driver.find_element_by_id("dropdownBasic1").click()
# driver.find_element_by_xpath("//*[contains(text(),'Logout')]").click()
#print("LogOut Successful")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'User Profile']")))
driver.find_element_by_xpath("//*[contains(text(),'User Profile']").click()
#"https://stackoverflow.com/questions/31643418/raise-timeoutexceptionmessage-screen-stacktrace-timeoutexception-message"