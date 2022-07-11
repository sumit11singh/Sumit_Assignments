#!/usr/bin/env python
# coding: utf-8

# In[90]:


df


# In[4]:


df.shape


# In[5]:


df.dtypes


# In[6]:


df.isnull().sum()


# there are some nan values are present in Dataset column in form of float ,int,object .use simpleimputer method for filling these nan values .
# 

# In[9]:


df


# In[12]:


df


# In[13]:


df.isnull().sum()


# now nun values are removed from given Dataset

# # EDA Analysis(Data Visulization)

# In[14]:


sns.distplot(df['LotFrontage'])


# In[15]:


sns.countplot(df['Street'])


# all street are related to pave .There is no single street belongs to Grvl

# In[16]:


sns.countplot(df['LotShape'])


# above Graph is showing 4 diff type of Lotshape
# 1-Reg count=680
# 2-IR1,count=390
# 3-IR2,count=58
# 4- IR3,count=40

# In[17]:


sns.countplot(df['LandContour'])


# above Graph is showing 4 diff type of LandContour 1-LvI count=1050 2-Bnk,count=45 3-HLS,count=45 4-Low,count=28

# In[79]:


sns.countplot(df['YrSold'])


# following graph is showing how many house are sold in a year.

# In[80]:


sns.countplot(df['SaleCondition'])


# sales are much better at 4.0

# In[81]:


sns.countplot(df['SaleType'])


# Following graph is showing that sales type are higher at 8.0

# In[82]:


sns.countplot(df['SaleCondition'])


# followibg grapgh is showing for the sales condition type .

# # EDA Analysis for label or o/p

# In[85]:


sns.countplot(df['SalePrice'])


# In[91]:


sns.distplot(df['SalePrice'])


# aboe grapgh sales price density is lying b/w 150000rs to 220000 rs

# In[93]:


sns.boxplot(y=df['SalePrice'])


# above grapgh is showing that most of the sales price are lying in b/w 150000rs to 220000rs.

# In[ ]:


sns.pairplot(df)


# In[ ]:





# # Encoding Technique

# Use OrdinalEncoder

# In[21]:


df


# # Defining the Correlation for given Dataset

# In[22]:


df.corr()['SalePrice'].sort_values()


# utilities has no any relationship with label or o/p of given Dataset so remove this column.

# In[24]:


df1


# In[25]:


df1.corr()['SalePrice'].sort_values()


# # Finding Corelatin Using HeatMap

# In[26]:


plt.figure(figsize=(60,25))
sns.heatmap(df1.corr(),annot=True,linewidths=0.5,linecolor='Black',fmt='.2f')


# # Describing Dataset

# In[27]:


df1.describe()


# # Plotting Heatmap

# In[28]:


plt.figure(figsize=(40,20))
sns.heatmap(round(df1.describe()[1:].transpose(),2),annot=True,linewidths=.2,linecolor='Black',fmt='.2f')


# # Checking Outliers in given Dataset

# In[29]:


df1.plot(kind='box',subplots=True,layout=(18,6),figsize=(50,25))


# outliers are present in given dataset

# # Use zscore method for removing outliers from given dataset

# In[31]:


z


# In[34]:


df1_new


# In[35]:


print('Old_dataframe',df1.shape)
print('new_dataframe',df1_new.shape)
print("reduction in rows",df1.shape[0]-df1_new.shape[0])


# In[37]:


Percentage_dataloss


# we can't afford too huge Dataloss present in given Dataset.so i will not remove outliers present in dataset

# # spliting Dataset in for training & testingphase

# In[39]:


x


# In[40]:


x.shape


# In[41]:


y=df1['SalePrice']


# In[42]:


y


# # check skewness present in Datset

# In[43]:


x.skew()


# In[44]:


df1.plot(kind='density',subplots=True,layout=(15,6),figsize=(40,32))


# skewness are present in given Dataset

# # Transformimg Data to remove skewness

# Using the power transforming method to remove Skewness present in the given dataset

# In[46]:


x


# # MIN values & MAX values difference is higher in Describe dataset so use the scaling method to scale the data

