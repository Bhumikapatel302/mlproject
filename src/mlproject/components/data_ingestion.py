import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


import os##To make current folders and path
import sys##to handle custom exception
from mlproject.exception import CustomException #to handle custom exception
from mlproject.logger import logging#to log the information
import pandas as pd
from mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split

from dataclasses import dataclass #to take input from user in a structured way

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')#t0 cceate the path for train,test and raw data


class DataIngestion:
    def __init__(self) :
        self.ingestion_config=DataIngestionConfig()   #to create a object of DataIngestionConfig class
    def initiate_data_ingestion(self) :
        try:
            #reading the data from mysql database
            df=read_sql_data()
            logging.info("Reading completed mysql database")#to log the information

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#to create the directory if not exists


            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)#to save the datta in csv format
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)# to split the data into train and test
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#to save the datta in csv format
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#to save the datta in csv format

            logging.info("Ingestion is completed")
            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path
                   
                   )
        

        except Exception as e:
            raise CustomException(e,sys) #to handle custom exception
        



        
