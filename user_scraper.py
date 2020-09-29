from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Person(object):
	"""docstring for Person"""
	def __init__(self, url, driver):
		self.url = url
		
		if url is not None:
			try:
				driver.get(self.url)
			except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
		else:
			print(f'None type url')

		self.driver = driver


	def get_name(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
											(By.XPATH, '//li[@class="inline t-24 t-black t-normal break-words"]')))
			name = driver.find_element_by_xpath(
											'//*[@class="inline t-24 t-black t-normal break-words"]').text
			return name
		except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
				return ''

	def get_position(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
												(By.XPATH, '//*[@class="mt1 t-18 t-black t-normal break-words"]')))
			position = driver.find_element_by_xpath(
												'//*[@class="mt1 t-18 t-black t-normal break-words"]').text
			return position
		except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
				return ''

	def get_company_name(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
													(By.ID, 'ember102')))
			company_name = driver.find_element_by_id(
													'ember102').text
			return company_name
		except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
				return ''

	def get_region(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
												(By.XPATH, '//*[@class="t-16 t-black t-normal inline-block"]')))
			region = driver.find_element_by_xpath(
												'//*[@class="t-16 t-black t-normal inline-block"]').text
			return region
		except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
				return ''

	def get_photo(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'ember68')))
			photo = driver.find_element_by_xpath('//*[@id="ember68"]/img').get_attribute('src')
			if 'http' not in photo:
				return '-'
			else:
				return photo
		except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
				return ''

	def get_education(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
												(By.XPATH, '//*[@class="top-card-link__description"]')))
			education = driver.find_element_by_xpath(
												'//*[@class="top-card-link__description"]').text
			return education
		except Exception:
				template = "An exception of type {0} occurred. Arguments:\n{1}"
				message = template.format(type(Exception).__name__, Exception.args)
				print(message)
				return ''

