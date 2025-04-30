from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv,set_key
import os




class webd:

    def __init__(self,system):

        if(system=="windows"):
            env_path = r"c:\Users\pechimut\WebScrapping\Webscrapping\Properties.env"
            load_dotenv(env_path)
            set_key(env_path, "SYSTEM", "WINDOWS")
        else:
            env_path = "/mnt/c/Users/pechimut/WebScrapping/Webscrapping/Properties.env"
            load_dotenv(env_path)
            set_key(env_path, "SYSTEM", "WSL")
            
        options = webdriver.ChromeOptions()
        # proxy = "123.45.67.89:8080"
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        # options.add_argument(f"--proxy-server={proxy}")
        options.add_argument("--disable-blink-features=AutomationControlled") 
        options.add_argument("--disable-gpu-rasterization")
        options.add_argument("--disable-software-rasterizer") 

        if(os.getenv("SYSTEM")=="WSL"):
            chrome_path = shutil.which("google-chrome")
            service = Service(ChromeDriverManager().install())
        else:
            chrome_path=os.getenv("CHROME_PATH")
            service = Service(executable_path=os.getenv("CHROMEDRIVER_PATH"))

        options.binary_location = chrome_path
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def quit(self):
        
        self.driver.quit()
