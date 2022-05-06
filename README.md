# Crypto Currency forecasting using LSTM model
In this project, using Long Term Short Memory (LSTM),  a model to predict the future price of a cryptocurrency.

# Overview
As any good investor it is important to know regarding the high prices, low prices, hold and correct sell of the cryptocurrency to increase the profitability.
 * The objective of this project is to build a model to predict the future price of any cryptocurrency using any datasets of four other cryptocurrencies using LSTM model.
 * For this project, I have approached by taking correlation between the prices of cryptocurrencies to find the best fit to use dataset. This project holds a way to collect datasets from any finance website and modify or train them accordingly to predict the future prices.  
 * This repository holds a set of code, that can be used to collect, prepare, and train the prices of cryptocurrencies.

# Summary of Workdone

* Data:
   * The datasets used in this repository are collected online using WebReader library of pandas. The main four datasets are the dataframes of particular cyrptocurrency, for example: Bitcoin : Date, CLosing price, Opening Price, Volume of the day, and Adj closing price of the day.
   * Four datasets of Cryptocurrency, From start date- End date, (Number of days X 5 columns)
   * Input: CSV files of timeseries and prices
   * Size of datasets: The size of datasets varies how many number of days/ years taken in consideration.
   
* Preprocessing/ Clean up:
   * For this project the closing price of all the cryptocurrencies have been collected to make a new dataframe with same date. Therefore, while collecting the datasets for different cryptocurrencies having same start and end date is necessary for further steps.

* Data Visualization:
   * In this project the price difference over the years and how each of them are related to each other. The crypto currencies have high correlation values.

![Data Visualization]

(https://github.com/lasta11/DATA-4380-Project-I/blob/main/Example_images/coins.png)

Correlation:
https://github.com/lasta11/DATA-4380-Project-I/blob/main/Example_images/Correlation.png

* Problem Formulation:
  * Crypto Forecast LSTM model:
  * Input: Timeseries data of prices of all four currencies
  * Output: Predicted price frame
  * Adam optimizer used

* Training
   * the model was trained for 60 epochs taking about 5 minutes.
   * Training model is shown under "modules" of the notebook.
 
 * Results:
 https://github.com/lasta11/DATA-4380-Project-I/blob/main/Example_images/Prediction.png
 
 # Conclusions:
  * From the loses, the model demonstrates that the predicted price of the crypto currency tend to match the actual price of the coins on the timeseries data. However, the predicted price have Test MAE: 2064.500914. The volume of the price change over the day can be used to get close predicted price of the currency.
  
 # Future Work:
 * Continue to work on using volume and other factors of price change to keep in model for more acccurate predictions.
 * Modify the model by splitting the data between 1-2 week timeframe and observe the predicted data over small number of time.

# How to reproduce results

* modules
   * prepData.py : Function to collect data and modify to make single datasets with necessary columns of all dataframes
   * dataVisualize.py:Function to visualize price change over time periods
   * Correlation.py : Function helping to see if the cryptocurrencies selected have correlation
   * splitData.py : Function to split data into test and train
   * scaledData.py : Function to normalize the data and transform test and train datasets
   * Trainsets.py : Function to build the model
   * TrainModel.py : Function to train the model
   * Plotgraph.py : Plot the price difference of predicted prive Vs. Actual price


*main.ipynb 
  * Consists of:
      * Background
      * Motivation 
      * Importing the libraries
      * Data Collection
      * Data Representation / Correlation Analysis
      * Loading and scaling data
      * Building model
      * Training model
      * Result Plots
      * Loss evaluation

# Software Setup
* Packages used in notebook: pandas, matplotlin, numpy, tensorflow, sklearn, seaborn, keras, datetime
