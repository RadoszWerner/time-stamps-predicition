import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random

class create_subsets():
    def __init__(self):
        pass
    
    def create_random_subsets(self, data, num_subsets=40, window_size=10):
        subsets = []
        num_rows = len(data)
        for _ in range(num_subsets):
            start_index = random.randint(0, num_rows - window_size)
            subset = data.iloc[start_index:start_index+window_size]
            subsets.append(subset)
        return subsets
    
    # Creating table of 10-day datasets
    def create_dataset_table(self, subsets):
        dataset_ids = []
        dates_list = []
        close_values_list = []

        for i, subset in enumerate(subsets):
            dataset_ids.append(i + 1)

            dates = subset.index.date.tolist()  # Extract only the date part
            close_values = subset['close'].tolist()

            dates_list.append(dates)
            close_values_list.append(close_values)

        table = pd.DataFrame({
            'dataset_id': dataset_ids,
            'dates': dates_list,
            'close_values': close_values_list
        })

        return table
    
    # Adding label collumn containing information about rise/ fall
    def add_label_column(self, table):
        for index, row in table.iterrows():
            close_day_7 = row['close_values'][6]
            close_day_10 = row['close_values'][9]

            label = int(close_day_10 > close_day_7)

            table.at[index, 'rise'] = label

        return table