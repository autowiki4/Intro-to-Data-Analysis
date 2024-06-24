import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                index_col = 0)

# Clean data
# Calculate the threshold values
top_threshold = df['value'].quantile(0.975) # top 2.5%
bottom_threshold = df['value'].quantile(0.025) # bottom 2.5%

# Filter out the rows outside the thresholds
df = df[(df['value'] > bottom_threshold) & (df['value'] < top_threshold)]

# Convert the index to datetime
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Plot the data
    fig, axis = plt.subplots(figsize=(20, 6))
    df.plot(kind='line', color='red', ax=axis)

    # Set title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Set x-axis ticker locator for 6-month intervals
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))

    # Rotate x-axis labels for better readability (optional)
    plt.xticks(rotation=45)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    monthly_avg_views = df.resample('M').mean()

    # Group the data by month and year
    monthly_avg_views['Year'] = monthly_avg_views.index.year
    monthly_avg_views['Month'] = monthly_avg_views.index.month
    monthly_avg_views_grouped = monthly_avg_views.groupby(['Year', 'Month']).mean()

    # Copy and modify data for monthly bar plot
    df_bar = monthly_avg_views_grouped.unstack()

    import calendar
    # Convert month numbers to month names and remove the 'value' part
    df_bar.columns = [calendar.month_name[label[1]] for label in df_bar.columns]

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)

    # Set the x-axis label
    plt.xlabel('Years')

    # Set the y-axis label
    plt.ylabel('Average Daily Page Views')

    # Set the legend title
    plt.legend(title='Months')



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

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot for Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Value')

    # Plot for Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Value')

    # Adjust the x-axis tick labels for the month-wise plot
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    axes[1].set_xticklabels(month_labels)



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

