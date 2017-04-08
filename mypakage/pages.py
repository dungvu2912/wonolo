from .base import Page
from .locators import *
from time import sleep

job_dict = {'JobName':"cleaning house at weekend",
			'Category':'Delivery',
			'TaskToBePerformed':"raising plants from seeds or cuttings.digging, planting and weeding flower beds and borders.",
			'WonoloersNeeded':'1',
			'Address':'Doan Van Bo',
			'City':'Sai Gon',
			'Zip':'70000',
			'EstimatedHours':'5',
			'EstimatedMins':'0',
			'Pay':'100'}

class LoginPage(Page):
	def signIn(self, username, password):
		self.find_element(*LoginPageLocators.Email).send_keys(username)
		self.find_element(*LoginPageLocators.Password).send_keys(password)
		self.find_element(*LoginPageLocators.LoginButton).click()

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


class ActiveJobPage(Page):
	def verifyJobTitle(self):
		#temp:
		self.find_element(*ActiveJobPageLocators.ActiveJobLink).click()
		self.find_element(*ActiveJobPageLocators.KeyWord).send_keys(job_dict["JobName"])
		self.find_element(*ActiveJobPageLocators.SearchButton).click()
		self.find_element(*ActiveJobPageLocators.DetailButton).click()
		result = self.find_element(*ActiveJobPageLocators.JobTitle).text
		#self.assertEquals(result,job_dict["JobName"])



class JobDetailPage(Page):
	def verifyJobDetail(self):
		for key in job_dict:
			job_detail_list = []
			job_detail_list = job_detail_list.append(self.find_element(*DetailJob.key).text)
			print(job_detail_list)
			
			for element in job_detail_list:
				if(self.assertEquals(job_dict[key],element)==True):
					print("Find %s in the job detail page."%key)
				else:
					print("%s not found."%element)
