# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('crypto-markets.csv')
data['date'] = pd.to_datetime(data['date'])
data = data.drop_duplicates(subset=['date'])
data.set_index('date', inplace=True)
missing_values = data.isnull().sum()
print("Missing values:\n", missing_values)


# Resample to daily frequency
data_daily = data.resample('D').ffill()

# Plot the data
data_daily['close'].plot(figsize=(12, 6), title='Bitcoin Closing Price')
plt.show()
