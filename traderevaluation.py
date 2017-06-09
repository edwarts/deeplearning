import tensorflow as tf
import numpy as np
import pandas as pd
import utilities as ut

rawCSVData="risktestdata.csv"

raw_df=ut.get_raw_df(rawCSVData)

# build up the training dataset and the model size is 13x13

matrix13=raw_df.head(13)

print matrix13.as_matrix()



