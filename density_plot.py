# Pandas and numpy for data manipulation
import inline as inline
import pandas as pd
import numpy as np

# No warnings about setting value on copy of slice
pd.options.mode.chained_assignment = None

# Display up to 60 columns of a dataframe
pd.set_option('display.max_columns', 60)

# Matplotlib visualization
import matplotlib
import matplotlib.pyplot as plt

# %matplotlib inline

# Set default font size
plt.rcParams['font.size'] = 24

# Internal ipython tool for setting figure size
from IPython.core.pylabtools import figsize

# Seaborn for visualization
import seaborn as sns

sns.set(font_scale=2)

# Splitting data into training and testing
# from sklearn.model_selection import train_test_split


featuresClean = pd.read_csv('test2.csv')
features = featuresClean+0.00001*np.random.rand(3, 3)

# Extract the columns to  plot
# plot_data = features[['qwer', 'asdf', 'zxcv']]
plot_data = features

# Replace the inf with nan
plot_data = plot_data.replace({np.inf: np.nan, -np.inf: np.nan})

# # Rename columns
# plot_data = plot_data.rename(columns = {'log_Total GHG Emissions (Metric Tons CO2e)': 'log GHG Emissions'})

# Drop na values
plot_data = plot_data.dropna()


# Create a list of buildings with more than 100 measurements
types = plot_data.dropna(subset=['semester'])
types = types['Year'].value_counts()
types = list(types[types.values > 0].index)

# Plot of distribution of scores for building categories
figsize(12, 10)

# Plot each building
for b_type in types:
    # Select the building type
    subset = plot_data[plot_data['Year'] == b_type]

    # Density plot of Energy Star scores
    sns.kdeplot(subset['semester'].dropna(),
                label=b_type, shade=False, alpha=0.8)

# label the plot
plt.xlabel('Energy Star Score', size=20);
plt.ylabel('Density', size=20);
plt.title('Density Plot of Energy Star Scores by Building Type', size=28)
