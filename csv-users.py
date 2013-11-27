import sys
import requests
import csv

def wistia_number():     
	portals = []
	keys = []

	r = requests.get("https://api.hubapi.com/hubs/v1/settings", params={'key': 'wistia_api_key', 'hapikey': 'apikey'})
	json = r.json()

	csv_out = open('portals.csv', 'wb')
	
	writer = csv.writer(csv_out, delimiter=",")

	data = [x for x in json['settings']]
	for x in data:
		portals.append(x['hubId'])
		keys.append(x['value'])
		portal = x['hubId']
		key = x['value']
		writer.writerow([portal, key])

wistia_number()

