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

job = "data engineer"

loginPage.verifyhomepage()

time.sleep(5)

mainPage.search(job)

arr = []

temp = extract.extract_titles_comp_loc()

for i in temp:
    arr.append(i)

while(mainPage.nav_next()):
    temp = []
    temp = extract.extract_titles_comp_loc()
    for i in temp:
        arr.append(i)

extract.savetxt(arr,job)

bot.quit()