#!/usr/bin/env python
# coding: utf-8

# In[ ]:


scaler = MinMaxScaler()
def scale(data):  #toget the scaled data back
    scaled_data = scaler.transform(data)
    return scaled_data
scalers = {}
for i in range (x_train.shape[2]):
    scalers[i] = MinMaxScaler()
    x_train[:, :, i] = scalers[i].fit_transform(x_train[:, :, i])
for i in range(x_test.shape[2]):
    x_test[:, :, i] = scalers[i].transform(x_test[:, :, i])

trainY_btc = scaler.fit_transform(trainY_btc)
testY_btc = scale(testY_btc)

