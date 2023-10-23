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


Split the data into training and testing set. 


import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('cw1data.csv')

# Define the input variables (X) and the output variable (y)
X = data.drop('y', axis=1)  # Features
y = data['y']  # Target variable

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shape of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)