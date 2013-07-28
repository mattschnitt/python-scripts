import json
from pprint import pprint

data_open = open('53lists.json')
data = json.load(data_open)

def get_the_names():
	listofnames = []
	print_it = [x for x in data]
	for key in print_it:
		triggerset = key['triggerSet']
		print_it_2 = [x for x in triggerset]
		for value in print_it_2:
			listofnames.append(value['name'])
	
	send_file = open('dynamiclistswithworkflows.txt', 'w')

	for items in listofnames:
		send_file.write(items + "\n")

	send_file.close()

	print "success!"

get_the_names()