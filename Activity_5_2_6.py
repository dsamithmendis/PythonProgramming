import pandas as pd

# Load the data
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
col_name = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url, names=col_name)

# Find the maximum value for the 'petal-length' column
max_petal_length = dataset['petal-length'].max()
print("Maximum petal-length:", max_petal_length)
