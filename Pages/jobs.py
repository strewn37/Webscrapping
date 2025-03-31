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

        print(f"Searched {job}")

        time.sleep(4)