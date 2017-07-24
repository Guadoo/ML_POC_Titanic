# Data analysis and wrangling
import pandas as pd







# Acquire data
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df, test_df]

# Analyze by describing data
print(train_df.columns.values)

# Preview the data
print(train_df.head())
train_df.head()