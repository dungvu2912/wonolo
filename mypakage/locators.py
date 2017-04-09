from selenium.webdriver.common.by import By

# XPATH of elements in the Login Page:
class LoginPageLocators(object):
	Email	           = (By.XPATH, "//input[@id='user_email']")
	Password	   = (By.XPATH, "//input[@id='user_password']")
	LoginButton	   = (By.XPATH, "//input[@class='btn primary_button']")

# XPATH of elements in the New Job Page:
class NewJobPageLocators(object):
	NewJobButton	   = (By.XPATH, "//a[@href='/job_requests/new']")
	JobName            = (By.XPATH, "//input[@id='job_request_request_name']")
	Category    	   = (By.XPATH, "//select[@id='job_request_category']/option[.='Delivery']")
	TaskToBePerformed  = (By.XPATH, "//textarea[@id='job_request_description_tasks']")
	Requirements       = (By.XPATH, "//div[@class='jr_requirement']/input")
	CompanyDescription = (By.XPATH, "//textarea[@id='job_request_description_company']")
	TravelTips         = (By.XPATH, "//textarea[@id='job_request_description_travel']")
	ArrivalIntructions = (By.XPATH, "//textarea[@id='job_request_description_arrival']")
	WonoloersNeeded    = (By.XPATH, "//input[@id='job_request_slots']")
	Venue              = (By.XPATH, "//input[@id='job_request_venue']")
	Address            = (By.XPATH, "//input[@id='job_request_address']")
	City               = (By.XPATH, "//input[@id='job_request_city']")
	Zip                = (By.XPATH, "//input[@id='job_request_zip']")
	EstimatedHours     = (By.XPATH, "//select[@id='job_request_duration_hours']/option[.='5']")
	EstimatedMins      = (By.XPATH, "//select[@id='job_request_duration_minutes']/option[.='30']")
	Pay                = (By.XPATH, "//input[@id='job_request_wage']")
	PostJobButton      = (By.XPATH, "//input[@id='post_job_button']")
	JobButton          = (By.XPATH, "//a[@id='new_request_button']")

# XPATH of elements in the Active Job Page:
class ActiveJobPageLocators(object):
	ActiveJobLink      = (By.XPATH, "//a[@href='/job_requests/active']")
	JobTitle           = (By.XPATH, "//td[@class='job_title'][.='Gardener']")
	KeyWord            = (By.XPATH, "//div[@class='input_container']//input[@class='form-control jri_requestor_name input_style']")
	SearchButton       = (By.XPATH, "//button[.='Search']")
	DetailButton       = (By.XPATH, "//td[@class='job_title'][.='Gardener']/following-sibling::td[@class='request_actions']//a/div/span")

# XPATH of elements in the Detail Job Page:
class DetailJob(object):
	JobName            = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Job name']/following-sibling::td")
	Category           = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Category']/following-sibling::td")
	TaskToBePerformed  = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Description']/following-sibling::td")
	WonoloersNeeded    = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Wonoloers needed']/following-sibling::td")
	Address            = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Address']/following-sibling::td")
	City               = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='City']/following-sibling::td")
	Zip                = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Zip']/following-sibling::td")
	EstimatedHours     = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Estimated Job Duration']/following-sibling::td")
	Pay                = (By.XPATH, "//div[@id='job_request_details_panel']//table/tbody/tr/td[.='Pay']/following-sibling::td")

