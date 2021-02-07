import json

    with open('export.geojson', 'rb') as f:
        data = f.read()
        data = json.loads(data)
        for i in data['features']:
            hid = i['properties']['@id']
            try:
                amenity = i['properties']['amenity']
            except:
                amenity = 'hospital'
            try:
                name = i['properties']['name']
            except:
                name = None
            try:
                address = i['properties']['addr:full']
            except:
                address = None
            try:
                district = i['properties']['addr:district']
            except:
                district = None
            try:
                postcode = i['properties']['addr:postcode']
            except:
                postcode = None
            try:
                state = i['properties']['addr:state']
            except:
                state = None
            try:
                phone = i['properties']['contact:phone']
            except:
                phone = None
            lon = i['geometry']['coordinates'][0]
            lat = i['geometry']['coordinates'][1]
            try:
                Hospital.objects.create(amenity=amenity, hid=hid, name=name, address=address, district=district, postcode=postcode, state=state, phone=phone, location=Point(x=lon, y=lat))
                print('-', end='')
            except:
                print(i)