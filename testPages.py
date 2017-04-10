import unittest
from mypakage.pages import *
from selenium import webdriver

# Test suite:
class TestPages(unittest.TestCase):
    #   Use Webdriver Firefox, open the Customer Portal Web app link
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.get('https://wonolo-dev.herokuapp.com/users/sign_in')

    #   Test case: Sign into the Web app by Username and Password
    def test_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.signIn("dungvu2912@gmail.com", "12345678")
    #   Verify if Sign in is successful, the Home page will be loaded
        self.assertEqual("Wonolo: Thao Create", self.driver.title)

    #   Test case: Fill in all required information and create a New Job
    def test_new_job_page(self):
        login_page = LoginPage(self.driver)
        login_page.signIn("dungvu2912@gmail.com", "12345678")
        new_job_page = NewJobPage(self.driver)
        new_job_page.addNewJob()
    #   Verify if the New Job has been created successfully, the Active Job page will be loaded
    #   self.assertEqual("Wonolo: Thao Create", self.driver.title)

    #   Test case: Go to Active Page and search for the added Job and its information
    def test_active_job_page(self):
        login_page = LoginPage(self.driver)
        login_page.signIn("dungvu2912@gmail.com", "12345678")
        active_job_page = ActiveJobPage(self.driver)
        active_job_page.verifyJobTitle()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

# Run test suite:
suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
unittest.TextTestRunner(verbosity=2).run(suite)
