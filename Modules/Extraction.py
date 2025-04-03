import Xpaths.mainpage_xpaths as pxp
from tqdm import tqdm as tq
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from Modules import Verfiy as v


class Extract:
    def __init__(self,bot: webdriver.Chrome):
            self.driver = bot

    def extract_titles_comp_loc(self):
            
            jobTitle = self.driver.find_elements(*pxp.job_title)
            company = self.driver.find_elements(*pxp.job_company)
            location = self.driver.find_elements(*pxp.job_location)

            arr = []

            for elementTitle,elementCompany,elementLocation in tq(zip(jobTitle,company,location),total=len(jobTitle),desc="Extracting JobTitle,Company,Location",unit="lines"):

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
                    title = re.sub(pattern_t," ",title)

                    row = title+","+comp+","+loc+","+salary
                    arr.append(row)
                    
                except Exception:
                     pass
            
            time.sleep(5)
            try:
                page = self.driver.find_element(*pxp.page_no).text
            
                print(f"Extracted all the Job Titles in {page}")

                if(page == '28'):
                    
                    v.verifyesc()
                    
                    self.driver.refresh()

            except Exception:

                print(f"Extracted!!")

            return arr
    
    def savetxt(self,array,job):

        df = pd.DataFrame(array)

        # np_array = np.array(array)

        # print(np_array.shape)
        
        path  = r"C:\Users\pechimut\Webscrape\Webscrape"+job+".txt"

        with open(path, "w", encoding="utf-8", errors="ignore") as file:
            for item in tq(df.squeeze(), desc="Writing to file", unit="row"):
                file.write(str(item) + "\n")