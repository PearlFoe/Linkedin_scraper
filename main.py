from selenium import webdriver
from user_scraper import Person
import actions
import config
import time

url = 'https://ru.linkedin.com/in/tayapopova/'

def main():
	driver = webdriver.Chrome()
	actions.login(driver=driver, email=config.EMAIL, password=config.PASSWORD)
	time.sleep(15)

	actions.logout(driver=driver)
	driver.close()

if __name__ == '__main__':
	main()