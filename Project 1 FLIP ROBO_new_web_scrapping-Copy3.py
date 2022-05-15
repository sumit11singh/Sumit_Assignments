#!/usr/bin/env python
# coding: utf-8

# # Ques-3: IDMB top rated movies

# In[6]:


import pandas as pd


# In[7]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[8]:


from bs4 import BeautifulSoup
import requests


# In[9]:


page=requests.get("https://www.imdb.com/india/top-rated-indian-movies")


# In[ ]:


page


# In[ ]:


soup=BeautifulSoup(page.content)


# In[ ]:


soup


# In[8]:


title_name=[]
for i in soup.find_all('td',class_="titleColumn"):
    title_name.append(i.text)
    title_name


# In[ ]:


title_name


# In[11]:


rating=[]
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text)
    
        


# In[ ]:


rating


# In[13]:


year_of_release=[]
for i in soup.find_all('span',class_="secondaryInfo"):
    year_of_release.append(i.text)


# In[ ]:


year_of_release


# In[15]:


print(len(title_name),len(rating),len(year_of_release))


# In[16]:


df=pd.DataFrame({'Title':title_name,'Rating':rating,'Year_of_Release':year_of_release})
df


# In[20]:


df.iloc[0:100:]


# # Qsn-4: meesho

# In[21]:


page=requests.get("https://meesho.com/bags-ladies/pl/p7vbp")


# In[22]:


page


# In[23]:


soup=BeautifulSoup(page.content)


# In[24]:


soup


# In[29]:


product_name=[]
for i in soup.find_all('div',class_="Card__BaseCard-sc-b3n78k-0 fa-dWHP NewProductCard__CardStyled-sc-j0e7tu-0 fqpiyA NewProductCard__CardStyled-sc-j0e7tu-0 fqpiyA"):
    product_name.append(i.text)
    product_name


# In[ ]:


product_name


# In[31]:


product_name=[]
for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
    product_name.append(i.text)
    product_name


# In[ ]:


product_name


# In[37]:


price=[]
for i in soup.find_all('h5',class_="Text__StyledText-sc-oo0kvp-0 hiHdyy"):
    price.append(i.text)
    price


# In[ ]:


price


# In[42]:


discount=[]
for i in soup.find_all('span',class_="Text__StyledText-sc-oo0kvp-0 lnonyH"):
    discount.append(i.text)
    discount


# In[ ]:


discount


# In[44]:


import pandas as pd


# In[45]:


print(len(product_name),len(price),len(discount))


# In[47]:



df=pd.DataFrame({'Product':product_name,'Price':price,'Discount':discount})
df


# # Ques-8 www.nobroker.in

# In[21]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[22]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[23]:


page=requests.get("https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,&locality=Jayanagar,&locality=Rajajinagar")


# In[24]:


page


# In[25]:


soup=BeautifulSoup(page.content)


# In[ ]:


soup


# In[27]:


title=[]
for i in soup.find_all('span',class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"):
    title.append(i.text)
    title


# In[ ]:


title


# In[29]:


loc=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95"):
    loc.append(i.text)
    loc


# In[ ]:


loc


# In[31]:


area=[]
for i in soup.find_all('div',class_="flex flex-col w-33pe items-center border-r border-r-solid border-card-overview-border-color tp:w-half po:w-full last:border-r-1"):
    area.append(i.text)
    area


# In[ ]:


area


# In[33]:


price=[]
for i in soup.find_all('div',class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r-0"):
    price.append(i.text)
    price


# In[ ]:


price


# In[35]:


import pandas as pd


# In[37]:


print(len(title),len(loc),len(price))


# In[38]:


df=pd.DataFrame({'Title':title,'LOC':loc,'Price':price})
df


# # Ques-09  dineout.co.in :

# In[42]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[43]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[44]:


page=requests.get("https://www.dineout.co.in/delhi-restaurants/welcome-back")


# In[45]:


page


# In[ ]:


soup=BeautifulSoup(page.content)
soup


# In[47]:


title=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
     title.append(i.text)


# In[ ]:


title


# In[49]:


loc=[]
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    loc.append(i.text)


# In[ ]:


loc


# In[51]:


rating=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
    


# In[ ]:


rating


# In[53]:


img=[]
for i in soup.find_all('img',class_="no-img"):
    img.append(i['data-src'])


# In[ ]:


img


# In[55]:


cusine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cusine.append(i.text)


# In[ ]:


cusine


# In[57]:


print(len(title),len(loc),len(rating),len(img),len(cusine))


# In[58]:


df=pd.DataFrame({'Title':title,'LOC':loc,'RATING':rating,'IMG':img,'CUSINE':cusine})
df


# # Ques-10 https://www.bewakoof.com/women-tshirts?ga_q=tshirts . 

# In[59]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[60]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[61]:


page=requests.get("https://www.bewakoof.com/women-plain-t-shirts")


# In[62]:


page


# In[ ]:


soup=BeautifulSoup(page.content)
soup


# In[64]:


price=[]
for i in soup.find_all('span',class_="discountedPriceText"):
    price.append(i.text)


# In[ ]:


price


# In[66]:


product=[]
for i in soup.find_all('div',class_="productCardBox"):
    product.append(i.text)


# In[ ]:


product


# In[68]:


product=[]
for i in soup.find_all('div',class_="productCardBox"):
    product.append(i.text.split()[0:5])


# In[ ]:


product


# In[70]:


print(len(product),len(price))


# In[71]:


df=pd.DataFrame({'Product':product,'PRICE':price})
df


# # Ques-7 https://coreyms.com/

# In[72]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[73]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[74]:


page=requests.get("https://coreyms.com/")


# In[75]:


page


# In[ ]:


soup=BeautifulSoup(page.content)
soup


# In[77]:


heading=[]
for i in soup.find_all('h2',class_="entry-title"):
    heading.append(i.text)


# In[ ]:


heading


# In[79]:


time=[]
for i in soup.find_all('time',class_="entry-time"):
    time.append(i.text)


# In[ ]:


time


# In[81]:


content=[]
for i in soup.find_all('div',class_="entry-content"):
    content.append(i.text)


# In[ ]:


content


# In[83]:


print(len(heading),len(time),(content))


# In[84]:


df=pd.DataFrame({'Heading':heading,'TIME':time,'CONTENT':content})
df


# In[ ]:





# In[85]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[86]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[87]:


page=requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[88]:


page


# In[89]:


soup=BeautifulSoup(page.content)
soup


# In[90]:


header=[]
for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)


# In[91]:


header


# In[ ]:




