
import calendar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def findDay(year, month, day):
    
    dayNumber = calendar.weekday(year, month, day)
     
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
     
    return days[dayNumber]


def cyclical_encoding(data, col: str, max_val: float):
    data[col + '_sin'] = np.sin(2 * np.pi * data[col] / max_val)
    data[col + '_cos'] = np.sin(2 * np.pi * data[col] /  max_val)
    return data

def plot_columns(ds: pd.DataFrame):
    columns = ds.columns
    for i, col in enumerate(columns):
        plt.figure(i)
        sns.histplot(ds[col], kde=True)