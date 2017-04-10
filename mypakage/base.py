from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


class Page(object):
    def __init__(self, driver, base_url='https://wonolo-dev.herokuapp.com/users/sign_in'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    #   Find the element by locator from locators.py
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    #   Wait until the element display
    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 30).until(lambda self: self.find_element(*locator))

    #   Pause for n seconds
    def sleep(self, sleepTime):
        time.sleep(sleepTime)

    #   Compare between valueA and valueB
    def compare_values(self, valueA, valueB):
    	if(valueA == valueB):
    		return True
    	else:
    		return False

    #   Check if the element is present
    def is_element_present(self,  *locator):
        try: 
        	self.driver.find_element(*locator)
        except NoSuchElementException as e: 
        	return False
        return True


