
# coding: utf-8

# In[159]:


from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import numpy as np
from os import listdir
from datetime import datetime as dt

def main():

    # In[160]:

    link = 'https://www.worldometers.info/coronavirus/#countries'


    # In[161]:


    req = get(link)
    page = BeautifulSoup(req.content, 'html.parser')


    # In[151]:


    table = page.find('table', {"id": "main_table_countries_today"})

    headers = [i.text for i in table.findAll('th')]

    lines = table.tbody.findAll('tr')


    # In[152]:


    rows = []
    for line in lines:
        td = line.findAll('td')
        row = [tds.text.strip() for tds in td]
        rows.append(row)
            
        
    df = pd.DataFrame(rows, columns=headers)
    df.insert(0, 'TimeStamp', dt.now().replace(microsecond=0))


    # In[153]:


    to_be_replaced = [ 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths',
        'TotalRecovered', 'ActiveCases', 'Serious,Critical']


    # In[154]:


    for column_name in to_be_replaced:
        df[column_name] = df[column_name].str.replace('+', '')
        df[column_name] = df[column_name].str.replace(',','')
        df[column_name] = pd.to_numeric(df[column_name])


    # In[155]:


    df.sort_values(by='NewCases', ascending=False)
    df.fillna(0, inplace=True)


    # In[156]:


    df['DailyIncreaseTax'] = (df.TotalCases)/(df.TotalCases- df.NewCases) - 1

    df.replace(np.inf, 0, inplace=True)


    # In[157]:


    df.sort_values('DailyIncreaseTax', ascending=False)


    # In[158]:


    if 'corona_data.csv' in listdir():
        df.to_csv('corona_data.csv', mode='a', header=False, index=False)
    else:
        df.to_csv('corona_data.csv', header=True, index=False)

if __name__=='__main__':
    main()