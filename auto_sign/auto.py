from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome('D:\\chrome_driver\\chromedriver.exe')
driver.maximize_window()
driver.get('http://hmgr.sec.lit.edu.cn/web/#/login')

name_input=driver.find_elements_by_xpath("//html/body/div[1]/div/div/div/div[1]/div[2]/div/input")
pwd_input=driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/input")
click_btn=driver.find_element_by_xpath("/html/body/div[1]/div/div/button")

name_input[0].send_keys("B20041230")
pwd_input[0].send_keys("qaz123")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             e
click_btn.click()

time.sleep(3000)

btn=driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/div[1]/div[2]/li[1]/div[1]")
print(driver.page_source)
# ActionChains(driver).context_click(btn).perform()
driver.quit() 
