from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from user_scraper import Person
import actions
import config
import time


def get_url(file_name):
	url_list = []
	with open(file_name, 'r') as f:
		data = f.read()
		url_list = [url for url in data.split('\n')]
	for url in url_list:
		yield url


def main():
	driver = webdriver.Chrome()
	act = ActionChains(driver)
	actions.login(driver=driver, email=config.EMAIL, password=config.PASSWORD)
	act.pause(2).perform()

	start_time = time.time()
	counter = 0
	
	for url in get_url('linkedin_urls.txt'):
		person = Person(url=url, driver=driver)
		actions.scroll_to_bottom(driver)
		data = {
			'name':person.get_name(),
			'url':person.url,
			'position':person.get_position(),
			'region':person.get_region(),
			'photo_url':person.get_photo(),
			'education':person.get_education()
		}
		counter += 1
		print()
		print(data)

	print()
	print(f'number of times: {counter}')
	print(f'time: {(time.time() - start_time)/counter}')
	
	a = input('\n----Press any key to exit----\n')
	actions.logout(driver=driver)
	driver.close()

if __name__ == '__main__':
	main()