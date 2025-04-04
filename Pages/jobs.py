import Xpaths.mainpage_xpaths as pxp
import time
from tqdm import tqdm as tq
from selenium import webdriver

class mainpage:

    def __init__(self, bot: webdriver.Chrome):
        self.driver = bot

    def search(self,job):

        self.driver.find_element(*pxp.search).send_keys(job)

        self.driver.find_element(*pxp.find_jobs).click()

        # print(f"Searched {job}")

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