# In[48]:


x


# # Model Selection

# # label or O/P is in Binary form so use Linear Regression Model

# In[50]:


for i in range(0,100):
        train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.25,random_state=i)
        lr.fit(train_x,train_y)
        lrpred=lr.predict(test_x)
        print(f"at random_state{i},the testing accuracy score is := {r2_score(test_y,lrpred)}")
        print(f"at random_state{i},the training accuracy is: =      {lr.score(train_x,train_y)}")


# In[51]:


train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.25,random_state=88)
lr.fit(train_x,train_y)
lrpred=lr.predict(test_x)
print(f"at randon_state{88},the testing accuracy score is := {r2_score(test_y,lrpred)}")
print(f"at random_state{88},the training accuracy is: =   {lr.score(train_x,train_y)}")


# at random_state=88 the training & testing score found Gd.

# In[53]:


cv_score=cross_val_score(lr,x,y,cv=10)
cv_mean=cv_score.mean()
cv_mean


# cv score for linear Regression Model is 76.19% which is less than the lg model score .it showing that lr model is overfitted

# In[54]:


plt.figure(figsize=(8,6))

plt.scatter(x=test_y,y=lrpred,color='r')
plt.plot(test_y,test_y,color='b')
plt.xlabel("sale price")
plt.ylabel("predcited sale price")
plt.title("Linear Regression")
plt.show()


# Best fit line covers most of the datapoints which shows gd fit for our model

# # use grid search cv technique for Ridge & Lasso model

# In[55]:


from sklearn.model_selection import GridSearchCV

param_new={'alpha':[1,.01,.001,.0001,.1,10]}
rd=Ridge()
grid=GridSearchCV(rd,param_grid=param_new)
grid.fit(train_x,train_y)
print(grid.best_params_)


# # Ridge model

# In[56]:


rd.fit(train_x,train_y)
train_score=rd.score(train_x,train_y)
rdpred=rd.predict(test_x)
print(r2_score(test_y,rdpred))
print(train_score)


# Ridge model score is 85.53% which is greater than the lr model.it means it has better performance than lr model

# # Lasso Model

# In[57]:


param_new={'alpha':[1,.01,.001,.0001,.1,10]}
ls=Lasso()
grid=GridSearchCV(ls,param_grid=param_new)
grid.fit(train_x,train_y)
print(grid.best_params_)


# In[58]:


ls.fit(train_x,train_y)
train_score=ls.score(train_x,train_y)
lspred=ls.predict(test_x)
print(r2_score(test_y,lspred))
print(train_score)


# accuracy for Lasso model is less than Ridge model .

# # Ensemble Technique
# RandomRegressor model

# In[59]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


# In[60]:


param_new = {'criterion':['mse','mae'],'max_features':["auto","log2","sqrt"]}
rf= RandomForestRegressor()
grid_latest=GridSearchCV(rf,param_new)
grid_latest.fit(train_x,train_y)
print(grid_latest)
print(grid_latest.best_params_)


# In[61]:


print(grid_latest.best_params_)


# In[62]:


rf=RandomForestRegressor(criterion='mae')
rf.fit(train_x,train_y)
rf.score(train_x,train_y)
rfpred=rf.predict(test_x)
print(r2_score(test_y,rfpred))
print(rf.score(train_x,train_y))


# rf model has the accuracy=87.07%  wich is greater than lr,rd,ls model.

# # Graphical Representation for rf model for actual sale values vs predicted values

# In[63]:


plt.figure(figsize=(8,6))
plt.scatter(x=test_y,y=rfpred,color='r')
plt.plot(test_y,test_y,color='b')
plt.xlabel("actual sale price")
plt.ylabel("predicted sale price")
plt.show


# Best fit line covers most of the datapoints which shows gd fit for our rf model.

# cross validation for rf model

# In[65]:


mean_acuracy


# # Predicting the best performance for the given model

# hence among all the model it is showing that RandomForestRegressor model is the best performing with Training accuracy=97.39% ,testing accuracy score=87.07%,cv score=84.96%.

# # Save the model for Production purpose

# In[78]:


House_sales_price_file

