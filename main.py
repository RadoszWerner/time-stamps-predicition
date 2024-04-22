# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib

matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load the data
data = pd.read_csv('crypto-markets.csv')
btc_data = data[data['symbol'] == 'BTC'].copy()
btc_data.loc[:, 'date'] = pd.to_datetime(btc_data['date'])
btc_data.set_index('date', inplace=True)
missing_values = btc_data.isnull().sum()
print("Missing values:\n", missing_values)

# Resample to daily frequency
btc_data_daily = btc_data.resample('D').ffill()
#print(btc_data_daily)

# plt.plot(btc_data.index, btc_data['close'])
# plt.show()

# Train test split
# print(int(len(btc_data)*0.9))
# 1866 wszystkich wierszy
to_row = int(len(btc_data_daily) * 0.9)  # 1679 wierszy

training_data = list(btc_data_daily[0:to_row]['close'])
testing_data = list(btc_data_daily[to_row:]['close'])

model_predictions = []
n_test_obs = len(testing_data)

for i in range(n_test_obs):
    model = ARIMA(training_data, order=(4, 1, 0))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    model_predictions.append(yhat)
    actual_test_value = testing_data[i]
    training_data.append(actual_test_value)
    #print(output[0])
    #break

print(model_fit.summary())
# Visualization
plt.figure(figsize=(15, 9))
plt.grid(True)

date_range = btc_data_daily[to_row:].index
plt.plot(date_range, model_predictions, color='blue', marker='o',linestyle='dashed', label='BTC predicted price')
plt.plot(date_range, testing_data, color='red', label='BTC actual')
plt.title('Bitcoin price predicition')

plt.xlabel('Dates')
plt.ylabel('Closing prices')
#plt.plot(btc_data_daily[0:to_row]['close'], 'green', label='Train data')
#plt.plot(btc_data_daily[to_row:]['close'], 'blue', label='Test data')
plt.legend()
plt.show()
