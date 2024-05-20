
import calendar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from correlation_plot_args import CorrelationPlotArgs

def findDay(year, month, day):
    
    dayNumber = calendar.weekday(year, month, day)
     
    days = [0, 1, 2, 3, 4, 5, 6]
     
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

def normalization_with_min_max(col):
  max_val = np.max(col)
  min_val = np.min(col)

  return (col - min_val) / (max_val - min_val)

def calculateCorrelation(x: pd.Series, y: pd.Series):
    return np.corrcoef(x, y)

def plotScatterPlot(args: CorrelationPlotArgs):
    plt.scatter(args.x, args.y, alpha=0.5)
    plt.title(f"{args.title}. Correlation: {args.correlation:.4f}")
    plt.show()

def printCorrelation(colName: str, correlation: float):
    print(f"Correlation for {colName} = {correlation:.4f}")

def histogramErrors(y: np.ndarray, title: str):
    xTicksLabels = ['ManuallyTrained', 'ScikitModel', 'AvgModel']
    fig, ax = plt.subplots(1, 1)
    ax.plot(xTicksLabels, y)
    ax.set_xticks(xTicksLabels)
    ax.set_xticklabels(xTicksLabels, rotation='vertical', fontsize=18)
    ax.set_title(title)

def barPlot(y: np.ndarray, title: str):
    xTicksLabels = ['ManuallyTrained', 'ScikitModel', 'AvgModel']
    fig, ax = plt.subplots(1, 1)
    ax.bar(xTicksLabels, y)
    ax.set_xticks(xTicksLabels)
    ax.set_xticklabels(xTicksLabels, rotation='vertical', fontsize=18)
    ax.set_title(title)