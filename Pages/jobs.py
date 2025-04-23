import Xpaths.mainpage_xpaths as pxp
import time
from Modules.Verfiy import verifyesc
from selenium import webdriver

class mainpage:

    def __init__(self, bot: webdriver.Chrome):
        self.driver = bot

    def search(self,job):

        self.driver.find_element(*pxp.search).send_keys(job)

        time.sleep(5)

        self.driver.find_element(*pxp.find_jobs).click()

        time.sleep(5)

        # print(f"Searched {job}")

        verifyesc(self.driver)

        time.sleep(4)

    def nav_next(self):

        try:

            if(self.driver.find_element(*pxp.next_page).is_displayed()):
                    
                    self.driver.find_element(*pxp.next_page).click()

                    return True
            
            else:
                return False
        except Exception:
             
             return False