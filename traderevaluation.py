import tensorflow as tf
import numpy as np
import pandas as pd


rawCSVData="/home/boma/risktestdata.csv"

rawDf=pd.read_csv(rawCSVData)

# print rawDf

"Start to normalize the data" \
"Set the buy as 0 and sell as 1"
for i,row in rawDf.iterrows():
    if rawDf.loc[i,'Type']=='buy':
        rawDf.loc[i,'Type']=0
    else :
        rawDf.loc[i,'Type']=1

"Omit the symbol column"
del rawDf['Item']

del rawDf['Ticket']

print rawDf
