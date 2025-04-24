import findspark
findspark.init()


from pyspark.sql import *
from pyspark.sql.functions import * 
from pyspark.sql.dataframe import DataFrame


class Functions:

        def __init__(self,session: SparkSession):
            self.spark = session

        def save(self,container,data: DataFrame,typeoffile,Name):
        
            if(typeoffile=="file"):

                if(container=="bronze"):
                    data.write \
                    .format("parquet") \
                    .mode("overwrite") \
                    .save(f"abfss://{container}@webscrapeadls01.dfs.core.windows.net/sample/output/{Name}")
                elif(container=="silver"):
                    data.write \
                    .format("delta") \
                    .mode("overwrite") \
                    .save(f"abfss://{container}@webscrapeadls01.dfs.core.windows.net/sample/output/{Name}")
                else:
                    data.write \
                    .format("delta") \
                    .mode("overwrite") \
                    .save(f"abfss://{container}@webscrapeadls01.dfs.core.windows.net/sample/output/{Name}")
            else:
                 data.write \
                    .format("delta") \
                    .mode("overwrite") \
                    .saveAsTable(f"{Name}")


 
              
            

