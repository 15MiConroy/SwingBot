import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

positive_growth_required = 5
negative_growth_required = 1
num_days = 14

def is_target_stock(ticker, positive_growth_required, negative_growth_required, num_days):
    end = dt.datetime.today().date()
    start = end - dt.timedelta(days=num_days + 1)
    df = web.DataReader(ticker, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df['growth'] = (df['Adj Close'] - df['Open']) / df['Open'] * 100
    df['is_short_day'] = df['growth'] <= negative_growth_required
    return((sum(df['is_short_day'] & (df['Date'].dt.date != end)) == (len(df) - 1)) & \
        (df.loc[df['Date'].dt.date == end, 'growth'].values[0] >= positive_growth_required))

#stocks = ['TSLA', 'TVIX', 'HEAR']
[stock for stock in stocks if is_target_stock(stock, positive_growth_required, negative_growth_required, num_days)]
