import os##To make current folders and path
import sys##to handle custom exception
from src.mlproject.exception import CustomException#to handle custom exception
from src.mlproject.logger import logging#to log the information
import pandas as pd 
from dotenv import load_dotenv
import pymysql

load_dotenv()##load environment variables from .env file
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')




def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex)
