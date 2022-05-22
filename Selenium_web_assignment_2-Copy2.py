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


# In[ ]:


title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags[0:4]


# In[11]:


for i in title_tags:
    title=i.text
    job_title.append(title)


# In[ ]:


job_title[0:4]


# In[ ]:


company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:4]


# In[14]:


for i in company_tags:
    company=i.text
    company_name.append(company)


# In[ ]:


company_name[0:4]


# In[ ]:


experience_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span")
experience_tags[0:4]


# In[17]:


for i in experience_tags:
    experience=i .text
    experience_list.append(experience)


# In[ ]:


experience_list[0:4]


# In[ ]:


location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location'] /span[1]")
location_tags[0:4]


# In[20]:


for i in location_tags:
    location=i.text
    job_location_list.append(location)
    


# In[ ]:


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


# In[ ]:


title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags[0:4]


# In[43]:


for i in title_tags:
    title=i.text
    job_title.append(title)


# In[ ]:


job_title[0:4]


# In[ ]:


company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:4]


# In[46]:


for i in company_tags:
    company=i.text
    company_name.append(company)


# In[ ]:


company_name[0:4]


# In[ ]:


experience_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[1]")
experience_tags[0:4]


# In[49]:


for i in experience_tags:
    experience=i .text
    experience_list.append(experience)


# In[ ]:


experience_list[0:4]


# In[ ]:


location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")
location_tags[0:4]


# In[52]:


for i in location_tags:
    location=i.text
    job_location_list.append(location)


# In[ ]:


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

# In[179]:


get_ipython().system('pip install selenium')


# In[181]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[183]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[184]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[14]:


driver.get("https://www.flipkart.com/")


# In[15]:


search_field=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_field.send_keys('sunglasses')


# In[16]:


search_button=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_button.click()


# In[10]:


sunglasses_name=[]
prices_total=[]
sunglasses_specification=[]


# In[ ]:


sunglass_tags=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
sunglass_tags[0:4]


# In[10]:


for i in sunglass_tags:
    sunglass=i.text
    sunglasses_name.append(sunglass)


# In[ ]:


sunglasses_name[0:4]


# In[ ]:


specification_tags=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
specification_tags[0:4]


# In[13]:


for i in specification_tags:
    sunglass=i.text
    sunglasses_specification.append(sunglass)


# In[ ]:


sunglasses_specification[0:4]


# In[ ]:


price_tags=driver.find_elements_by_xpath("//div[@class='_30jeq3']")
price_tags[0:4]


# In[16]:


for i in price_tags:
    price=i.text
    prices_total.append(price)


# In[ ]:


prices_total[0:4]


# In[18]:


print(len(sunglasses_name),len(sunglasses_specification),len(prices_total))


# In[ ]:





# In[19]:


df1=pd.DataFrame({'SUNGLASSES_NAME':sunglasses_name,'SUNGLASSES_SPECIFICATION':sunglasses_specification, 'PRICES_TOTAL':prices_total})


# In[20]:


df1


# In[33]:


t_list=[]
for i in range(0,3):
    sunglass_tags=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for i in sunglass_tags:
        sunglass=i.text
        t_list.append(sunglass)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)
      


# In[ ]:


len(t_list)


# In[17]:


price_list=[]
for i in range(0,3):
    price_tags=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
    for i in price_tags:
        price=i.text
        price_list.append(price)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)
    


# In[ ]:


len(price_list)


# In[28]:


product_des=[]
for i in range(0,3):
    des_tags=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
    for i in des_tags:
        des=i.text
        product_des.append(des)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(product_des)


# In[35]:


df1=pd.DataFrame({'T_LIST':t_list,'PRICE_LIST':price_list,'PRODUCT_LIST':product_des})


# In[36]:


df1


# In[37]:


df1.head(100)


# In[ ]:





# # Ques-3: Naukri.com

# In[280]:


get_ipython().system('pip install selenium')


# In[281]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[232]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[233]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[114]:


driver.get("https://www.naukri.com/")


# In[115]:


search_field_designation=driver.find_element_by_class_name('suggestor-input ')
search_field_designation.send_keys('Data Scientist')


# In[116]:


search_field_location=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_field_location.send_keys('Delhi/NCR')


# In[117]:


search_button=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search_button.click()


# In[118]:


salary_filter_button=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[4]/div[2]/div[2]/label/p/span[1]')
salary_filter_button.click()


# In[119]:


job_title_list=[]
job_location_list=[]
company_name_list=[]
experience_list=[]


