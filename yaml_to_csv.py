import csv 
import yaml

if __name__ == "__main__":
	with open("1.yaml",'r') as f:
		doc = yaml.safe_load(f)
		data = doc["2017-01-01"]
		f1 = csv.writer(open("1.csv", "w+"))
		f1.writerow(['FlightNum', 'Company', 'NumClientLoyalty', 'Class', 'Fare', 'From', 'Status', 'To' ])
		for q,x in zip(data,dict.values(data)):
			flightnum = q
			fRom = x.pop('FROM')
			status = x.pop('STATUS')
			to = x.pop('TO')
			for y in dict.values(x):
				for z,t  in zip(y,dict.values(y)):
					company = z[0:2]
					numclient = z[3:]
					cLass = t['CLASS']  
					fare = t['FARE']
					data_1 = [flightnum, company, numclient, cLass, fare, fRom, status, to]
					f1.writerow(data_1)


	
	
	



