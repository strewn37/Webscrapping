import findspark
findspark.init()


from pyspark.sql import SparkSession
from dotenv import load_dotenv,set_key
import os



class SessionCreate:
    
    def __init__(self):

        env_path = r"c:\Users\pechimut\WebScrapping\Webscrapping\Pysprk\Properties.env"
        load_dotenv(env_path)   

        self.storage_account_name = os.getenv("account_name")
        self.storage_account_key = os.getenv("account_key")
        self.container_name = os.getenv("warehouse_container")
        self.spark = None

    def initial(self):

        self.spark = SparkSession.builder \
                                .appName("Refine") \
                                .config("spark.sql.warehouse.dir", f"abfss://{self.container_name}@{self.storage_account_name}.dfs.core.windows.net/warehouse/") \
                                .config("spark.hadoop.fs.azure", "org.apache.hadoop.fs.azure.NativeAzureFileSystem") \
                                .config(f"fs.azure.account.key.{self.storage_account_name}.dfs.core.windows.net", self.storage_account_key) \
                                .config("spark.jars.packages", "io.delta:delta-spark_2.12:3.1.0") \
                                .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
                                .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
                                .config("spark.sql.execution.arrow.enabled", "true") \
                                .getOrCreate()


