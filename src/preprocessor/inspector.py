import pandas as pd
# ask the user for the file pathe
user_input = input("Enter CSV path: ")


# load the csv path
def load_csv(path):
  try:
    data = pd.read_csv(path)  
  except FileNotFoundError:
    print("File Not Found")
  except pd.errors.EmptyDataError:
    print("Empty CSV")
  except pd.errors.ParserError:
    print("Malformed CSV")
  return data
data = load_csv(user_input)

# geting the column names
def column_name_operation(data):
  column_names = data.columns.tolist()
  return column_names
column_names = column_name_operation(data) 

# shape of data
def data_shape_operation(data):
  return data.shape

# Column Names & Data Types
def data_type_operation(data):  
  datatype = []
  for i in range(len(column_names)):
    datatype.append({column_names[i] : data[column_names[i]].dtype} )
  return datatype

# numerical columns
def numerical_columns_operation(data):
  numeric_columns = data.select_dtypes(include="number").columns.tolist()
  return numeric_columns

# Missing Values by Row
def missing_values_operation(data):
  missing_values = int(data.isna().sum().sum())
  nan_rows = data[data.isna().any(axis=1)]
  return {"Total missing values" : {missing_values}, "Affected rows" : {len(nan_rows)}}

# spot indexes
def spot_indexes_operation(data, column_names):
  result = []
  for i in range(len(column_names)):
    if data[column_names[i]].dtype in ['int64', 'float64']:
      if data[column_names[i]].is_unique:
        # if (data[column_names[i]].diff().dropna()==1).all():
        result.append(column_names[i])
  return result
index_columns = spot_indexes_operation(data, column_names)

# Duplicate rows
def duplicate_values_operation(data, column_names, index_columns):
  columns_to_compare = []
  for j in range(len(column_names)):
    if (column_names[j] not in index_columns):
      columns_to_compare.append(column_names[j])
  
  # check if columns to compare is empty
  if not columns_to_compare: 
    return []

  # check the duplicate columns in columns to compare and put them in a list
  duplicate_rows = []
  duplicate = data.duplicated(subset=columns_to_compare, keep=False) 

  for i in range(len(duplicate)):
    if (duplicate[i]==True):
      duplicate_rows.append(i)
  return duplicate_rows

# check unique values
def unique_values_operation(data):
  unique_values = []
  for i in range(len(column_names)):
    value = len(data[column_names[i]].unique())
    unique_values.append({column_names[i] : value})
    return {column_names[i] : unique_values[i].get(column_names[i])}

# check for constant columns
def constant_column_operation(data):
  result = []
  for i in range(len(column_names)):
    if (data[column_names[i]].nunique() == 1):
      result.append({column_names[i]})
  return result


def inspect_dataset(data):
  #a dictionary that holds the profile of the data being passed
  profile = {} 
  profile["column_names"] = column_name_operation(data)
  profile["shape"] = data_shape_operation(data)
  profile["dtypes"] = data_type_operation(data)
  profile["numeric_columns"] = numerical_columns_operation(data)
  profile["missing_values"] = missing_values_operation(data)
  profile["index_columns"] = spot_indexes_operation(data, column_names)
  profile["duplicates"] = duplicate_values_operation(data, column_names, index_columns)
  profile["uniuqe_counts"] = unique_values_operation(data)
  profile["constant_columns"] = constant_column_operation(data)
  
  return profile
profile = inspect_dataset(data)

# print profile
def print_profile(profile):
  print("\nDATA PROFILE\n")
  print(f"COLUMN NAMES\n{profile['column_names']}\n")

  rows, columns = profile["shape"]
  print(f"SHAPE\nRows: {rows}\nColumns: {columns}\n")

  print(f"DATA TYPE OF EACH COLUMN")
  for i in range(len(column_names)):
    print(profile['dtypes'][i])

  print(f"\nNUMERIC COLUMNS\n{profile['numeric_columns']}")

  print(f"\nMISSING VALUES\n{profile['missing_values']}")
  
  print(f"\nINDEX COLUMNS\n{profile['index_columns']}")

  print(f"\nDUPLICATE ROWS\nThere are {len(profile['duplicates'])} duplicate rows\n{profile['duplicates']}")

  print(f"\nUNIQUE VALUES\n{profile['uniuqe_counts']}")

  print(f"\nCONSTANT COLUMNS\n{profile['constant_columns']}")

  
print_profile(profile)