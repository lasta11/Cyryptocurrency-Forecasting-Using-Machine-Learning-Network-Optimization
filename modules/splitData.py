#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def splitTrainData(df,trainOrTest):
    test_ratio= 0.2  #20% testing data
    df_np= df.values
    split_point= int(len(df_np)* (1-test_ratio))
    if trainOrTest=='train':
        train_set= df_np[: split_point]
        return train_set
    if trainOrTest=='test':
        test_set= df_np[split_point:]
        return test_set

