# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('crypto-markets.csv')
btc_data = data[data['symbol'] == 'BTC'].copy()
btc_data.loc[:, 'date'] = pd.to_datetime(btc_data['date'])
btc_data.set_index('date', inplace=True)
missing_values = btc_data.isnull().sum()
print("Missing values:\n", missing_values)


# Resample to daily frequency
btc_data_daily = btc_data.resample('D').ffill()
print(btc_data)

# Plot the data
btc_data_daily['close'].plot(figsize=(12, 6), title='Bitcoin Closing Price')
plt.show()
