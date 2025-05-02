import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import os##To make current folders and path
import sys##to handle custom exception
from mlproject.exception import CustomException#to handle custom exception
from mlproject.logger import logging#to log the information
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import mysql.connector
load_dotenv()##load environment variables from .env file
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')




def read_sql_data():
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user=user,
            password=password,
            database=db,
            port = 3306  
        )
        
        if mydb.is_connected():
            print("Successfully connected to the database!")
            # logging.info("Connection Established")

        # Query data
        query = "SELECT * FROM students"  # Adjust to your table name
        df = pd.read_sql_query(query, mydb)  # Using pandas to run SQL query

        print(df.head()) 
        return df


    except Exception as ex:
        logging.error("Failed to read from database", exc_info=True)
        raise CustomException(ex, sys)

