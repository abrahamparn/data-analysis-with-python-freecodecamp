import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv", index_col=['Year'])

    # Create scatter plot
    fig,ax = plt.subplots(figsize=(16, 9))
    plt.scatter(x=df.index, y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope, intercept, *_ = linregress(x=df.index, y=df["CSIRO Adjusted Sea Level"])
    x = pd.Series(range(1880, 2051))
    y= slope * x + intercept
    plt.plot(x, y, 'r')

    # Create second line of best fit (2000 to 2050)
    df_2000 = df[df.index >= 2000]
    slope_2000, intercept_2000, *_ = linregress(df_2000.index, df_2000['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = slope_2000 * x_recent + intercept_2000
    plt.plot(x_recent, y_recent, 'r')


    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()