import cloudscraper
import time
from selenium import webdriver

def verifyesc(driver:webdriver.Chrome):

        print(f"Escaping Verification!")

        scraper = cloudscraper.create_scraper()

        response = scraper.get(driver.current_url)

        cookies = response.cookies

        time.sleep(4)

        for cookie in cookies:

            driver.add_cookie({"name": cookie.name, "value": cookie.value})
        
        time.sleep(5)
    
        driver.refresh()
