import time
from tqdm import tqdm as tq
import Xpaths.page_xpaths as pxp
import Xpaths.starter_xpaths as sxp
from Driver_init.initial import start
from Pages import login
driver = start()

login.login_in(driver)

time.sleep(4)

Home = driver.find_element(*sxp.home)

print(f"Landed in Homepage({Home.is_displayed()})")

Home.click()

time.sleep(3)

driver.find_element(*pxp.search).send_keys("jobs")

driver.find_element(*pxp.find_jobs).click()

print("Searched Jobs")

time.sleep(4)
jobTitle = driver.find_elements(*pxp.job_title)

print(len(jobTitle))