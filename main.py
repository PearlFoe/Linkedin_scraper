from selenium import webdriver
from user_scraper import Person
import actions
import config
import time

url = 'https://ru.linkedin.com/in/tayapopova/'

def main():
	driver = webdriver.Chrome()
	actions.login(driver=driver, email=config.EMAIL, password=config.PASSWORD)
	time.sleep(2)
	person = Person(url=url, driver=driver)
	actions.scroll_to_bottom(driver)
	data = {
		'name':person.get_name(),
		'position':person.get_position(),
		'company_name':person.get_company_name(),
		'region':person.get_region(),
		'photo_url':person.get_photo(),
		'education':person.get_education()
	}
	print(data)
	x=input()
	driver.close()

if __name__ == '__main__':
	main()