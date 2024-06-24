import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df.apply(lambda x: 1 if x['weight']/(x['height'] ** 2) > 25 else 0, axis=1)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df.apply(lambda x: 0 if x['cholesterol'] == 1 else 1, axis=1)
df['gluc'] = df.apply(lambda x: 0 if x['gluc'] == 1 else 1, axis=1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    # Drop columns I do not need in a new dataframe to be worked on
    melt_sample = df.drop(columns=['age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo'])

    # Melt my new dataframe while keeping the value of cardio
    melted_df = pd.melt(melt_sample, id_vars=['id', 'cardio'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    df_cat = melted_df.groupby(['variable', 'value', 'cardio',]).size().unstack(fill_value=0)

    # Draw the catplot with 'sns.catplot()'
    # Create the two subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    # Plot for cardio = 0 (Trend)
    cardio_0 = df_cat[0].unstack()  # dataframe for cardio = 0
    cardio_0.plot(kind='bar', ax=axes[0], legend=False)
    axes[0].set_title('cardio = 0')
    axes[0].tick_params(axis='x', rotation=0)  # Set x-axis label rotation

    # Plot for cardio = 0 (Trend)
    cardio_1 = df_cat[1].unstack()  # dataframe for cardio = 1
    cardio_1.plot(kind='bar', ax=axes[1], legend=False)
    axes[1].set_title('cardio = 1')
    axes[1].tick_params(axis='x', rotation=0)  # Set x-axis label rotation

    axes[0].set_ylabel('total')

    # Remove the box around the plot
    for ax in axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    # Create a common legend
    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, title='value', loc='upper right')
    # Adjust layout to remove any gap between subplots
    plt.subplots_adjust(wspace=0.05)

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt=".1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig