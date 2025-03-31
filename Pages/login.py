import Xpaths.starter_xpaths as sxp
import time
from selenium import webdriver


def login_in(driver: webdriver.Chrome):
    driver.get(r"https://in.indeed.com/")

    print("Landed in Indeed Page")

    homeicon = driver.find_element(*sxp.ind_home)
    
    driver.execute_script("arguments[0].setAttribute('style','border: 3px solid red;');",homeicon)

    driver.execute_script("arguments[0].click();",homeicon)

    print("Clicked Home Icon")

    time.sleep(10)

    # while(1):
    #     if(driver.find_element(*sxp.home).is_displayed()):
    #         break

    # driver.find_element(*sxp.sign_in).click()

    # print("Clicked Sign In")

    # time.sleep(3)

    # email = driver.find_element(*sxp.email_id)
    
    # email.click()

    # email.send_keys("gokulakrishnaap@gmail.com")

    # print("Entered Email ID")

    # time.sleep(3)

    # sub = driver.find_element(*sxp.submit)

    # print(f"Continue button is {sub.is_enabled()}")

    # driver.execute_script("arguments[0].click();", sub)

    # # time.sleep(5)

    # # driver.execute_script("arguments[0].click();", sub)

    # time.sleep(3)

    # driver.find_element(*sxp.login_code).click()

    # time.sleep(3)

    # print("Enter the Code")

    # code = str(input())

    # logcode = driver.find_element(*sxp.passcode)

    # logcode.click()

    # logcode.send_keys(code)

    # time.sleep(6)

    # signIn = driver.find_element(*sxp.login)

    # driver.execute_script("arguments[0].click();", signIn)

    # loginerror = driver.find_element(*sxp.error)

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
        

