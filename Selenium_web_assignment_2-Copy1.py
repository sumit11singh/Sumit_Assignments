#!/usr/bin/env python
# coding: utf-8

# # Ques-1 DATA analyist

# In[2]:


get_ipython().system('pip install selenium')


# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[5]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[6]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[5]:


driver.get("https://www.naukri.com/")


# In[6]:


search_field_designation=driver.find_element_by_class_name('suggestor-input ')
search_field_designation.send_keys('data analyst')
                                  


# In[7]:


search_field_location=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_field_location.send_keys('Bangalore')


# In[8]:


search_button=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search_button.click()


# In[9]:


job_title=[]
company_name=[]
job_location_list=[]
experience_list=[]


# In[10]:


title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags[0:4]


# In[11]:


for i in title_tags:
    title=i.text
    job_title.append(title)


# In[12]:


job_title[0:4]


# In[13]:


company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:4]


# In[14]:


for i in company_tags:
    company=i.text
    company_name.append(company)


# In[15]:


company_name[0:4]


# In[16]:


experience_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span")
experience_tags[0:4]


# In[17]:


for i in experience_tags:
    experience=i .text
    experience_list.append(experience)


# In[18]:


experience_list[0:4]


# In[19]:


location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location'] /span[1]")
location_tags[0:4]


# In[20]:


for i in location_tags:
    location=i.text
    job_location_list.append(location)
    


# In[21]:


job_location_list[0:4]


# In[22]:


print(len('job_title'),len(company_name),len(experience_list),len(job_location_list))


# In[ ]:





# In[23]:


df=pd.DataFrame({'JOB_TITLE':job_title,'COMPANY_NAME':company_name,'EXPERIENCE_LIST':experience_list,'JOB_LOCATION_LIST':job_location_list})


# In[24]:


df


# In[25]:


df.iloc[0:10,]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[48]:


get_ipython().system('pip install selenium')


# In[49]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[50]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[51]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[52]:


driver.get("https://www.myntra.com/shoes")


# In[ ]:


filter_price=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul")
filter_price.click()


# In[32]:


filter_colour=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label")
filter_colour.click()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Ques-2 DATA SCIENTIST

# In[33]:


get_ipython().system('pip install selenium')


# In[34]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[35]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[36]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[37]:


driver.get("https://www.naukri.com/")


# In[38]:


search_field_designation=driver.find_element_by_class_name('suggestor-input ')
search_field_designation.send_keys('Data Scientist')


# In[39]:


search_field_location=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_field_location.send_keys('Bangalore')


# In[40]:


search_button=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search_button.click()


# In[41]:


job_title=[]
company_name=[]
job_location_list=[]
experience_list=[]


# In[42]:


title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags[0:4]


# In[43]:


for i in title_tags:
    title=i.text
    job_title.append(title)


# In[44]:


job_title[0:4]


# In[45]:


company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:4]


# In[46]:


for i in company_tags:
    company=i.text
    company_name.append(company)


# In[47]:


company_name[0:4]


# In[48]:


experience_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[1]")
experience_tags[0:4]


# In[49]:


for i in experience_tags:
    experience=i .text
    experience_list.append(experience)


# In[50]:


experience_list[0:4]


# In[51]:


location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
location_tags[0:4]


# In[52]:


for i in location_tags:
    location=i.text
    job_location_list.append(location)


# In[53]:


job_location_list[0:4]


# In[54]:


print(len('job_title'),len(company_name),len(experience_list),len(job_location_list))


# In[55]:


df=pd.DataFrame({'JOB_TITLE':job_title,'COMPANY_NAME':company_name,'EXPERIENCE_LIST':experience_list,'JOB_LOCATION_LIST':job_location_list})


# In[56]:


df


# In[57]:


df.iloc[0:10,]


# # Ques-4 FLIPKART.COM

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[4]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[5]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[6]:


driver.get("https://www.flipkart.com/")


# In[8]:


search_field=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_field.send_keys('sunglasses')


# In[9]:


search_button=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_button.click()


# In[10]:


sunglasses_name=[]
prices_total=[]
sunglasses_specification=[]


# In[9]:


sunglass_tags=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
sunglass_tags[0:4]


# In[10]:


for i in sunglass_tags:
    sunglass=i.text
    sunglasses_name.append(sunglass)


# In[11]:


sunglasses_name[0:4]


# In[12]:


specification_tags=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
specification_tags[0:4]


# In[13]:


for i in specification_tags:
    sunglass=i.text
    sunglasses_specification.append(sunglass)


# In[14]:


sunglasses_specification[0:4]


# In[15]:


price_tags=driver.find_elements_by_xpath("//div[@class='_30jeq3']")
price_tags[0:4]


# In[16]:


for i in price_tags:
    price=i.text
    prices_total.append(price)


# In[17]:


prices_total[0:4]


# In[18]:


print(len(sunglasses_name),len(sunglasses_specification),len(prices_total))


# In[ ]:





# In[19]:


df1=pd.DataFrame({'SUNGLASSES_NAME':sunglasses_name,'SUNGLASSES_SPECIFICATION':sunglasses_specification, 'PRICES_TOTAL':prices_total})


# In[20]:


df1


# In[12]:


t_list=[]
for i in range(0,3):
    sunglass_tags=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for i in sunglass_tags:
        sunglass=i.text
        t_list.append(sunglass)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)
      


# In[13]:


len(t_list)


# In[ ]:





# In[ ]:





# In[11]:


p_list=[]
for i in range(0,3):
    price_tags=driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    for i in price_tags:
        price=i.text
    p_list.append(price)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(4)
    
    
    
    


# In[12]:


len(p_list)


# In[ ]:





# In[ ]:





# In[ ]:





# # Ques-5: Iphone_11

# In[145]:


get_ipython().system('pip install selenium')


# In[146]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[147]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[148]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[149]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-power- adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace")


# In[151]:


ratings_iphone_11=[]
reviews_summary=[]
full_reviews=[]


# In[152]:


rating_tags=driver.find_elements_by_xpath("//div[@class='_3LWZlK _1BLPMq']")
rating_tags[0:4]


# In[153]:


for i in rating_tags:
    rating=i.text
    ratings_iphone_11.append(rating)


# In[154]:


ratings_iphone_11


# In[155]:


review_summary_tags=driver.find_elements_by_xpath("//p[@class='_2-N8zT']")
review_summary_tags[0:4]


# In[156]:


for i in review_summary_tags:
    review=i.text
    reviews_summary.append(review)


# In[157]:


reviews_summary[0:4]


# In[158]:


full_review_tags=driver.find_elements_by_xpath("//div[@class='t-ZTKy']")
full_review_tags[0:4]


# In[47]:


for i in full_review_tags:
    review=i.text
    full_reviews.append(review)


# In[46]:


full_reviews[0:10]


# In[161]:


df=pd.DataFrame({'RATING_IPHONE_11':ratings_iphone_11,'REVIEW_SUMMARY':reviews_summary,'FULL_REVIEW':full_reviews})


# In[162]:


df


# In[163]:


print(len(ratings_iphone_11),len(reviews_summary),len(full_reviews))


# In[ ]:




