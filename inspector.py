import pandas as pd
# ask the user for the file pathe
user_input = input("Enter CSV path: ")

try:
  # load the csv
  data = pd.read_csv(user_input)

  print("================================\nDATASET INSPECTOR\n================================")
  print("\nDataset Information\n-------------------")

  # pandas operations
  # Rows & Columns
  print(f"Rows: {data.shape[0]}")
  print(f"Columns: {data.shape[1]}\n")

  # Column Names & Data Types
  column_names = data.columns
  print("Column Names & Data Types:\n-------------------------------")
  for i in range(len(column_names)):
    print(f"Column {column_names[i]} is of type { data[column_names[i]].dtype}")

  # Missing Values by Row
  print("\nMissing Values\n--------------")
  missing_values = data.isna().sum().sum()
  nan_rows = data[data.isna().any(axis=1)]
  print(f"Total missing values {missing_values}")
  print(f"Affected rows: {len(nan_rows)}\n")

  # Duplicate rows
  print("Duplicate Rows\n--------------")
  duplicate = data.duplicated() #duplicate values
  print(f"Duplicate Rows: {len(duplicate)}")
  for i in range(len(duplicate)):
    if (duplicate[i]==True):
      print(f"Row \"{i}\" is a duplicate\n")
    

  # check unique values
  print("Unique Values\n-------------")
  unique_values = []
  for i in range(len(column_names)):
    value = len(data[column_names[i]].unique())
    unique_values.append({column_names[i] : value})
    print(f"Column {column_names[i]} has {unique_values[i].get(column_names[i])} unique_values")

  # print("\nConstant Columns\n----------------")
  # unique_full = []
  # for i in range(len(column_names)):
  #   value = data[column_names[i]].unique()
  #   unique_full.append(value)
  #   if ((len(unique_full[i])==2)):
  #     if((str(unique_full[i][0])=="nan") | (str(unique_full[i][1])=="nan")):
  #       print(f"'{column_names[i]}' is a column of constant values")
      
  print("\nConstant Columns\n----------------")
  for i in range(len(column_names)):
    if (data[column_names[i]].nunique() == 1):
      print(f"'{column_names[i]}' is a column of constant values")
      print(f"constant value: {data[column_names[i]].values}")

  # # spot indexes
  # print("\nPotential Index Columns\n-----------------------")
  # if ((len(data[column_names[0]].values)) == (data.shape[0])):
  #   print(f"Column {column_names[0]} is an index column\n")

except FileNotFoundError:
  print("enter a valid file path.")

