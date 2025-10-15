import pandas as pd 
import os
import sys
from pathlib import Path

def load_raw_data(file_path):

    raw_Path = Path(file_path)

    if os.path.exists(raw_Path) == False:
        print("RAW file not found at:" ,raw_Path)
        sys.exit(1)
    else:
        print("Found raw file",raw_Path)
        df= pd.read_csv(raw_Path)
        print("successefully read data")
        print("raws loaded:" ,df.shape[0])
        print("Columns:" ,df.shape[1])
        print(df.columns)
        return df

data_path = "data/raw/world_population.csv"
df=load_raw_data(data_path)

# def validate_schema(df):

#     selected_DF=df[["country","Year","Polulation"]]
#     print(selected_DF)
# validate_schema(df)