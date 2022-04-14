from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = Chrome('./chromedriver')
driver.get("https://developer.riotgames.com/")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"osano-cm-accept-all"))).click()
driver.find_element(By.CLASS_NAME, "admin-title").click()
driver.find_element(By.NAME, "username").send_keys("ezioo77")
driver.find_element(By.NAME, "password").send_keys("polska100")
driver.find_element(By.CLASS_NAME, "mobile-button").click()
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "apikey_show"))).click()

menu = driver.find_element(By.NAME, "confirm_action")
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.move_by_offset(0, -60)
actions.click()
actions.perform()
driver.implicitly_wait(3)
#actions = ActionChains(driver)
#actions.move_by_offset(10, 60)
#actions.context_click()
#actions.perform()

#todo: przklikanie recpatcha audio

driver.find_element(By.NAME, "confirm_action").click()
print(driver.find_element(By.ID, "apikey").text)
#%%
