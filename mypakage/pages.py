from .base import Page
from .locators import *
import time

job_dict = {'JobName':'Gardener',
			'Category':'Delivery',
			'TaskToBePerformed':"raising plants from seeds or cuttings.digging, planting and weeding flower beds and borders.",
			'WonoloersNeeded':'1',
			'Address':'Doan Van Bo',
			'City':'Sai Gon',
			'Zip':'70000',
			'EstimatedHours':'5',
			'EstimatedMins':'0',
			'Pay':'100'}

# Login Page class: Input username and password, and then click the Sign in button
class LoginPage(Page):
	def signIn(self, username, password):
		self.find_element(*LoginPageLocators.Email).send_keys(username)
		self.find_element(*LoginPageLocators.Password).send_keys(password)
		self.find_element(*LoginPageLocators.LoginButton).click()
		self.wait_for_element(*NewJobPageLocators.NewJobButton)

# New Job Page class: Fill in all the required information to create a New Job in New Job page
class NewJobPage(Page):
	def addNewJob(self):
		self.find_element(*NewJobPageLocators.NewJobButton).click()
		self.find_element(*NewJobPageLocators.JobName).send_keys(job_dict["JobName"])
		self.find_element(*NewJobPageLocators.Category).click()
		self.find_element(*NewJobPageLocators.TaskToBePerformed).send_keys(job_dict["TaskToBePerformed"])
		self.find_element(*NewJobPageLocators.WonoloersNeeded).clear()
		self.find_element(*NewJobPageLocators.WonoloersNeeded).send_keys(job_dict["WonoloersNeeded"])
		self.find_element(*NewJobPageLocators.Address).send_keys(job_dict["Address"])
		self.find_element(*NewJobPageLocators.City).send_keys(job_dict["City"])
		self.find_element(*NewJobPageLocators.Zip).send_keys(job_dict["Zip"])
		self.find_element(*NewJobPageLocators.EstimatedHours).click()
		self.find_element(*NewJobPageLocators.EstimatedMins).click()
		self.find_element(*NewJobPageLocators.Pay).send_keys(job_dict["Pay"])
		self.find_element(*NewJobPageLocators.PostJobButton).click()

# Active Job Page class: Open Active job page, search for the Job Name, and then click the Detail button
class ActiveJobPage(Page):
	def verifyJobTitle(self):
		self.find_element(*ActiveJobPageLocators.ActiveJobLink).click()
		self.find_element(*ActiveJobPageLocators.KeyWord).send_keys(job_dict["JobName"])
		self.find_element(*ActiveJobPageLocators.SearchButton).click()
		# Wait for the ajax button Detail is loaded
		self.sleep(7)
		#self.wait_for_element(*ActiveJobPageLocators.DetailButton)
		print("\nThe new added Job Name '" + self.find_element(*ActiveJobPageLocators.JobTitle).text + "' is found.\n")
		self.find_element(*ActiveJobPageLocators.DetailButton).click()
		#  Wait for the Job Request Page is loaded
		self.wait_for_element(*DetailJob.JobName)

		# Job Name
		addedJobName = self.find_element(*DetailJob.JobName).text
		print("Check the Job Name field: " + str(self.compare_values(job_dict["JobName"],addedJobName)) + "\n")

		# Category
		addedCategory = self.find_element(*DetailJob.Category).text
		print("Check the Category field: " + str(self.compare_values(job_dict["Category"],addedCategory)) + "\n")

		# Task to be performed field
		tasks = "TASKS TO BE PERFORMED: " + job_dict["TaskToBePerformed"]
		addedTasks = self.find_element(*DetailJob.TaskToBePerformed).text
		print("Check the Task to be performed field: " + str(self.compare_values(tasks,addedTasks)) +"\n")

		# Wonoloers needed field
		addedWonoloersNeeded = self.find_element(*DetailJob.WonoloersNeeded).text
		print("Check the Wonoloers needed field: " + str(self.compare_values(job_dict["WonoloersNeeded"],addedWonoloersNeeded)) + "\n")

		# Address
		addedAddress = self.find_element(*DetailJob.Address).text
		print("Check the Address field: " + str(self.compare_values(job_dict["Address"],addedAddress)) + "\n")

		# City
		addedCity = self.find_element(*DetailJob.City).text
		print("Check the City field: " + str(self.compare_values(job_dict["City"],addedCity)) + "\n")

		# Zip
		addedZip = self.find_element(*DetailJob.Zip).text
		print("Check the Zip field: " + str(self.compare_values(job_dict["Zip"],addedZip)) + "\n")

		# Time
		time = job_dict["EstimatedHours"] + "h"
		addedTime = self.find_element(*DetailJob.EstimatedHours).text
		print("Check the Estimated Hours field: " + str(self.compare_values(time,addedTime)) + "\n")

		# Pay
		pay = "$" + job_dict["Pay"] + ".00"
		addedPay = self.find_element(*DetailJob.Pay).text
		print("Check the Pay: " + str(self.compare_values(pay,addedPay)) + "\n")
		

