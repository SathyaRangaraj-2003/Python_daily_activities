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

#cleaning
df_csv.columns = df_csv.columns.str.lower().str.replace(' ','_')
#df_csv

#TASK 2 : DATA MERGING
#concatenation:

new_data = pd.concat([df_csv , df_json] , ignore_index = True)
#print(new_data)


#year_column

new_data['year'] = ["2023" if idx < len(df_csv)  else "2024" for idx in range(len(new_data))]
#print(new_data)


#month consistency:

df_json = new_data[new_data.month.isin(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])]
print(df_json)


#sorting

#chronologically by month
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
new_data['month'] = pd.Categorical(new_data['month'],categories = month_order , ordered = True)
new_data.sort_values(['year','month'],inplace=True)
new_data


#TASK 3 : Data Analysis
#performance metrics

new_data['pct_diff_target'] = ((new_data['passengers_carried'] - new_data['target_passengers']) / new_data['target_passengers']) * 100
new_data


#Target Non-Achievement:

not_achieved = new_data[new_data['pct_diff_target'] < 0 ]
not_achieved[['month','year','pct_diff_target']]


#Annual Summaries:

total_passenger = new_data.groupby('year')['passengers_carried'].sum().astype(int)
total_passenger

total_flights = new_data.groupby('year').flights_operated.sum().astype(int)
total_flights

average = new_data.groupby('month',observed=True)['pct_diff_target'].mean()
average







