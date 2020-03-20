#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd


# ### Bring in data that is in wrong schema

# In[76]:


#Read in the csv that you need to change
#Remember that windows uses "\" to seperate paths, but you need to switch them to "/"

DFWrongSchema = pd.read_excel('C:/Users/Eric/Documents/Work from Home/Resident Survey PowerBI Updates/FY2020 Survey Data WORKING COPY.xlsx')


# In[77]:


#Grab the wrong schemas current order
DFWrongSchemaCols = DFWrongSchema.columns.tolist()


# ### Bring in data that is in correct schema

# In[78]:


#Read in the excel file containing the right schema, the one you want your bad data to end up matching
DFRightSchema = pd.read_excel('C:/Users/Eric/Documents/Work from Home/Resident Survey PowerBI Updates/Correct2020schema.xlsx')


# In[79]:


ColsCorrectOrder = DFRightSchema.columns


# In[80]:


DFWrongSchema['Unnamed: 154'] = ""
DFWrongSchema['Unnamed: 177'] = ""
DFWrongSchema['Unnamed: 68'] = ""
DFWrongSchema['Unnamed: 212'] = ""
DFWrongSchema['Unnamed: 74'] = ""
DFWrongSchema['Unnamed: 180'] = ""
DFWrongSchema['Unnamed: 214'] = ""
DFWrongSchema['Unnamed: 72'] = ""
DFWrongSchema['Unnamed: 183'] = ""
DFWrongSchema['Unnamed: 213'] = ""
DFWrongSchema['Unnamed: 175'] = ""
DFWrongSchema['Unnamed: 106'] = ""
DFWrongSchema['Unnamed: 66'] = ""
DFWrongSchema['Unnamed: 86'] = ""
DFWrongSchema['Unnamed: 172'] = ""
DFWrongSchema['Unnamed: 70'] = ""
DFWrongSchema['Unnamed: 105'] = ""
DFWrongSchema['Unnamed: 87'] = ""
DFWrongSchema['OLDETC_ID'] = ""


# ### Rearrange columns according to right schema

# In[81]:


DFWrongSchema = DFWrongSchema[ColsCorrectOrder]


# ### Export the data
# 

# In[83]:


# Now we export the data as a csv for PowerBI to use and append
DFWrongSchema.to_csv('DataRearrangedCorrectSchema.csv')

