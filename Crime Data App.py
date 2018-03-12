
# coding: utf-8


import pandas as pd
import os
from sodapy import Socrata

un = os.environ['MYSOCRATAUSER'] #Get username from env variable
pw = os.environ['MYSOCRATA'] 

client = Socrata("data.cityofchicago.org", "Cpx1LuOdxYRwllKvAxE14mcx1", username = un, password = pw) #Connect to chicago data portal


results = client.get("6zsd-86xi", limit=2000) #Specify what data I want and max rows

results_df = pd.DataFrame.from_records(results) #Store the results in panda data frame object

results_df[['community_area','description']] #Filter by community area and description

#results_df #Prints full table results

