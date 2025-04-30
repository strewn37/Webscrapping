import Xpaths.mainpage_xpaths as pxp
from tqdm import tqdm as tq
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from Modules import Verfiy as v
from dotenv import load_dotenv
import os

load_dotenv()


class Extract:
    def __init__(self,bot: webdriver.Chrome):
            self.driver = bot
            self.page = "0"

    def extract_titles_comp_loc(self):
            
            page_check = int(self.page)
            
            if(page_check == 28 or page_check == 31 or page_check>36):
                    
                v.verifyesc(self.driver)
                        
                self.driver.refresh()
            
            jobTitle = self.driver.find_elements(*pxp.job_title)
            company = self.driver.find_elements(*pxp.job_company)
            location = self.driver.find_elements(*pxp.job_location)

            arr = []

            for elementTitle,elementCompany,elementLocation in zip(jobTitle,company,location):

                try:
                    title = str(elementTitle.text)
                    comp = str(elementCompany.text)
                    loc = str(elementLocation.text)
                    if(len(loc.split(","))==3):
                        loc = loc.split(",")[1]+","+loc.split(",")[2]
                    try:
                        salary = self.driver.find_element(By.XPATH,"//span[text()='"+comp+"']/../../../following-sibling::div/ul//div[contains(@class,'salary')]/div").text
                    except Exception:
                        salary = "Not Mentioned"
                    
                    pattern_s = r"\bFrom\b|₹|\ba\b|[,]|\bup\b|\bto\b"
                    pattern_t = r"[,]"

                    salary = re.sub(pattern_s,"",salary)
                    title = re.sub(pattern_t,"-",title)

                    row = title+","+comp+","+loc+","+salary
                    arr.append(row)
                    
                except Exception:
                     pass
            
            time.sleep(5)

            try:

                self.page = self.driver.find_element(*pxp.page_no).text
            
                # print(f"Extracted all the Job Titles in {self.page}")

            except Exception:

                print(f"Extracted!!")
                return arr

            return arr
    
    def savetxt(self,array,job):

        df = pd.DataFrame(array)

        # np_array = np.array(array)

        # print(np_array.shape)
        

        if(os.getenv("SYSTEM")=='WSL'):
            path = os.getenv("PATH_WSL")+job+".txt"
        else:
            path = os.getenv("PATH_Windows")+job+".txt"

        with open(path, "w", encoding="utf-8", errors="ignore") as file:
            for item in df.squeeze():
                file.write(str(item) + "\n")

        print(f"Saved the file in {path}")