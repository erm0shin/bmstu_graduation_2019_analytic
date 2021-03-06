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


featuresClean = pd.read_csv('test.csv')
features = featuresClean+0.00001*np.random.rand(3, 3)

# Extract the columns to  plot
plot_data = features[['qwer', 'asdf', 'zxcv']]

# Replace the inf with nan
plot_data = plot_data.replace({np.inf: np.nan, -np.inf: np.nan})

# # Rename columns
# plot_data = plot_data.rename(columns = {'log_Total GHG Emissions (Metric Tons CO2e)': 'log GHG Emissions'})

# Drop na values
plot_data = plot_data.dropna()


# Function to calculate correlation coefficient between two columns
def corr_func(x, y, **kwargs):
    r = np.corrcoef(x, y)[0][1]
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.2, .8), xycoords=ax.transAxes,
                size=20)


# Create the pairgrid object
# grid = sns.PairGrid(data=plot_data, size=3)
grid = sns.PairGrid(data=plot_data, height=3)

# Upper is a scatter plot
grid.map_upper(plt.scatter, color='red', alpha=0.6)

# Diagonal is a histogram
grid.map_diag(plt.hist, color='red', edgecolor='black')

# Bottom is correlation and density plot
grid.map_lower(corr_func)
grid.map_lower(sns.kdeplot, cmap=plt.cm.Reds)

# Title for entire plot
plt.suptitle('Pairs Plot of Energy Data', size=36, y=1)

# plt.draw()
plt.savefig('test.png')
