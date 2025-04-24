from Modules import Session,Funtionalities
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def start(container,status):

    sessionObject = Session.SessionCreate()
    sessionObject.initial()
    spark = sessionObject.spark
    func = Funtionalities.Functions(spark)


    while(status=='presist'):
        
        data = spark.read.csv(r"C:\Users\pechimut\Downloads\Employee.csv", header=True, inferSchema=True)

        func.save(container,data,"table","sample_Table")

        status = input()
    
    spark.close()

start("gold","presist")
