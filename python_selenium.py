from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("http://www.google.com")
print(driver.title)
driver.quit()