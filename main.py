import bottle
import json
import data
import process
import os.path

#Grabs csv file data from website
def get_data():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/mr8w-325u.json?$limit=50000'
    info = data.grab_json(url)
    data.separate_dates(info, "week_ending_date")
    heads = ['year', 'week', 'week_ending_date', 'region', 'state',        'city',
    'pneumonia_and_influenza_deaths', 'all_deaths', '_1_year',             '_1_24_years',
    '_25_44_years', '_54_64_years', '_65_years', 'month', 'day']

    data.write_csv(info, csv_file,heads)
    
get_data()

#Serve the HTML file as a static file
@bottle.route("/")
def send_HTML():
  return bottle.static_file("index.html", root=".")

#A route to serve up the javascript file as a static file
@bottle.route("/java.js")
def javscript_file():
  return bottle.static_file("java.js", root=".")

#A get to serve up the line graph data as a JSON blob
@bottle.get("/line_graph")
def get_line_graph():
  read_file = data.read_csv("saved_data.csv")
  list = []
  get_year = process.get_values(read_file, "year")
  death_dict = process.dict_from_values(read_file, "year")
  for year in get_year:
    deaths = process.sum_death_matches(read_file, "all_deaths", "year", year)
    death_dict[year] = deaths
  list.append(death_dict)
  get_year1 = process.get_values(read_file, "year")
  death_dict1 = process.dict_from_values(read_file, "year")
  for year1 in get_year1:
    deaths = process.sum_death_matches(read_file, "_1_year", "year", year)
    death_dict1[year1] = deaths
  list.append(death_dict1)
  get_year2 = process.get_values(read_file, "year")
  death_dict2 = process.dict_from_values(read_file, "year")
  for year2 in get_year2:
    deaths = process.sum_death_matches(read_file, "_1_24_years", "year", year)
    death_dict2[year2] = deaths
  list.append(death_dict2)
  get_year3 = process.get_values(read_file, "year")
  death_dict3 = process.dict_from_values(read_file, "year")
  for year3 in get_year3:
    deaths = process.sum_death_matches(read_file, "_25_44_years", "year", year)
    death_dict3[year3] = deaths
  list.append(death_dict3)
  get_year4 = process.get_values(read_file, "year")
  death_dict4 = process.dict_from_values(read_file, "year")
  for year4 in get_year4:
    deaths = process.sum_death_matches(read_file, "_54_64_years", "year", year)
    death_dict4[year4] = deaths
  list.append(death_dict4)
  get_year5 = process.get_values(read_file, "year")
  death_dict5 = process.dict_from_values(read_file, "year")
  for year5 in get_year5:
    deaths = process.sum_death_matches(read_file, "_65_years", "year", year)
    death_dict5[year5] = deaths
  list.append(death_dict5)
  return json.dumps(list)


#A post to serve up the line graph data as a JSON blob
@bottle.post("/add_line_graph")
def post_line_graph():
  jsonString = bottle.request.body.read().decode()
  content = json.loads(jsonString)
  val = get_line_graph()
  return content
  


#A get to serve up the pie chart data as a JSON blob
@bottle.get("/pie_chart")
def get_pie_chart():
  read_file = data.read_csv("saved_data.csv")
  get_month = process.get_values(read_file, "month")
  death_dict = process.dict_from_values(read_file, "month")
  for month in get_month:
    deaths = process.sum_death_matches(read_file, "all_deaths", "month", month)
    death_dict[month] = deaths
  final = death_dict
  return json.dumps(final)
  

bottle.run(host="0.0.0.0")