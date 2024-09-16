import pandas as pd

# Load the CSV file
file_path = 'C:/Users/Josh/Downloads/Results_Data.csv'
data = pd.read_csv(file_path)

# Convert each column into a list
columns_as_lists = {col: data[col].tolist() for col in data.columns}

# Print the lists for each column
for col_name, col_list in columns_as_lists.items():
    print(f"{col_name}: {col_list}")