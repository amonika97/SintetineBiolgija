#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import pandas as pd
print("Pandas imported successfully, version: "+pd.__version__)
import scipy as sm
from scipy.stats import *
print("SciPy imported successfully, version: "+sm.__version__)

import seaborn as sns
print("Seaborn imported successfully, version: "+sns.__version__)
sns.set(style="whitegrid")

from sklearn.decomposition import PCA


# In[3]:


data_all = pd.read_csv("duomenys.csv")


# In[4]:


data_all = pd.read_csv("https://github.com/amonika97/SintetineBiolgija/blob/main/duomenys.csv")


# In[5]:


data_all = pd.read_csv('https://github.com/amonika97/SintetineBiolgija/blob/main/duomenys.csv')


# In[6]:


data_all = pd.read_csv('https://raw.githubusercontent.com/amonika97/SintetineBiolgija/main/duomenys.csv?token=ARVCIU4JMJPH7SCK7D5ARTS72PAPO
        ')


# In[7]:


data_all = pd.read_csv('https://raw.githubusercontent.com/amonika97/SintetineBiolgija/main/duomenys.csv?token=ARVCIU4JMJPH7SCK7D5ARTS72PAPO')


# In[8]:


data_all = pd.read_csv('https://raw.githubusercontent.com/amonika97/SintetineBiolgija/main/duomenys.csv?token=ARVCIU32VAWF4XJWZSF7KQC72PBCG')


# In[1]:


data_all = pd.read_csv('https://raw.githubusercontent.com/amonika97/SintetineBiolgija/main/Breast_cancer_data.csv?token=ARVCIUYP37VXUXYDTS62YE272PNO6')


# In[2]:


import pandas as pd
print("Pandas imported successfully, version: "+pd.__version__)
import scipy as sm
from scipy.stats import *
print("SciPy imported successfully, version: "+sm.__version__)

import seaborn as sns
print("Seaborn imported successfully, version: "+sns.__version__)
sns.set(style="whitegrid")

from sklearn.decomposition import PCA


# In[3]:


data_all = pd.read_csv('https://raw.githubusercontent.com/amonika97/SintetineBiolgija/main/Breast_cancer_data.csv?token=ARVCIUYP37VXUXYDTS62YE272PNO6')


# In[7]:


data_all = pd.read_csv('/Users/Vartotojas/Desktop/Breast_cancer_data.csv')


# In[8]:


data_all.head()


# In[16]:


diagnosis_rows = data_all["diagnosis"] == "1"
diagnosis_data = data_all[diagnosis_rows]['mean_radius']
diag_rows = data_all['diagnosis'] == '0'
diag_data = data_all[diag_rows]['mean_radius']


# In[17]:


(t, p) = ttest_ind(diagnosis_data, diag_data)
print("P-Value for the measurement: "+str(p))


# In[15]:


ax = sns.boxplot(x="diagnosis", y="mean_radius", data=data_all[diagnosis_rows | diag_rows])


# In[18]:


data_all.shape()


# In[19]:


data_all.head()


# In[21]:


data_all.shape


# In[22]:


data_all.columns


# In[25]:


data_all=data_all.dropna(axis=1)


# In[26]:


data_all['diagnosis'].value_counts()


# In[27]:


sns.countplot(data_all['diagnosis'], label="Count")


# In[43]:


plot= sns.boxplot (x= "diagnosis" , y= "mean_texture", data=data_all, showfliers=False)

plot.set_title('Graph of texture mean vs diagnosis of tumor') 


# In[44]:


plot= sns.boxplot (x= "diagnosis" , y= "mean_radius", data=data_all, showfliers=False)

plot.set_title('Graph of mean radius vs diagnosis of tumor')


# In[45]:


plot= sns.boxplot (x= "diagnosis" , y= "mean_perimeter", data=data_all, showfliers=False)

plot.set_title('Graph of mean perimeter vs diagnosis of tumor')


# In[46]:


plot= sns.boxplot (x= "diagnosis" , y= "mean_area", data=data_all, showfliers=False)

plot.set_title('Graph of mean area vs diagnosis of tumor')


# In[47]:


plot= sns.boxplot (x= "diagnosis" , y= "mean_smoothness", data=data_all, showfliers=False)

plot.set_title('Graph of mean smoothness vs diagnosis of tumor')


# In[ ]:

                       
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
print("Pandas imported successfully, version: "+pd.__version__)
import scipy as sm
from scipy.stats import *
print("SciPy imported successfully, version: "+sm.__version__)

import seaborn as sns
print("Seaborn imported successfully, version: "+sns.__version__)
sns.set(style="whitegrid")

from sklearn.decomposition import PCA


# In[2]:


data_all = pd.read_csv('/Users/Vartotojas/Desktop/Breast_cancer_data.csv')


# In[3]:


data_all.head()


# In[4]:


data_all.mean()


# In[6]:


data_all.median()


# In[7]:


data_all.mode()


# In[11]:


data_all.std()


# In[12]:


data_all.var()


# In[13]:


data_all.describe()


# In[14]:


data_all.describe(include='all')


# In[25]:



y = data_all.diagnosis
# drop the column 'id' as it is does not convey any useful info
# drop diagnosis since we are separating labels and features 
list = ['diagnosis']
# X includes our features
X = data_all.drop(list,axis = 1)
# get the first ten features
data_dia = y
data = X
data_std = (data-data.mean()) / (data.std()) # standardization
# get the first 10 features
data = pd.concat([y,data_std.iloc[:,0:10]],axis=1)
data = pd.melt(data,id_vars='diagnosis',
 var_name='features',
 value_name='value')
# make a violin plot
plt.figure(figsize=(10,10))
sns.violinplot(x='features', y='value', hue='diagnosis', data=data,split=True, inner='quart')
plt.xticks(rotation=90)


# In[26]:


from matplotlib import pyplot as plt


# In[27]:



y = data_all.diagnosis
list = ['diagnosis']
X = data_all.drop(list,axis = 1)
data_dia = y
data = X
data_std = (data-data.mean()) / (data.std()) 
data = pd.concat([y,data_std.iloc[:,0:10]],axis=1)
data = pd.melt(data,id_vars='diagnosis',
 var_name='features',
 value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x='features', y='value', hue='diagnosis', data=data,split=True, inner='quart')
plt.xticks(rotation=90)


# In[ ]:





# In[35]:


import numpy as np
f,ax = plt.subplots(figsize=(18, 18))
matrix = np.triu(X.corr())
sns.heatmap(X.corr(), annot=True, linewidths=.5, fmt= '1f',ax=ax, mask=matrix)


# In[38]:


num_missing = (data_all == 0).sum()


# In[39]:


print(num_missing)


# In[ ]:




