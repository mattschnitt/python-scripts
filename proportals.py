import urllib2
import json

portals = json.load(urllib2.urlopen('internalapi'))

def organization_type():
	
	count = 0

	for portalid in portals:
		try:
			orgstats = 'internalapi' % portalid
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
