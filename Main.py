import time
from Modules import initial,Extraction
from Pages import login,jobs

##---- Initializing all Pages----

bot = initial.webd()
driver = bot.driver
mainPage = jobs.mainpage(driver)
loginPage = login.log(driver)
extract = Extraction.Extract(driver)
print("Intialized all the pages")

##-------------------------------

loginPage.login_in()

time.sleep(4)

loginPage.verifyhomepage()

time.sleep(5)

mainPage.search("data analyst")

arr = extract.extract_titles_comp_loc()

# for i in arr:
#     print(i)

bot.quit()