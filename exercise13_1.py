"""
Exercise 13.1: Change either the www.py4e.com/code3/geojson.py or
www.py4e.com/code3/geoxml.py to print oout the two-character country code from
the retrieved data. Add error checking so you program does not traceback if 
the country code is not there. Once you have it working, search for "Atlantic 
Ocean" and make sure it can handle locations that are not in any country.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 5, 2017
"""

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

#    print(json.dumps(js, indent=4))
    counter = -1
    info = js["results"][0]["address_components"]
    for item in info:
        counter += 1
        if js["results"][0]["address_components"][counter]["types"] == ['country', 'political']:
            print(js["results"][0]["address_components"][counter]["short_name"])  
        else:
            continue
        
