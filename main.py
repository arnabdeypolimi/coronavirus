from selenium import webdriver
import time
import pandas as pd
from datetime import date

def clean_data(df):
    # df = df.drop('Unnamed: 0', axis=1)

    df['new case'] = df['new case'].str.replace('+', '')
    df['new_death'] = df['new_death'].str.replace('+', '')

    df['death'] = df['death'].str.replace(',', '')
    df['active_cases'] = df['active_cases'].str.replace(',', '')
    df['recovered'] = df['recovered'].str.replace(',', '')
    df['critical'] = df['critical'].str.replace(',', '')
    df['total'] = df['total'].str.replace(',', '')

    df = df.drop(df.index[0])
    df = df.drop(df.index[len(df)-1])

    df = df.fillna(0)
    return df

path='daily_data/result_'

today = str(date.today())
driver = webdriver.Chrome()
driver.get("https://www.worldometers.info/coronavirus/")
time.sleep(10)
data=driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr')
# data=driver.find_element_by_xpath('//*[@id="main_table_countries_yesterday"]/tbody/tr')
print(data)
data=[[0,0,0,0,0,0,0,0]]
df=pd.DataFrame(data,columns=['country', 'total', 'new case', 'death', 'new_death','recovered', 'active_cases',  'critical'])
for tr in driver.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr'):
    tds=tr.find_elements_by_tag_name('td')
    temp=[]
    for td in tds:
        temp.append(td.text)
    data_to_append = {}
    for i in range(len(df.columns)):
        data_to_append[df.columns[i]] = temp[i]
    df = df.append(data_to_append, ignore_index=True)

driver.close()

df_cleaned=clean_data(df)
output=path+today+'.csv'
df_cleaned.to_csv(output)