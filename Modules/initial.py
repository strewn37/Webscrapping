from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import shutil
from webdriver_manager.chrome import ChromeDriverManager

class webd:

    def __init__(self):

        chrome_path = shutil.which("google-chrome")
        
        options = webdriver.ChromeOptions()
        # proxy = "123.45.67.89:8080"
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        # options.add_argument(f"--proxy-server={proxy}")
        options.add_argument("--disable-blink-features=AutomationControlled") 
        options.add_argument("--disable-gpu-rasterization")
        options.add_argument("--disable-software-rasterizer") 
        options.binary_location = chrome_path
        
        # chrome_driver_path = r"\home\gokul\driver\chromedriver"
        # service = Service(executable_path=chrome_driver_path)

        service = Service(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service, options=options)
    
    def quit(self):
        
        self.driver.quit()
