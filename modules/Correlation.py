#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def dataRepresentation(df):
    df.corr()
    dataplot = sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
    plt.show()