# In[120]:


title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
for i in title_tags:
    title=i.text
    job_title_list.append(title)


# In[ ]:


job_title_list[0:4]


# In[122]:


len(job_title_list)


# In[ ]:





# In[123]:


location_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]/span[1]')
for i in location_tags:
    location=i.text
    job_location_list.append(location)


# In[ ]:


job_location_list[0:4]


# In[ ]:


len(job_location_list)


# In[126]:


company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
for i in company_tags:
    company=i.text
    company_name_list.append(company)


# In[ ]:


company_name_list[0:4]


# In[ ]:


len(company_name_list)


# In[129]:


experience_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]/span[1]')
for i in experience_tags:
    experience=i.text
    experience_list.append(experience)


# In[ ]:


experience_list[0:4]


# In[ ]:


len(experience_list)


# In[132]:


df=pd.DataFrame({'JOB_TITLE':job_title_list,'JOB_LOCATION_LIST':job_location_list,'company_name_list':company_name_list,'EXPERIENCE_LIST':experience_list})


# In[133]:


df


# In[134]:


df.head(10)


# # Ques-6: Sneakers

# In[197]:


driver.get("https://www.flipkart.com/")


# In[198]:


sneakers_search=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
sneakers_search.send_keys('sneakers')


# In[199]:


search_button=driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_button.click()


# In[160]:


Brand_name=[]
for i in range(0,3):
    brand_tags=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
    for i in brand_tags:
        brand=i.text
        Brand_name.append(brand)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)
    
        
    


# In[ ]:


len(Brand_name)


# In[163]:


price_list=[]
for i in range(0,3):
    price_tags=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
    for i in price_tags:
        price=i.text
        price_list.append(price)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)
    


# In[ ]:


len( price_list)


# In[202]:


discount_price_list=[]
for i in range(0,3):
    discount_price_tags=driver.find_elements_by_xpath('//div[@class="_3Ay6Sb"]')
    for i in discount_price_tags:
        discount_price=i.text
        discount_price_list.append(price)
    next_button=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(discount_price_list)


# In[207]:


df2=pd.DataFrame({'BRAND_NAME':Brand_name,'price_list':price_list,'DISCOUNT_PRICE':discount_price})


# In[208]:


df2


# In[209]:


df2.head(100)


# # Ques-:7 https://www.myntra.com/shoes
# 

# In[28]:


get_ipython().system('pip install selenium')


# In[29]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
import time


# In[3]:


driver=webdriver.Chrome(r"C:\Webchrome_driver_1\chromedriver.exe")


# In[267]:


driver=webdriver.Chrome("chromedriver.exe")
time.sleep(2)


# In[30]:


driver.get("https://www.myntra.com/shoes")


# In[33]:


price_filter=driver.find_element_by_xpath('//*[@id="mountRoot"]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label')
price_filter.click()


# In[32]:


black_filter=driver.find_element_by_xpath('//*[@id="mountRoot"]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label')
black_filter.click()


# In[36]:


Brand_of_shoe=[]
for i in range(0,3):
    brand_tags=driver.find_elements_by_xpath('//span[@class="product-wishlistFlex product-actionsButton product-wishlist "]')
    for i in brand_tags:
        brand=i.text
        Brand_of_shoe.append(brand)
    next_button=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[12]/a')
    next_button.click()
    time.sleep(5)


# In[37]:


len(Brand_of_shoe)


# In[41]:


shoe_des=[]
for i in range(0,3):
    des_tags=driver.find_elements_by_xpath('//h4[@class="product-sizes"]')
    for i in des_tags:
        des=i.text
        shoe_des.append(des)
    next_button=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[12]/a')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(shoe_des)


# In[44]:


shoe_name=[]
for i in range(0,3):
    name_tags=driver.find_elements_by_xpath('//h3[@class="product-brand"]')
    for i in name_tags:
        name=i.text
        shoe_name.append(name)
    next_button=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[12]/a')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(shoe_name)


# In[49]:


price_list=[]
for i in range(0,3):
    price_tags=driver.find_elements_by_xpath('//div[@class="product-price"]')
    for i in price_tags:
        price=i.text
        price_list.append(price)
    next_button=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[12]/a')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(price_list)


# In[51]:


df=pd.DataFrame({'BRAND_SHOE':Brand_of_shoe,'SHOE_DES':shoe_des,'SHOE_NAME':shoe_name,'PRICE_LIST':price_list})


# In[52]:


df


# In[53]:


df.head(100)


# In[ ]:




