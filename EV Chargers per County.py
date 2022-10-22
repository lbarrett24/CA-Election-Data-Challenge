#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import plotnine as p9
from plotnine import theme, element_text


# In[15]:


ev_chargers = pd.read_csv("EV Chargers_Last updated 01-31-2022.csv")
ev_chargers


# In[124]:


ev_chargers2 = ev_chargers.drop('Total', axis=1)
ev_chargers2.head()


# In[126]:


ev_chargers2 = ev_chargers.drop('Total', axis=1)
ev_chargers2["Public Chargers"] = (ev_chargers2["Public Level 1"] + ev_chargers2["Public Level 2"] + 
                                   ev_chargers2["Public DC Fast"])
ev_chargers2["Private Chargers"] = (ev_chargers2["Shared Private Level 1"] + ev_chargers2["Shared Private Level 2"] + 
                                   ev_chargers2["Shared Private DC Fast"])
ev_chargers2 = ev_chargers2.drop([59])
ev_chargers2.tail()


# In[128]:


charger_list = list(ev_chargers2) 
charger_list.remove('County')
charger_list.remove('Public Chargers')
charger_list.remove('Private Chargers')

ev_df = pd.DataFrame()
for i in range(len(charger_list)):
    placeholder = pd.melt(ev_chargers2, id_vars = ['County'], value_vars = [charger_list[i]])
    ev_df = pd.concat([ev_df, placeholder], ignore_index = True)
    
ev_df


# In[76]:


(p9.ggplot(ev_df, p9.aes(x = 'County', y = 'value')) 
+ p9.geom_col() 
+ p9.labs(title = "EV Chargers per County", x = "County", y = "Count")
+ theme(axis_text_x=element_text(rotation=45, hjust = 1))
+ p9.facet_wrap('~variable'))


# In[89]:


import plotly.express as px


# In[141]:


ev_pub = ev_chargers2[["County","Public Level 1", "Public Level 2", "Public DC Fast", "Public Chargers"]]
ev_pub.tail()


# In[142]:


ev_priv = ev_chargers2[["County","Shared Private Level 1", "Shared Private Level 2", "Shared Private DC Fast", 
                       "Private Chargers"]]
ev_priv.head()


# In[134]:


px.bar(ev_df, x="County",y=["value"], color="variable", 
       labels={'_value': 'Count'}, title='All EV Chargers per County')


# In[136]:


px.bar(ev_pub, x="County",y=["Public Level 1", "Public Level 2", "Public DC Fast"], 
       labels={'value': 'Count'}, title='Public EV Chargers per County')


# In[138]:


px.bar(ev_priv, x="County",y=["Shared Private Level 1", "Shared Private Level 2", "Shared Private DC Fast"],
      labels={'value': 'Count'}, title='Private EV Chargers per County')

