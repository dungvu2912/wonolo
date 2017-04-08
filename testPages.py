import unittest
from mypakage.pages import *
from selenium import webdriver


class TestPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get('https://wonolo-dev.herokuapp.com/users/sign_in')

    # def test_login_page(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.signIn("dungvu2912@gmail.com", "12345678")
    #     self.assertEqual("Wonolo:", self.driver.title)

    # def test_new_job_page(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.signIn("dungvu2912@gmail.com", "12345678")
    #     new_job_page = NewJobPage(self.driver)
    #     new_job_page.addNewJob()

    def test_active_job_page(self):
        login_page = LoginPage(self.driver)
        login_page.signIn("dungvu2912@gmail.com", "12345678")    	
        active_job_page = ActiveJobPage(self.driver)
        active_job_page.verifyJobTitle()


if __name__ == '__main__':
    unittest.main()
