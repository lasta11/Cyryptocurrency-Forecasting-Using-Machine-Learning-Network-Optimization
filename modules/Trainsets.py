#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def split_data(data,num_data=4,time=1):
    x,y= [], []  #creating two separate lists to appaned the train or test sets of x and y
    for i in range(len(data)-num_data-time+1):
        x.append(data[i:(i+num_data)])
        y.append(data[i+time+num_data-1])
    return np.array(x), np.array(y) 

