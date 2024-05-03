import csv
import json
import urllib.request

def values_to_dict(keys, llv):
  list = []
  for val in llv:
    Dict = {}
    for key in range(len(keys)):
      Dict[keys[key]] = val[key]
    list.append(Dict)
  return list

def load_csv(file):
  final = []
  with open(file) as files:
    reader = csv.reader(files)
    header = next(reader)
    for str in reader:
      final.append(str)
    return final

def dict_to_list(lod,keys) :#if key does not exist store a -1
  ret_val = [ ]
  for lst in lod :
    sub_list = [ ]
    for key in keys :
      val = lst.get(key,-1)
      sub_list.append(val)
  ret_val.append(sub_list)
  return ret_val

def list_to_csv(file, llv):
  with open(file, "a") as files:
    writer = csv.writer(files)
    for content in llv:
       writer.writerow(content)


#Project 3
def fix_date(date):
  list = []
  split = date.split("/")
  month = split[0]
  day = split[1]
  list.append(int(month))
  list.append(int(day))
  return list

def separate_dates(lod, k):
  for Dict in lod:
    val = Dict[k]
    new = fix_date(val)
    Dict["month"] = new[0]
    Dict["day"] = new[1]
  return lod

def grab_json(x):
  request = urllib.request.urlopen(x)
  content = request.read().decode()
  val = json.loads(content)
  return val

def parse_numbers(lod, keys):
  for aDict in lod:
    for key in keys:
      val = int(aDict[key])
      aDict[key] = val
  return lod

def write_csv(lod, filename, keys):
  with open(filename, "w") as write:
    writer = csv.writer(write)
    writer.writerow(keys)
    for aDict in lod:
      list =[]
      for key in keys:
        list.append(aDict[key])
      writer.writerow(list)

def read_csv(x):
  with open(x) as file:
    reader = csv.reader(file)
    headers = next(reader)
    list = []
    for read in reader:
      dict = {}
      for content in range(len(headers)):
        dict[headers[content]] = read[content]
      list.append(dict)
  return list