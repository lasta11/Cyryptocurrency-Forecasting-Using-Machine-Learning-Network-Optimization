#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def subPlots(df):
    df.plot(subplots=True,figsize=(8,8))
    plt.legend(loc='best')

