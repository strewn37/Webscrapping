from selenium.webdriver.common.by import By

job_title = (By.XPATH,"//span[contains(@id,'jobTitle')]")

job_location = (By.XPATH,"//div[@data-testid='company-name']")

job_salary = (By.XPATH,"//div[contains(@class,'salary')]")

next_page = (By.XPATH,"//a[contains(@data-testid,'page-next')]")

search = (By.XPATH,"//input[@aria-label='search: Job title, keywords, or company']")

find_jobs = (By.XPATH,"//button[text()='Find jobs']")
