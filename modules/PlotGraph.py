#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def plot_graph(predictions,y):
    predictions = scaler.inverse_transform(predictions)
    y = scaler.inverse_transform(y)
    mae = mean_absolute_error(y, predictions)
    print("Test MAE: %.6f" % mae)
    plt.figure(figsize=(15,6))
    plt.plot(predictions,color='red', label="Test set predictions" )
    plt.plot(y,color='green', label="Actual closing data")
    plt.legend()
    plt.ylabel('Price')
    plt.xlabel('Days' )
    plt.title ("Bitcoin close Price prediction")
    plt.show()

