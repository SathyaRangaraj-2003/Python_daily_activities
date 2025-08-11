#activity_07 => pandas

import pandas as pd

df = pd.read_csv('student.csv')

result = df[((df['gender']=='male') & (df['mark'] > 70)) & ((df['class']=='Four') | (df['class']=='Five'))]

print(result)

'''
print(df.loc[((df['gender']=='male') & (df['mark'] > 70)) & ((df['class']=='Four') | (df['class']=='Five'))])

'''