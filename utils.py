import pandas as pd

PATH = "COLLECTED-DATA/"
def justify_time(filename):
  """
  Function that take a file with relative timestamp and return a file with absolute timestamp
  """
  
  f = pd.read_csv(PATH + filename)
  
  print(f.columns)
  
