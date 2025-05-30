
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[6]:


ms = pd.DataFrame.from_csv('../data/microsoft.csv')
ms['MA10'] = ms['Close'].rolling(10).mean()
ms['MA50'] = ms['Close'].rolling(50).mean()
ms = ms.dropna()
ms.head()


# In[7]:


ms['Shares'] = [1 if ms.loc[ei,'MA10']>ms.loc[ei,'MA50'] else 0 for ei in ms.index]


# In[12]:


ms['Close1'] = ms['Close'].shift(-1)
ms['Profit'] =[ ms.loc[ei,'Close1'] - ms.loc[ei,'Close'] if ms.loc[ei,'Shares']== 1 else 0 for ei in ms.index]
ms['Profit'].plot()
plt.axhline(y=0, color='black')


# In[13]:


ms['wealth'] = ms['Profit'].cumsum()
ms.tail()


# In[20]:


ms['wealth'].plot()
plt.title('Total money you win is {}'.format(ms.loc[ms.index[-2],
                                                    'wealth']))


# In[ ]:





# In[ ]:




