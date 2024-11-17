from pyspark.sql import SparkSession
import os

def create_spark_session():
    jdbc_driver_path = os.path.join(os.getcwd(), 'library', 'mysql-connector-j-9.1.0.jar')
    spark = SparkSession.builder.appName("MySQL_spark_integration").config('spark.jars', jdbc_driver_path).getOrCreate()
    return spark

def execute_query(spark: SparkSession, query: str):
    df =  spark.read.format("jdbc").options(
            url = 'jdbc:mysql://localhost:3306/2024_fast_api_student',
            dbtable = f"({query}) as query",
            driver = "com.mysql.cj.jdbc.Driver",
            user = "root",
            password = "",
            autoReconnect='true',
            useServerPrepStmts='true'
        ).load()
    return df
