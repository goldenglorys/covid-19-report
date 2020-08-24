import requests
import datetime

timestamp = datetime.datetime.now()
get_date = timestamp.strftime("%B, %d %Y")
get_time = timestamp.strftime("%I:%M:%S %p")

class Covidreport:
  def __init__(self, country):
    self.country = country

  def getreport(self):
    """Summary or description of getreport function

    Parameters:
    country (string): is required and stands as the country selected to get it's covid-19 report

    Returns:
    dictionary collection: current report status for the selected country is returned. 
    Total Cases
    Active Cases
    Discharged Cases
    Deaths Cases

    """

    url = "https://covid2019-api.herokuapp.com/v2/country/"+str(self.country)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    response_payload = response.json()['data']
    return response_payload


available_country = ('seychelles', 'eritrea', 'mauritania', 'eswatini', 'ethiopia')
ask_country = ""
want_descriptive = ""

while ask_country != "q":
  print("Select among the listed africa country to get their covid-19 latest report or press q to quit\n")
  for country in available_country:
    print(country.capitalize())
  ask_country = input("input among the name listed above : \n").lower()
  if ask_country == "q":
    print("Program terminated")
    break
  elif ask_country not in available_country:
    print("Invalid input, please follow the instruction\n")
  else:
    country_report = Covidreport(ask_country)
    report = country_report.getreport()
    print("=================================================")
    print(f""" Here's a simple report of {ask_country.capitalize()} Novel-coronavirus/covid-19 report status as at {get_date} {get_time}:
    - Total Confiremed Cases: {report['confirmed']}
    - Active Cases: {report['active']}
    - Discharged Cases: {report['recovered']}
    - Death Cases:{report['deaths']}
    """)
    print("=================================================\n")
    want_descriptive = input(f"Press [y] to get a descriptive report for {ask_country.capitalize()} or any key to continue: \n").lower()
    if want_descriptive == "y":
      print("getting description")
    else:
      next_country = input("Enter [y] to get report for another country or any key to end the program: \n").lower()
      if next_country == 'y':
        continue
      else:
        print("Program terminated")
        break
    

  
