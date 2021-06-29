#!/usr/bin/env python
# coding: utf-8

# In[13]:


from selenium import webdriver
from pathlib import Path
import time
import datetime
import pandas as pd

#it doesn´t show the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)

#if the browser needs to be visible comment the 3 lines above and uncomment the line below
#driver = webdriver.Chrome()


# Define timestamp

# In[14]:


#type the Test execution start in the format year, month, day, hour, minute
epoch = datetime.datetime(2021, 4, 1, 10, 28).timestamp()
data = datetime.datetime.fromtimestamp(epoch)
#Riverbed needs int type to define time range
start_time = int(epoch/60)


# In[15]:


#one Riverbed Barchat report for payload type
payloads = [
    ("2-1051Cert*",1051,2),
    ("2-788Cert*",788,2),
    ("2-536Cert*",536,2),
    ("2-378Cert*",378,2),
    ("2-200Cert*",200,2),
    ("2-101Cert*",101,2),
    ("2-56Cert*",56,2),
    ("2-01Cert*",1,2),
    ("3-1051Cert*",1051,3),
    ("3-788Cert*",788,3),
    ("3-536Cert*",536,3),
    ("3-378Cert*",378,3),
    ("3-200Cert*",200,3),
    ("3-101Cert*",101,3),
    ("3-56Cert*",56,3),
    ("3-01Cert*",1,3),
    ("8-1051Cert*",1051,8),
    ("8-788Cert*",788,8),
    ("8-536Cert*",536,8),
    ("8-378Cert*",378,8),
    ("8-200Cert*",200,8),
    ("8-101Cert*",101,8),
    ("8-56Cert*",56,8),
    ("8-01Cert*",1,8),
    ("12-1051Cert*",1051,12),
    ("12-788Cert*",788,12),
    ("12-536Cert*",536,12),
    ("12-378Cert*",378,12),
    ("12-200Cert*",200,12),
    ("12-101Cert*",101,12),
    ("12-56Cert*",56,12),
    ("12-01Cert*",1,12),
    ("14-1051Cert*",1051,14),
    ("14-788Cert*",788,14),
    ("14-536Cert*",536,14),
    ("14-378Cert*",378,14),
    ("14-200Cert*",200,14),
    ("14-101Cert*",101,14),
    ("14-56Cert*",56,14),
    ("14-01Cert*",1,14),
    ("16-1051Cert*",1051,16),
    ("16-788Cert*",788,16),
    ("16-536Cert*",536,16),
    ("16-378Cert*",378,16),
    ("16-200Cert*",200,16),
    ("16-101Cert*",101,16),
    ("16-56Cert*",56,16),
    ("16-01Cert*",1,16),
    ("18-1051Cert*",1051,18),
    ("18-788Cert*",788,18),
    ("18-536Cert*",536,18),
    ("18-378Cert*",378,18),
    ("18-200Cert*",200,18),
    ("18-101Cert*",101,18),
    ("18-56Cert*",56,18),
    ("18-01Cert*",1,18),
    ("21-1051Cert*",1051,21),
    ("21-788Cert*",788,21),
    ("21-536Cert*",536,21),
    ("21-378Cert*",378,21),
    ("21-200Cert*",200,21),
    ("21-101Cert*",101,21),
    ("21-56Cert*",56,21),
    ("21-01Cert*",1,21),
    ("24-1051Cert*",1051,24),
    ("24-788Cert*",788,24),
    ("24-536Cert*",536,24),
    ("24-378Cert*",378,24),
    ("24-200Cert*",200,24),
    ("24-101Cert*",101,24),
    ("24-56Cert*",56,24),
    ("24-01Cert*",1,24),
        ]


# In[16]:

url = ""

folder = "{}_{}_{}__{}_{}".format(data.year, data.month, data.day, data.hour, data.minute)

dict_payloads = {}

images_place = Path.cwd()

#Barchart images folder
try:
    Path(folder).mkdir()                                  
except:
    print("Folder was not created")
    
