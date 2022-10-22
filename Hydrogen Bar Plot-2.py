#!/usr/bin/env python
# coding: utf-8

# In[58]:


# Import pandas
import pandas as pd
import numpy as np

excel_data = pd.read_csv('/Users/kaleemezatullah/Downloads/Hydrogen_Refueling_Stations.csv')

# Read the values of the file in the dataframe
df = pd.DataFrame(excel_data)
df


# In[59]:


df.tail()


# In[60]:


df.head()


# In[33]:


county= df['County'].unique()
#df.groupby('County').unique()
county=np.delete(county, -1)
county


# In[61]:


county_hydrogen_fuel= pd.DataFrame()

for i in range(len(county)):

    placeholder = pd.DataFrame() #placeholder dataframe
    placeholder['county'] = [county[i]] #state name into state column

    county_rows = df[df['County'] == str(county[i])] #group rows from the same state
    county_sum = county_rows['Fueling Positions'].sum() #sum of each age bin within the same state
    fuel = county_sum.sum() #add the sum of age bins together to get state population

    placeholder['total hydrogen stations'] = [fuel] #state population into state pop column

    county_hydrogen_fuel = pd.concat([county_hydrogen_fuel, placeholder], ignore_index = True) 
    #append placeholder to the state_prop data frame

county_hydrogen_fuel


# In[62]:


plot= county_hydrogen_fuel.plot.bar(x='county', y='total hydrogen stations')
# all counties not listed are 0


Southern California and the Bay area are the leaders by far when it comes to avaialbility of hydrogen refueling stations.
Approximately 50% of all the hydrogen stations in CA are private and not accessible to the public which are used specifically
used only for the private sector. These private stations are typically used by industrial purposes in refining and chemical processes. With a
Prop30 approval, hydrogen vehicles would likely increase in number requiring more public infrastructure for refueling. This would also
allow the industrial sector to tap into these stations as well making working conditions more convenient. Hydrogen fuel cells are major
proponents for the ZEV sector since their only waste is water and air. 
