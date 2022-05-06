#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def data_preparation(tickers,start_date,end_date=dt.datetime.now()):
    end_date= end_date
    start_date= start_date
    df_list=[]
    close_list=[]
    for i in range(len(tickers)):
        crypto_data= web.DataReader(tickers[i],data_source='yahoo',start=start_date, end=end_date)
        df_list.append(crypto_data)
    for i in range(len(df_list)):
        closing_price=df_list[i]['Close'].values
        to_list= closing_price.tolist()
        close_list.append(to_list)
    indexing=[]
    for i in range(1,(len(close_list[1])+1)):
        indexing.append(i)

    data={tickers[0]:close_list[0],tickers[1]:close_list[1],tickers[2]:close_list[2],tickers[3]:close_list[3]}
    
    df_tickers=pd.DataFrame(data,index=indexing)
    return df_tickers

