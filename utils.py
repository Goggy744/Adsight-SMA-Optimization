import pandas as pd
import datetime

PATH = "COLLECTED-DATA/"

def justify_time(filename):
  """
  Function that take a file with relative timestamp and return a file with absolute timestamp
  """
  
  data = pd.read_csv(PATH + filename+'.csv')
  relative_to = data.columns[3]
  relative_to = relative_to.split('(')[1].split(')')[0]
  
  date, time = relative_to.split(" ")
  year, month, day = date.split('/')
  milliseconds = time.split('.')[1]
  hours, minutes, seconds = time.split('.')[0].split(':')
  year, month, day, hours, minutes, seconds, milliseconds = int(year), int(month), int(day), int(hours), int(minutes), int(seconds), int(milliseconds)
  
  relative_to = datetime.datetime(year, month, day, hours, minutes, seconds, milliseconds).strftime('%s')
  
  justified_data = data.copy()
  
  col_name = justified_data.columns[3]
  for i in range(0, justified_data.shape[0]):
    current_value = justified_data.iloc[i,3]
    new_value = current_value + int(relative_to)
    
    justified_data[col_name] = justified_data[col_name].replace([current_value], new_value)
  
  
  justified_data.to_csv(PATH+filename+'_justified_data.csv', index=False)
  
