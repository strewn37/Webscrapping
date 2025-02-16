from pyspark.sql import SparkSession
from pyspark.sql.types import *
import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background mode (no UI)
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.in")

print("What do you want to search for?")
val = input()
print("Do you have specifications about the product(size, feature) for?")
keyVal = input()
print("What is your budget?")
budget = int(input())
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon.in']").send_keys(val+" "+str(budget))
print("Clicked Search bar and typed "+val)
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']/parent::span").click()
print("Searched for "+val)



driver.implicitly_wait(2)

titles = driver.find_elements(By.XPATH,"//div[@role='listitem']//h2/span")
ratings = driver.find_elements(By.XPATH,"//div[@role='listitem']//div[@data-cy='reviews-block']//a[@href='javascript:void(0)']")
noofratings = driver.find_elements(By.XPATH,"//div[@role='listitem']//div[@data-cy='reviews-block']//a[@href='javascript:void(0)']/parent::span/following-sibling::a")
prices = driver.find_elements(By.XPATH,"//span[@class='a-price']//span[@class='a-price-whole']")
lop = []
lor = []
i = 0
statement = "+-----*List of "+val+"s*-----+"
eol = '-'*(len(statement)-2)
print(statement)
for title,rating,noofrating,price in zip(titles,ratings,noofratings,prices):
    templor = []
    templop = []
    if( True if (keyVal.lower() == 'na') or (keyVal.lower() == 'no') else keyVal in title.text):
        hrefvalue = title.text.split(' ')[0]+'-'+title.text.split(' ')[1]+'-'+title.text.split(' ')[2]
        # print(hrefvalue+" with Ratings - "+rating.get_attribute("aria-label").split(',')[0]+\
        #                 " with these "+noofrating.get_attribute("aria-label").split(' ')[0]+" people"\
        #                     +" Price of the product Rs."+price.text)
        rawrat = rating.get_attribute("aria-label").split(',')[0]
        try:
            rawnfr = noofrating.get_attribute("aria-label").split(' ')[0].split(',')[0]+noofrating.get_attribute("aria-label").split(' ')[0].split(',')[1]
        except Exception:
            rawnfr = noofrating.get_attribute("aria-label").split(' ')[0]
        try:
            rawprice = price.text.split(',')[0]+price.text.split(',')[1]
        except Exception:
            rawprice = price.text
        rat = float(rawrat.split(' ')[0])
        nfr = float(rawnfr.split(' ')[0])
        pop = int(rawprice)
        riskfactor = (rat*pop)/nfr
        # print(f"rat = "+rawrat+" nfr = "+rawnfr+" pop = "+rawprice+"\n------------")
        # print("Risk Factor to Buy this product ",riskfactor)
        # print("------------")
        if(budget>=pop):
            temp = hrefvalue+" which is priced @"+rawprice+" with Ratings "+rawrat+" with these no of people "+rawnfr
            templop.append(i)
            templop.append(temp)
            lop.append(templop)
        else:
            temp = hrefvalue+" which is priced @"+rawprice+" with Ratings "+rawrat+" with these no of people "+rawnfr
            templop.append(i)
            templop.append(temp)
            lop.append(templop)
        print(f"{temp} with {riskfactor}")
        templor.append(i)
        templor.append(riskfactor)
        lor.append(templor)
        i+=1
    else: 
        # print(keyVal+" "+Lan cabletitle.text)
        continue
print("+"+eol+"+")
lor.sort(key=lambda x:x[1])
# print(lor)
# print(lop)
statement = "\n+-----*Best "+val+" Under the budget is*-----+"
eol = '-'*(len(statement)-2)
for i in lop:
    if(i[0]==lor[0][0]):
        print(statement+"\n"+i[1]+"\n+"+eol+"+")


driver.quit()

# file_path = r'C:\Users\Gokul\Downloads\netflix_titles.csv'
# file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB

# print(f"CSV file size: {file_size_mb:.2f} MB")

# spark  = SparkSession.builder.appName("Firstapp")\
#         .master("local[*]")\
#         .config("spark.ui.retainedJobs", "100")\
#         .config("spark.sql.warehouse.dir", r"C:\Users\Gokul\hive\warehouse") \
#         .config("spark.ui.enabled",True)\
#         .enableHiveSupport()\
#         .getOrCreate()

# spark.sql("CREATE DATABASE IF NOT EXISTS default")
# spark.sql("SHOW DATABASES").show()


# schema = StructType([StructField('show_id', StringType(), True),\
#                      StructField('type', StringType(), True),\
#                           StructField('title', StringType(), True),\
#                               StructField('director', StringType(), True),\
#                                   StructField('cast', StringType(), True),\
#                                       StructField('country', StringType(), True),\
#                                           StructField('date_added', StringType(), True),\
#                                               StructField('release_year', StringType(), True),\
#                                                   StructField('rating', StringType(), True),\
#                                                       StructField('duration', StringType(), True),\
#                                                           StructField('listed_in', StringType(), True),\
#                                                               StructField('description', StringType(), True)])
# df = spark.read.csv(r'C:\Users\Gokul\Downloads\netflix_titles.csv',header=True,schema=schema)
# df = df.select("release_year")
# spark.sql("SHOW TABLES IN default").show()
# # df = df.repartition(2)
# # print(spark.get)
# # print(spark.conf.get("spark.sql.autoBroadcastJoinThreshold").split('b'))
# size = int(spark.conf.get("spark.sql.autoBroadcastJoinThreshold").split('b')[0])/(1024*1024*8)
# print(df.count(), df.rdd.getNumPartitions(),spark.conf.get("spark.sql.adaptive.enabled"),f"{file_size_mb:.2f} MB",spark.conf.get("spark.sql.warehouse.dir"))
# # df.show()
# df.show()
# df.write.format("parquet").mode("overwrite").save(r'C:\Users\Gokul\Data\Bronze\release_year')
# df.write.mode("overwrite").saveAsTable("default.release_yeartb")
# rdf = spark.read.format("parquet").load(r'C:\Users\Gokul\Data\Bronze\release_year')
# rdf.show()
# t = input()
# while t=='R':
#     time.sleep(60) 
#     t = input()