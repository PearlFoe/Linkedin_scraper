from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def get_email_password():
	email = input('Email: ')
	password = input('Password: ')

	return(email, password)

def page_has_loaded(driver):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

def scroll_to_bottom(driver):
	try:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	except Exception:
		print(Exception)

def login(driver, email=None, password=None):
	if not email or not password:
		email, password = get_email_password()

	actions = ActionChains(driver)
	driver.get("https://www.linkedin.com/login")
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

	element = driver.find_element_by_id("username")
	actions.move_to_element(element).perform()
	actions.click(element).perform()
	driver.find_element_by_id("username").send_keys(email)

	element = driver.find_element_by_id("password")
	actions.move_to_element(element).perform()
	actions.click(element).perform()
	driver.find_element_by_id("password").send_keys(password)

	element = driver.find_element_by_tag_name("button")
	actions.move_to_element(element).perform()
	actions.click(element).perform()

	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
