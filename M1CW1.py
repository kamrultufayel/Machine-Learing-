#import data 


import pandas as pd

# Load the dataset
data = pd.read_csv('cw1data.csv')

# Display the first few rows of the dataset to inspect the data
print(data.head())

#Visualise the data


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('cw1data.csv')

# Assuming the target variable is in a column named 'target'
# If 'target' is categorical, you may want to encode it numerically for visualization
# For example, using label encoding:
# data['target'] = data['target'].astype('category').cat.codes





plt.scatter(y_test, linear_predictions, label='Linear Regression', alpha=0.5)
plt.scatter(y_test, tree_predictions, label='Decision Tree Regression', alpha=0.5)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.legend()
plt.show()
