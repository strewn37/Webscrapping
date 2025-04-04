import cloudscraper
import time
from selenium import webdriver

def verifyesc(driver:webdriver.Chrome):
        
        url = driver.current_url

        print(f"Escaping Verification {url}!")

        scraper = cloudscraper.create_scraper()

        response = scraper.get(url)

        cookies = response.cookies
        
        time.sleep(5)
        
        for cookie in cookies:

            driver.add_cookie({"name": cookie.name, "value": cookie.value})
        
        time.sleep(5)

        driver.refresh()

        time.sleep(5)