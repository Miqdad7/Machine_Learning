import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

fifa_complete_df=pd.read_csv('fifa23.csv')
fifa_df=fifa_complete_df.iloc[:51].copy()
countries=np.unique(fifa_df['Nationality'])

cle=LabelEncoder()
country_labels=cle.fit_transform(fifa_df['Nationality'])
fifa_df['Country_Label']=country_labels

country_mappings={}
for index,labels in enumerate(cle.classes_):
    country_mappings[labels]=index
print(country_mappings)

print(fifa_df[['Known As','Age','Overall','Nationality','Country_Label']])

