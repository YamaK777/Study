import geoip2.database
check_ip = '157.7.205.139'
reader = geoip2.database.Reader('GeoLite2-City.mmdb')
rec = reader.city(check_ip)
print('IP:', check_ip)
print('Country:', rec.country.name)
print('City:', rec.city.name)
print('Latitude:', rec.location.latitude)
print('Longitude:', rec.location.longitude)
