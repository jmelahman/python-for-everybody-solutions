"""
Exercise 13.1: Change either the www.py4e.com/code3/geojson.py or
www.py4e.com/code3/geoxml.py to print out the two-character country code from
the retrieved data. Add error checking so you program does not traceback if
the country code is not there. Once you have it working, search for "Atlantic
Ocean" and make sure it can handle locations that are not in any country.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

import urllib.request
import urllib.parse
import urllib.error
import json

# If you have a Google Places API key, enter it here
# api_key = 'xxx'
api_key = ''

if not api_key:
    api_key = '42'
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if not address:
        break
    params = {'address': address, 'key': api_key}
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except BaseException:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    counter = -1
    info = js["results"][0]["address_components"]
    for item in info:
        counter += 1
        if js["results"][0]["address_components"][counter]["types"] == [
                'country', 'political']:
            print(js["results"][0]["address_components"][counter]
                ["short_name"])
            break
        else:
            continue
    print("No country code")
