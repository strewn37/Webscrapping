import time
from Modules import initial,Extraction
from Pages import login,jobs


def scrape(job):
    ##---- Initializing all Pages----

    bot = initial.webd()
    driver = bot.driver
    mainPage = jobs.mainpage(driver)
    loginPage = login.log(driver)
    extract = Extraction.Extract(driver)
    print("Intialized all the pages")

    ##-------------------------------

    # print("Which Job you want scrape?")

    # job = input()

    loginPage.login_in()

    time.sleep(5)

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
        time.sleep(5)

    extract.savetxt(arr,job)

    bot.quit()

# scrape("Data Engineer")