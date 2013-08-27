import urllib2
import json

portals = json.load(urllib2.urlopen('http://internal.hubapi.com/sfdc/v1/versions/v2?hapikey='))

def organization_type():
	
	count = 0

	for portalid in portals:
		try:
			orgstats = 'http://internal.hubapi.com/sfdc/v1/objects/%d/Organization?hapikey=' % portalid
			f = json.load(urllib2.urlopen(orgstats))
			z = [x for x in f]
			for key in z:
				fields = key['fields']
				#print fields
				for x in fields:
					if x['name'] == 'OrganizationType' and x['value'] == 'Professional Edition':
						print 'Pro Edition'
						count += 1

		except urllib2.HTTPError:
			pass

	print count
	print 'All done!'



organization_type()