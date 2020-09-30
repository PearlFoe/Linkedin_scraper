from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Person(object):
	"""docstring for Person"""
	def __init__(self, url, driver):
		self.url = url
		
		if url is not None:
			try:
				driver.get(self.url)
			except Exception:
				print('Url error')
		else:
			print('None url')

		self.driver = driver


	def get_name(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
											(By.XPATH, '//li[@class="inline t-24 t-black t-normal break-words"]')))
			name = driver.find_element_by_xpath(
											'//*[@class="inline t-24 t-black t-normal break-words"]').text
			return name
		except Exception:
			return ''

	def get_position(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
												(By.XPATH, '//*[@class="mt1 t-18 t-black t-normal break-words"]')))
			position = driver.find_element_by_xpath(
												'//*[@class="mt1 t-18 t-black t-normal break-words"]').text
			return position
		except Exception:
			return ''
	'''
	def get_company_name(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
													(By.ID, 'ember101')))
			company_name = driver.find_element_by_id(
													'ember101').text
			return company_name
		except Exception:
			try:
				company_name = driver.find_element_by_xpath(
													'//*[class="mt1 t-18 t-black t-normal break-words"]').text
				return company_name
			except Exception:
				return ''
	'''

	def get_region(self):
		driver = self.driver
		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
												(By.XPATH, '//*[@class="t-16 t-black t-normal inline-block"]')))
			region = driver.find_element_by_xpath(
												'//*[@class="t-16 t-black t-normal inline-block"]').text
			return region
		except Exception:
			return ''

	def get_photo(self):
		driver = self.driver
		actions = ActionChains(driver)
		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'ember68')))
			actions.pause(0.5).perform()
			photo = driver.find_element_by_xpath('//*[@id="ember68"]/img').get_attribute('src')
			if 'http' not in photo:
				return '-'
			else:
				return photo
		except Exception:
			return ''

	def get_education(self):
		driver = self.driver
		education = dict()
		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
												(By.ID, 'education-section')))
			education_place = driver.find_elements_by_xpath(
												'//*[@class="pv-entity__summary-info pv-entity__summary-info--background-section"]')
			for place in education_place:
				education_place = place.find_element_by_xpath('//*[@class="pv-entity__degree-info"]').find_elements_by_tag_name('h3').text

				professions = driver.find_element_by_xpath(
													'//*[@class="pv-entity__degree-info"]').find_elements_by_tag_name('p')

				education[education_place] = [prof.find_element_by_class_name('pv-entity__comma-item').text for prof in professions]

			return education
		except Exception:
			return ''



'''		try:
			_ = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
												(By.XPATH, '//*[@class="pv-entity__school-name t-16 t-black t-bold"]')))
			education_place = driver.find_element_by_xpath(
												'//*[@class="pv-entity__school-name t-16 t-black t-bold"]').text

			education['education_place'] = education_place
			professions = driver.find_element_by_xpath(
												'//*[@class="pv-entity__degree-info"]').find_elements_by_tag_name('p')

			education['profession'] = [prof.find_element_by_class_name('pv-entity__comma-item').text for prof in professions]

			return education
		except Exception:
			return ''
'''