import pandas as pd

# ask the user for the file path
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

def clean_dataset(data):
  # make a copy of the data
  working_copy = data.copy()
  log = {}

  working_copy, removed = remove_duplicates(working_copy)
  log["duplicates_removed"] = removed

  working_copy, dropped = remove_constant_columns(working_copy)
  log["constant_columns_removed"] = dropped

  working_copy, emptied = remove_empty_columns(working_copy)
  log["empty_columns_removed"] = emptied

  working_copy, filled = fill_missing(working_copy)
  log["missing_values_filled"] = filled
  log["fill_method"] = "median"

  return working_copy, log

def remove_duplicates(data):
  before = data.shape[0]
  # remove duplicates
  data = data.drop_duplicates()
  after = data.shape[0]
  return data, before - after

def remove_constant_columns(data):
  result = []
  column_names = data.columns
  for i in range(len(column_names)):
    if (data[column_names[i]].nunique() == 1):
      result.append(column_names[i])
  
  data = data.drop(result, axis=1)

  return data, result

def remove_empty_columns(data):
  empty_columns = data.columns[data.isna().all()].tolist()
  data = data.drop(empty_columns, axis=1)
  
  return data, empty_columns

def fill_missing(data):
  total_missing_values = int(data.isna().sum().sum())
  data = data.fillna(data.median(numeric_only=True))

  return data, total_missing_values

cleaned_data, log = clean_dataset(data)
print(cleaned_data)
print(log)
