import csv
import os
import json

path = os.path.dirname(__file__)

def createExpTimestamp(userId):
  with open(os.path.join(path,f"data/expLog/{userId}.csv"), 'w') as file:
    writer = csv.writer(file)
    columnsName = ['eventName', 'timestamp']
    
    writer.writerow(columnsName)
  
def getUserId():
  directory = os.path.join(os.path.dirname(__file__), "data/expLog")
  id = 1
  for path in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, path)):
      id+=1
      
  return id

def addEvent(eventName, timeStamp, userId):
  with open(os.path.join(path, f"data/expLog/{userId}.csv"), "a") as file:
    writer = csv.writer(file)
    newRow = [eventName, timeStamp]
    writer.writerow(newRow)
    
def createExpInfo(fname, data):
  json_dict = {'articleLayout':{}}
  for el in data:
    if len(el.values()) == 1:
      for key in el.keys():
        json_dict.update({key: el[key] })
    else:
      for key, value in el.items():
        json_dict['articleLayout'].update({key:value})
        
  with open(os.path.join(path, f"data/expInfo/{fname}.json"), "w") as f:
    json.dump(json_dict, f)
    
  
        
    
  
    
  
       
    
  