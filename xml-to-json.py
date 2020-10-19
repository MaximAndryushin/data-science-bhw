import xml.etree.ElementTree as ET
import csv

f1 = csv.writer(open("PointzAggregator.csv", "w"))
f1.writerow(["UID", "Name", "LastName", "CardType", "CardNumber", "BonusProgramm", "Activities", "Code", "Date",
             "Departure", "Arrival", "Fare"])


def getFromXML(XML_path):
    try:
        tree = ET.parse(XML_path)
        root = tree.getroot()
        for user in root.findall('user'):
            uid = user.get('uid')
            name = user.find('name').get('first')
            lastname = user.find('name').get('last')
            cards = user.find('cards')
            cardtype = cards.get('type')
            for card in cards.findall('card'):
                number = card.get('number')
                bonus = card.find('bonusprogramm').text
                activities = card.find('activities')
                activitiestype = activities.get('type')
                for activity in activities.findall('activity'):
                    code = activity.find('Code').text
                    date = activity.find('Date').text
                    departure = activity.find('Departure').text
                    arrival = activity.find('Arrival').text
                    fare = activity.find('Fare').text
                    f1.writerow([uid, name, lastname, cardtype, number,  bonus, activitiestype, code, date, departure,
                                 arrival, fare])


    except IOError as e:
        print(e)

getFromXML("PointzAggregator-AirlinesData.xml")