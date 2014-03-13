import requests
import csv
from address import AddressParser, Address

ap = AddressParser()

domains = []

with open("""list of domains""", 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		domains.append(row[0])

print domains

def get_zip():

	csv_out = open("""destination csv""", 'wb')
	writer = csv.writer(csv_out, delimiter=",")

	for domain in domains:

		r = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json", 
					params={'query': domain, 'sensor':'false', 'key':"""your key here"""})
		json = r.json()

		result = json['results']

		if result == []:
			writer.writerow([domain, 'None'])
		else:

			latlng = None

			for x in result[:1]:
				latitude = str(x['geometry']['location']['lat'])
				longitude = str(x['geometry']['location']['lng'])

				ll = [latitude, longitude]

				latlng = ",".join(ll)

			s = requests.get("https://maps.googleapis.com/maps/api/geocode/json", 
						params={'latlng': '%s'%(latlng), 'sensor':'false', 'key':"""your key here"""})

			unpacked = s.json()

			data = unpacked['results']

			for x in data[:1]:
				address = x["formatted_address"]
				parsed_address = ap.parse_address(address)
				writer.writerow([domain, parsed_address.zip])
	

get_zip()