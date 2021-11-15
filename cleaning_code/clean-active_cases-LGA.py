import pandas as pd
import re

PATH_FILE = "../raw_datasets/active_cases_by_lga.csv"
PATH_FILE_OUT = "../cleaned_datasets/active_cases_by_lga.csv"

df = pd.read_csv(PATH_FILE)
df = df.drop(df.columns[[1,2,4,5,6,7,8,9,10]], axis=1) #remove unwanted rows
pattern = '[^a-zA-Z\s\n	]' #regex to remove brackets
dropList = []
for index in df.index:
    oldLGA = df.at[index,'LGA']
    if oldLGA.find(')') != -1: #remove brackets
        pattern = '\([^)]*\)'
        newtext = re.sub(pattern, ' ', oldLGA)
        df.at[index,'LGA']=newtext 
    else:
        dropList.append(index)
df = df.drop(df.index[dropList])
df.to_csv(PATH_FILE_OUT, index=False)
print(df.to_string())