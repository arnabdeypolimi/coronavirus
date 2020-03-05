from selenium import webdriver
import time
import pandas as pd
driver = webdriver.Chrome()
driver.get("https://www.worldometers.info/coronavirus/")
time.sleep(10)
data=driver.find_element_by_xpath('//*[@id="main_table_countries"]/tbody/tr')
print(data)
data=[[0,0,0,0,0,0,0,0]]
df=pd.DataFrame(data,columns=['country', 'total', 'new case', 'death', 'new_death', 'active_cases', 'recovered', 'critical'])
for tr in driver.find_elements_by_xpath('//*[@id="main_table_countries"]/tbody/tr'):
    tds=tr.find_elements_by_tag_name('td')
    temp=[]
    for td in tds:
        temp.append(td.text)
    data_to_append = {}
    for i in range(len(df.columns)):
        data_to_append[df.columns[i]] = temp[i]
    df = df.append(data_to_append, ignore_index=True)

driver.close()
df.to_csv('result_4_3_20.csv')