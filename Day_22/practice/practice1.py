#mini assessment:

#importing

import csv
import json
import pandas as pd

#TASK 1 : dataloading and cleaning
#loading

df_csv = pd.read_csv('old_airline_data_2023.csv')
df_json = pd.read_json('new_airline_data_2024.json',)
print(df_json)
'''
#identify all missing values

missing_values = df_json.isnull().sum()
#print(missing_values)


#numeric columns

df_json['Flights Operated'] = df_json['Flights Operated'].fillna(df_json['Flights Operated'].mean())

df_json.iloc[:,2:] = df_json.iloc[:,2:].fillna(df_json.iloc[:,2:].mean())

#print(df_json)


#drop simultaneously(all three numeric columns)

#df_json = df_json.dropna(subset=['Flights Operated', 'Passengers Carried' , 'Target Passengers'] , how = 'all',axis=0) 
#print(df_json)


#validate the month

df_json = df_json[df_json.iloc[:,0].isin(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])]
#print(df_json)



#standardization:

df_json.columns = df_json.columns.str.lower()
df_json.columns = df_json.columns.str.replace(' ','_')
df_json['month'] = df_json['month'].str.capitalize()
#print(df_json)


#Duplicate Handling:

df_json = df_json.groupby('month',as_index = False).first()
#print(df_json)


#TASK 2 : DATA MERGING
#concatenation:

new_data = pd.concat([df_csv , df_json] , ignore_index = True)
#print(new_data)


#year_column

new_data['year'] = ["2023" if idx < len(df_csv)  else "2024" for idx in range(len(new_data))]
#print(new_data)


#month consistency:

#print(df_csv.columns)
#print(df_json.columns)


print(new_data.iloc[:,2:5])




'''




