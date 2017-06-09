from datetime import datetime
from time import time
import pandas as pd

def get_time_stamp(str):
    return long(datetime.strptime(str,"%Y.%m.%d %X").strftime("%s"))

def get_raw_df(raw_file_path):
    rawDf=pd.read_csv(raw_file_path)

# print rawDf

    "Start to normalize the data" \
    "Set the buy as 0 and sell as 1"
    for i,row in rawDf.iterrows():
        if rawDf.loc[i,'Type']=='buy':
            rawDf.loc[i,'Type']=0
        else :
            rawDf.loc[i,'Type']=1
        rawDf.loc[i,'StayTime']=(get_time_stamp(rawDf.loc[i,'Close Time'])-get_time_stamp(rawDf.loc[i,'Open Time']))/1000


    "Omit the symbol column"
    del rawDf['Item']

    del rawDf['Ticket']

    del rawDf['Close Time']

    del rawDf['Open Time']

    return rawDf
