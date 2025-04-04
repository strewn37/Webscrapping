import Xpaths.starter_xpaths as sxp
from Modules import Verfiy as v
from selenium import webdriver
import cloudscraper

class log:

    def __init__(self, bot: webdriver.Chrome):

        self.driver = bot
    
    def login_in(self):

        self.driver.get(r"https://in.indeed.com/")

        v.verifyesc(self.driver)

        print("Landed in Indeed Page")

        homeicon = self.driver.find_element(*sxp.ind_home)
        
        self.driver.execute_script("arguments[0].setAttribute('style','border: 3px solid red;');",homeicon)

        self.driver.execute_script("arguments[0].click();",homeicon)

        print("Clicked Home Icon")



        # time.sleep(10)

        # command = input()

        # if(command.lower() == 'proceed' or command.lower() == 'ok'):

        #     user = self.driver.find_element(*sxp.name).text

        #     print(f"Logged in as {user}")
        #     print("Proceeding with next Steps....")


        # while(1):
        #     if(self.driver.find_element(*sxp.home).is_displayed()):
        #         break

        # self.driver.find_element(*sxp.sign_in).click()

        # print("Clicked Sign In")

        # time.sleep(3)

        # email = self.driver.find_element(*sxp.email_id)
        
        # email.click()

        # email.send_keys("gokulakrishnaap@gmail.com")

        # print("Entered Email ID")

        # time.sleep(3)

        # sub = self.driver.find_element(*sxp.submit)

        # print(f"Continue button is {sub.is_enabled()}")

        # self.driver.execute_script("arguments[0].click();", sub)

        # # time.sleep(5)

        # # self.driver.execute_script("arguments[0].click();", sub)

        # time.sleep(3)

        # self.driver.find_element(*sxp.login_code).click()

        # time.sleep(3)

        # print("Enter the Code")

        # code = str(input())

        # logcode = self.driver.find_element(*sxp.passcode)

        # logcode.click()

        # logcode.send_keys(code)

        # time.sleep(6)

        # signIn = self.driver.find_element(*sxp.login)

        # self.driver.execute_script("arguments[0].click();", signIn)

        # loginerror = self.driver.find_element(*sxp.error)

        # while(loginerror.is_displayed()):


        #     print("Wrong Code!!")

            
        #     print("Enter the Code again")

        #     code = str(input())

        #     logcode = driver.find_element(*sxp.passcode)

        #     logcode.click()

        #     logcode.send_keys(code)

        #     time.sleep(6)

        #     signIn = driver.find_element(*sxp.sign_in)

        #     driver.execute_script("arguments[0].click();", signIn)

        #     time.sleep(3)

    def verifyhomepage(self):

        try:
            
            self.driver.find_element(*sxp.home)

        except Exception:

            current_url = self.driver.current_url

            v.verifyesc(self.driver,current_url)

        finally:

            if(self.driver.find_element(*sxp.home).is_displayed()):

                    print(f"Landed in Homepage")
                    
                    self.driver.find_element(*sxp.home).click()
            else:

                print(f"Not Landed in Homepage")