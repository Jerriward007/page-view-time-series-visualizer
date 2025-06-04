import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def draw_line_plot():
    # Import data
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

    # Clean data
    df = df[(df['value'] >= df['value'].quantile(0.025)) & 
            (df['value'] <= df['value'].quantile(0.975))]

    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change these two lines)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Import data
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

    # Clean data
    df = df[(df['value'] >= df['value'].quantile(0.025)) & 
            (df['value'] <= df['value'].quantile(0.975))]

    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')

    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig = df_grouped.plot(kind='bar', figsize=(12, 8)).figure
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Import data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

    # Clean data
    df = df[(df['value'] >= df['value'].quantile(0.025)) & 
            (df['value'] <= df['value'].quantile(0.975))]

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.strftime('%b')
    df['month_num'] = df['date'].dt.month

    df.sort_values('month_num', inplace=True)

    # Draw box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
