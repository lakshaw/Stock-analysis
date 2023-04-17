import glob
import pandas as pd
from datetime import datetime
import csv
import tempfile

tmpfile = "tmp.tmp"
logtempfile = "log_temp_file.txt"
targetfile = "transformed_data_temp.csv"
BAJAJRE = "BAJAJRE.csv"


def extract_from_csv(BAJAJRE):
    dataframe = pd.read_csv('BAJAJRE.csv')
    #dataframe = dataframe.drop('Timestamp',inplace = True,axis = 1)
    return dataframe


#data = extract_from_csv(BIDATA).drop('Timestamp',inplace = True,axis = 1)

def extract():
    extracted_data = pd.DataFrame(columns=['Date','Turnover','%Deliverble','Last'])
    for BAJAJFINSV in glob.glob("BAJAJRE.csv"):
        extracted_data = extracted_data.append(extract_from_csv(BAJAJRE),ignore_index = True)
    return extracted_data

#print(extract())
#data_temp = extract_from_csv(BAJAJFINSV)
#data = extract_from_csv(BAJAJRE).drop(['Symbol','Series', 'Close','Open','High','Low','Last','Close','VWAP','Volume','Trades','Deliverable Volume'],axis = 1)
#print(data)
def transform(data):
    data['EPS'] = round(167,1)
    data['P.E ratio'] = data.Last/data.EPS
    data['Year'] = round(2008,1)

    return data

datareq = extract()
data1 = transform(datareq)

#Load the data
df = pd.DataFrame(data1)

df.to_csv("transformed_data_temp.csv")

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("log_temp_file.txt","a") as f:
        #f.write(timestamp + ',' + message + '\n')
        print(timestamp + ',' + message + '\n')
    
    
log("ETL Job Started")
log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
extracted_data

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
transformed_data 

log("Load phase Started")
df = pd.DataFrame(data1)
df.to_csv("transformed_data_temp.csv")
log("Load phase Ended")

log("ETL Job Ended")
