import pandas as pd
# ask the user for the file pathe
user_input = input("Enter CSV path: ")

# pandas operations
# Rows & Columns
def data_shape_operation():
  print(f"Rows: {data.shape[0]}")
  print(f"Columns: {data.shape[1]}\n")

# Column Names & Data Types
def data_type_operation():  
  print("Column Names & Data Types:\n-------------------------------")
  for i in range(len(column_names)):
    print(f"Column {column_names[i]} is of type { data[column_names[i]].dtype}")

# Missing Values by Row
def missing_values_operation():
  print("\nMissing Values\n--------------")
  missing_values = data.isna().sum().sum()
  nan_rows = data[data.isna().any(axis=1)]
  print(f"Total missing values {missing_values}")
  print(f"Affected rows: {len(nan_rows)}\n")

# Duplicate rows
def duplicate_values_operation():
  print("Duplicate Rows\n--------------")
  duplicate = data.duplicated() #duplicate values
  print(f"Duplicate Rows: {duplicate.sum()}")
  for i in range(len(duplicate)):
    if (duplicate[i]==True):
      print(f"Row \"{i}\" is a duplicate\n")
    
# check unique values
def unique_values_operation():
  print("Unique Values\n-------------")
  unique_values = []
  for i in range(len(column_names)):
    value = len(data[column_names[i]].unique())
    unique_values.append({column_names[i] : value})
    print(f"Column {column_names[i]} has {unique_values[i].get(column_names[i])} unique_values")

# check for constant columns
def constant_column_operation():
  print("\nConstant Columns\n----------------")
  for i in range(len(column_names)):
    if (data[column_names[i]].nunique() == 1):
      print(f"'{column_names[i]}' is a column of constant values")
      print(f"constant value: {data[column_names[i]].values}")

# spot indexes
def spot_indexes_operation():
  print("\nPotential Index Columns\n-----------------------")
  for i in range(len(column_names)):
    if data[column_names[i]].is_unique:
      if pd.api.types.is_numeric_dtype(data[column_names[i]]):
        if (data[column_names[i]].diff().dropna()==1).all():
          print(f"column \"{column_names[i]}\" may be an index column")        

try:
  # load the csv
  data = pd.read_csv(user_input)

  print("================================\nDATASET INSPECTOR\n================================")
  print("\nDataset Information\n-------------------")

  # geting the column names
  column_names = data.columns

  data_shape_operation()
  data_type_operation()
  missing_values_operation()
  duplicate_values_operation()
  unique_values_operation()
  constant_column_operation()
  spot_indexes_operation()

except FileNotFoundError:
  print("enter a valid file path.")

