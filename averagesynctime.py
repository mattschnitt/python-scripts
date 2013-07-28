import urllib2
import json
from numpy import mean
import threading

v2portals = 'http://internal.hubapi.com/sfdc/v1/versions/v2?hapikey=07dc043a-ca93-442c-9b3f-98837871f96d'

response = urllib2.urlopen(v2portals)
intermediary = json.load(response)

#print each portal
def print_portals(): 
	for i in intermediary:
		print i

#count each portal and return total
def count_portals():
	count = 0
	for i in intermediary:
		count +=1
	print count

#return individual portal based on position
def print_individual(id):
	individual = intermediary[id]
	print individual

#print portal stats for individual portal
def individual_stats(portalid):
	portalstats = 'http://internal.hubapi.com/sfdc/v1/portals/%d?hapikey=07dc043a-ca93-442c-9b3f-98837871f96d' % portalid
	f = json.load(urllib2.urlopen(portalstats))
	print f

#grab only averageSyncTimeLastHourInSeconds if a portal has intermediary
#note: after json is decoded, it just exists as a dictionary
def inividual_sync_time(portalid):
	portalstats = 'http://internal.hubapi.com/sfdc/v1/portals/%d?hapikey=07dc043a-ca93-442c-9b3f-98837871f96d' % portalid
	f = json.load(urllib2.urlopen(portalstats))
	if 'averageSyncTimeLastHourInSeconds' in f:
		print f['averageSyncTimeLastHourInSeconds']
	else:
		print False

# passes portalid into portals endpoint, adds it to a list, and returns the average of that list
def get_all_average_sync_times():
	synctimes = []
	for portalid in intermediary:
		portalstats = 'http://internal.hubapi.com/sfdc/v1/portals/%d?hapikey=07dc043a-ca93-442c-9b3f-98837871f96d' % portalid
		f = json.load(urllib2.urlopen(portalstats))
		if 'averageSyncTimeLastHourInSeconds' in f:
			synctimes.append(f['averageSyncTimeLastHourInSeconds'])
			print synctimes
	
	NUM_THREADS = 200
	for i in range(0, NUM_THREADS):
		thread = threading.Thread(target=get_all_average_sync_times)
		thread.start()

	sleep(0.01)

	averagetime = mean(synctimes)

	print 'The average sync time for the last hour is %d seconds' % averagetime

get_all_average_sync_times()
