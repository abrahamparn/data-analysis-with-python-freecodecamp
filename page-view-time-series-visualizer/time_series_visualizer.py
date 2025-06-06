import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# TEMP FIX for Seaborn compatibility with new NumPy
if not hasattr(np, 'float'):
    np.float = float

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./fcc-forum-pageviews.csv", index_col=['date'], parse_dates=True)
# Clean data
max = df['value'].max()
min = df['value'].min()
print(f'max is {max} and min is {min}')
# finding the top 2.5% and bottom 2.5%
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
print(f"top 2.5% is {lower_bound} and min 2.5% is {upper_bound}")
value = df['value']
df = df[(value >= lower_bound) & (value <= upper_bound)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean()
    df_pivot = df_pivot.unstack()
    
    # Draw bar plot
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot[month_order]

    fig = df_pivot.plot(kind='bar', figsize=(15, 5)).figure

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 7))

    sns.boxplot(data = df_box, x='year', y='value', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    sns.boxplot(data = df_box, x='month', y='value', ax=ax[1], order=month_order)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
