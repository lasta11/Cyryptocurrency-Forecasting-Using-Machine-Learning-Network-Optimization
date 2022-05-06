#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def train_model(y):
    model= Sequential()
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    history = model.fit(x_train, y, epochs =60, verbose =1)
    return history, model

