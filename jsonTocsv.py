import csv
import json

with open('/home/limage/Documents/data_science/bhw/Airlines-All/Airlines/FrequentFlyerForum-Profiles.json') as json_file:
    data = json.load(json_file)

data = data["Forum Profiles"]
f1 = csv.writer(open("flights.csv", "w+"))
f2 = csv.writer(open("loyality_programms.csv", "w+"))
f3 = csv.writer(open("users.csv", "w+"))

f1.writerow(['NickName', 'Date', 'Codeshare', 'Flight' 'ArrivalCity', 'ArrivalAirport', 'ArrivalCountry', 'DepartureCity', 'DepartureAirport', 'DepartureCountry'])

for x in data:
  for y in x["Registered Flights"]:
    f1.writerow([
      x["NickName"],
      y["Date"],
      y["Codeshare"],
      y["Flight"],
      y["Arrival"]["City"],
      y["Arrival"]["Airport"],
      y["Arrival"]["Country"],
      y["Departure"]["City"],
      y["Departure"]["Airport"],
      y["Departure"]["Country"],
    ])

f2.writerow(['NicKName', 'Status', 'Prorgamm', 'Number'])

for x in data:
  for y in x["Loyality Programm"]:
    f2.writerow([
      x["NickName"],
      y["Status"],
      y["programm"],
      y["Number"]
    ])

f3.writerow(['NicKName', 'LastName', 'FirstName', 'Sex', 'Passports'])

for x in data:
  for y in x["Travel Documents"]:
    f3.writerow([
      x["NickName"],
      x["Real Name"]["Last Name"],
      x["Real Name"]["First Name"],
      x["Sex"],
      y["Passports"]
    ])