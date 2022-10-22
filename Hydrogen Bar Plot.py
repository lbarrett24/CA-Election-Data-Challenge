#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Import pandas
import pandas as pd
import numpy as np

excel_data = pd.read_csv('/Users/kaleemezatullah/Downloads/Hydrogen_Refueling_Stations.csv')

# Read the values of the file in the dataframe
df = pd.DataFrame(excel_data)
df


# In[18]:


df.tail()


# In[19]:


df.head()


# In[33]:


county= df['County'].unique()
#df.groupby('County').unique()
county=np.delete(county, -1)
county


# In[41]:


county_hydrogen_fuel= pd.DataFrame()

for i in range(len(county)):

    placeholder = pd.DataFrame() #placeholder dataframe
    placeholder['county'] = [county[i]] #state name into state column

    county_rows = df[df['County'] == str(county[i])] #group rows from the same state
    county_sum = county_rows['Fueling Positions'].sum() #sum of each age bin within the same state
    fuel = county_sum.sum() #add the sum of age bins together to get state population

    placeholder['total fueling'] = [fuel] #state population into state pop column

    county_hydrogen_fuel = pd.concat([county_hydrogen_fuel, placeholder], ignore_index = True) 
    #append placeholder to the state_prop data frame

county_hydrogen_fuel


# In[43]:


plot= county_hydrogen_fuel.plot.bar(x='county', y='total fueling')
# all counties not listed are 0

