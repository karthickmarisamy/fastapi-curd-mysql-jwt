from fastapi import APIRouter, Depends
from pyspark.sql import SparkSession
from fastapi.responses import JSONResponse
from utils.spark import create_spark_session, execute_query

router = APIRouter()

spark = create_spark_session()

@router.get("/query")
async def run_query():
    ''' 
    if not query:
        return JSONResponse(content={"error": "Query is not provided"}, status_code = 400)
    '''
    df = execute_query(spark, 'select * from student_info')
    
    result = df.toPandas().to_dict(orient='records')
    
    return result