images_place = Path(Path.cwd() / folder)
print(images_place)

size_control = 0

for payload, certificate, lines in payloads:
    print(payload)
    dict_payloads[payload] = [certificate, lines]
    #print(f"urlpath = '/sabrix/xmlinvoice' AND http.method = 'POST' AND received.http.request.header = 'neoload-payload-key:{payload}' | barchart -calc transactioncount(),avg(responsetime),percentile(responsetime, 50,95,99),min(responsetime),max(responsetime)")
    driver.get(f"https://[url}/#search:time={start_time}+31")
    time.sleep(20)  
    
    #capture the full page, code from https://pythonbasics.org/selenium-screenshot/
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X) 
    #increase browser width
    if size_control == 0:
        driver.set_window_size(S('Width')+800,S('Height')) # May need manual adjustment
        size_control += 1
    
    #capture Summary Page
    #driver.get(f"https://{url}/#search:time={start_time}+31")
    #time.sleep(20)   
    try:
        driver.find_element_by_xpath("//*[@id=\"contentBody\"]/div/div[2]/div[1]/form/div/div[1]/input").send_keys(f"urlpath = '/sabrix/xmlinvoice' AND http.method = 'POST' AND received.http.request.header = 'neoload-payload-key:{payload}'")
        #print("Query inserted")
    except:
        print("Could not insert query")

    try:
        driver.find_element_by_xpath("//*[@id=\"contentBody\"]/div/div[2]/div[1]/form/div/div[3]/button").click()
        #print("Button clicked")
    except:
        print("Could not click button") 

    time.sleep(15)
    
    image_name = payload[:-1] + "_Summary.png"
    final = Path(f"{images_place}/{image_name}")
    print(final)
    driver.find_element_by_tag_name('body').screenshot(f"{final}")  
    
    #capture Processing Time
    #driver.get(f"https://{url}/#search:time={start_time}+31")
    #time.sleep(20)   
    try:
        driver.find_element_by_xpath("//*[@id=\"contentBody\"]/div/div[2]/div[1]/form/div/div[1]/input").send_keys(f"urlpath = '/sabrix/xmlinvoice' AND http.method = 'POST' AND received.http.request.header = 'neoload-payload-key:{payload}' | processingtime -level auto -visualization pie_and_table")
        #print("Query inserted")
    except:
        print("Could not insert query")

    try:
        driver.find_element_by_xpath("//*[@id=\"contentBody\"]/div/div[2]/div[1]/form/div/div[3]/button").click()
        #print("Button clicked")
    except:
        print("Could not click button") 

    time.sleep(15)
    
    image_name = payload[:-1] + "_ProcessingTime.png"
    final = Path(f"{images_place}/{image_name}")
    print(final)
    #capture the full page, code from https://pythonbasics.org/selenium-screenshot/
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X) 
    #increase browser width
    if size_control == 0:
        driver.set_window_size(S('Width')+800,S('Height')) # May need manual adjustment
        size_control += 1
    driver.find_element_by_tag_name('body').screenshot(f"{final}")  
    
    #Capture Barchart           
    try:
        driver.find_element_by_xpath("//*[@id=\"contentBody\"]/div/div[2]/div[1]/form/div/div[1]/input").send_keys(f"urlpath = '/sabrix/xmlinvoice' AND http.method = 'POST' AND received.http.request.header = 'neoload-payload-key:{payload}' | barchart -calc transactioncount(),avg(responsetime),percentile(responsetime, 50,95,99),min(responsetime),max(responsetime)")
        #print("Query inserted")
    except:
        print("Could not insert query")

    try:
        driver.find_element_by_xpath("//*[@id=\"contentBody\"]/div/div[2]/div[1]/form/div/div[3]/button").click()
        #print("Button clicked")
    except:
        print("Could not click button") 

    time.sleep(20)

    image_name = payload[:-1] + "_Barchart.png"
    final = Path(f"{images_place}/{image_name}")
    print(final)
    #capture the full page, code from https://pythonbasics.org/selenium-screenshot/
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X) 
    #increase browser width
    if size_control == 0:
        driver.set_window_size(S('Width')+800,S('Height')) # May need manual adjustment
        size_control += 1
    driver.find_element_by_tag_name('body').screenshot(f"{final}")  

    try:
        transaction_count = float(driver.find_element_by_xpath("//*[@id=\"Transaction Count\"]/div[1]/table/tbody/tr[1]/td[2]/div/div[2]").text)
        transaction_count = int(transaction_count)
        print("Transaction Count: ",transaction_count)
        dict_payloads[payload].append(transaction_count)
    except:
        dict_payloads[payload].append("NotFound")
        print("Transaction Count not found")

    try:
        average = float(driver.find_element_by_xpath("//*[@id=\"Transaction Duration - Average, 50th, 95th and 99th Percentile, Minimum, Maximum\"]/div[1]/table/tbody/tr[1]/td[2]/div/div[2]").text)
        print("Average Transaction Duration: ",average)
        dict_payloads[payload].append(average)
    except:
        dict_payloads[payload].append("NotFound")
        print("Average Transaction Duration not found")
        
    try:
        percentile50 = float(driver.find_element_by_xpath("//*[@id=\"Transaction Duration - Average, 50th, 95th and 99th Percentile, Minimum, Maximum\"]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]").text)
        print("50th percentile: ",percentile50)
        dict_payloads[payload].append(percentile50)
    except:
        dict_payloads[payload].append("NotFound")
        print("50th percentile not found")

    try:
        percentile95 = float(driver.find_element_by_xpath("//*[@id=\"Transaction Duration - Average, 50th, 95th and 99th Percentile, Minimum, Maximum\"]/div[1]/table/tbody/tr[3]/td[2]/div/div[2]").text)
        print("95th percentile: ",percentile95)
        dict_payloads[payload].append(percentile95)
    except:
        dict_payloads[payload].append("NotFound")
        print("95th percentile not found")

    try:
        percentile99 = float(driver.find_element_by_xpath("//*[@id=\"Transaction Duration - Average, 50th, 95th and 99th Percentile, Minimum, Maximum\"]/div[1]/table/tbody/tr[4]/td[2]/div/div[2]").text)
        print("99th percentile: ",percentile99)
        dict_payloads[payload].append(percentile99)
    except:
        dict_payloads[payload].append("NotFound")
        print("99th percentile not found")        

    try:
        minimum = float(driver.find_element_by_xpath("//*[@id=\"Transaction Duration - Average, 50th, 95th and 99th Percentile, Minimum, Maximum\"]/div[1]/table/tbody/tr[5]/td[2]/div/div[2]").text)
        print("Minimum Transaction Duration: ",minimum)
        dict_payloads[payload].append(minimum)
    except:
        dict_payloads[payload].append("NotFound")
        print("Minimum Transaction Duration not found")

    try:
        maximum = float(driver.find_element_by_xpath("//*[@id=\"Transaction Duration - Average, 50th, 95th and 99th Percentile, Minimum, Maximum\"]/div[1]/table/tbody/tr[6]/td[2]/div/div[2]").text)
        print("Maximum Transaction Duration: ",maximum)
        dict_payloads[payload].append(maximum)
    except:
        dict_payloads[payload].append("NotFound")
        print("Maximum Transaction Duration not found")
  
    display(dict_payloads)    
    
list_index = [
    "Certificates",
    "Lines",
    "Transaction Count",
    "Average Transaction Duration",
    "50th percentile",
    "95th percentile",
    "99th percentile",
    "Minimum Transaction Duration",
    "Maximum Transaction Duration"
]
result_df = pd.DataFrame(dict_payloads, list_index)
display(result_df)
result_df = result_df.transpose()
display(result_df)
filename = "ResultRiverbed_{}_{}_{}_{}_{}.xlsx".format(data.year, data.month, data.day, data.hour, data.minute)
result_df.to_excel(filename)

