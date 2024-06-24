import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    # Calculate the line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Extend the line to 'Year' = 2050
    target_x = 2050
    target_y = slope * target_x + intercept

    plot_original = plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit
    plt.plot([min(df['Year']), max(df['Year'])],
             [slope * min(df['Year']) + intercept, slope * max(df['Year']) + intercept], color='red',
             label='Line of Best Fit')

    # Plot the extended line
    plt.plot([max(df['Year']), target_x], [slope * max(df['Year']) + intercept, target_y], linestyle='--',
             color='green', label='Extended Line')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000] # copy of dataframe that fulfills condition

    # Calculate the line of best fit
    slope, intercept, _, _, _ = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])

    # Extend the line to 'Year' = 2050
    target_x = 2050
    target_y = slope * target_x + intercept

    plt.scatter(x=new_df['Year'], y=new_df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit
    plt.plot([min(new_df['Year']), max(new_df['Year'])],
             [slope * min(new_df['Year']) + intercept, slope * max(new_df['Year']) + intercept], color='red',
             label='Line of Best Fit')

    # Plot the extended line
    plt.plot([max(new_df['Year']), target_x], [slope * max(new_df['Year']) + intercept, target_y], linestyle='--',
             color='green', label='Extended Line')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (Inches)')
    plt.title('Rise in Sea Level')
    plt.grid(True)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()