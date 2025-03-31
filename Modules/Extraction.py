import Xpaths.mainpage_xpaths as pxp
from tqdm import tqdm as tq
from selenium import webdriver


class Extract:
    def __init__(self,bot: webdriver.Chrome):
            self.driver = bot

    def extract_titles_comp_loc(self):
            
            jobTitle = self.driver.find_elements(*pxp.job_title)
            company = self.driver.find_elements(*pxp.job_company)
            location = self.driver.find_elements(*pxp.job_location)

            print(len(jobTitle))

            arr = []

            for elementTitle,elementCompany,elementLocation in tq(zip(jobTitle,company,location),total=len(jobTitle),desc="Extracting JobTitle,Company,Location",unit="lines"):

                title = elementTitle.text
                comp = elementCompany.text
                loc = elementLocation.text
                row = title+","+comp+","+loc
                arr.append(row)

            print("Extracted all the Job Titles")

            return arr
