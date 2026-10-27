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



def find_outliers(data):
  report = {}
  numeric_columns = data.select_dtypes(include="number").columns.tolist()
  for col in numeric_columns:
    low, high = get_iqr_bounds(data[col])
    report[col] = count_outside_bounds(data[col], low, high)
  return report

def get_iqr_bounds(column):
  q1 = column.quantile(0.25)
  q3 = column.quantile(0.75)
  iqr = q3 - q1
  low = q1 - (1.5*iqr)
  high = q3 + (1.5*iqr)
  return low, high

def count_outside_bounds(column, low, high):
  below = column < low
  above = column > high
  outside = below | above
  return int(outside.sum())

outliers = find_outliers(data)
print(outliers)