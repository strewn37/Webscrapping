import cloudscraper
from selenium import webdriver

def verifyesc(driver:webdriver.Chrome,url):

        print("Escaping Verification!")

        scraper = cloudscraper.create_scraper()

        response = scraper.get(url)

        cookies = response.cookies
        
        for cookie in cookies:

            driver.add_cookie({"name": cookie.name, "value": cookie.value})

        driver.refresh()
