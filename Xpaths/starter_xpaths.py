from selenium.webdriver.common.by import By

ind_home = (By.XPATH,"//a[@aria-label='Indeed Home']")

home = (By.XPATH,"//a[text()='Home']")

sign_in = (By.XPATH,"//a[text()='Sign in']")

login = (By.XPATH,"//span[text()='Sign in']/..")

email_id = (By.XPATH,"//input[@name='__email']")

submit = (By.XPATH,"//button[@type='submit']")

login_code = (By.XPATH,"//a[text()='Sign in with login code instead']")

passcode = (By.XPATH,"//input[@name='passcode']")

error = (By.XPATH,"//div[text()='Code did not match or is no longer valid']")
