import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    country_code = None
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
     
    if tree.find('status') is None or 'ZERO_RESULTS' == tree.find('status').text :
        print('==== Failure To Retrieve ====')
        print(data.decode())
        continue

    results = tree.findall('result')
    address_components = results[0].findall('address_component')
        

    for address_component in address_components :
        type_el_list = address_component.findall('type')
        type_list = list()
        for type_el in type_el_list :
            type_list.append(type_el.text)
        if 'country' in type_list and 'political' in type_list :
            country_code = address_component.find('short_name').text
            break
    
    if country_code :
        print('Country code :',country_code)
    else :
        print('No country code.')