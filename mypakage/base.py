from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


class Page(object):
	def __init__(self, driver, base_url='https://wonolo-dev.herokuapp.com/users/sign_in'):
		self.base_url = base_url
		self.driver = driver
		self.timeout = 30

	def find_element(self, *locator):
		return self.driver.find_element(*locator)

	def wait_for_element(self, *locator):
		return WebDriverWait(self, self.driver, 30).until(lambda self: self.find_element(*locator))


