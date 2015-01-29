from cartodb import CartoDBAPIKey, CartoDBException
import csv

user =  'YOUR_EMAIL'
API_KEY ='YOUR_API_KEY'
cartodb_domain = 'YOUR_USERNAME'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)

def spatialfromcsv(filename):
    with open(filename) as csvfile:
        datatable = csv.DictReader(csvfile)
        for row in datatable:
            lat = row['latitude']
            lon = row['longitude']
            bright = row['brightness']
            scan = row['scan']
            trk = row['track']
            date = str(row['acq_date'])
            time = row['acq_time']
            satlt = str(row['satellite'])
            conf = row['confidence']
            v = row['version']
            bright_t = row['bright_t31']
            frp = row['frp']

            All of the values are strings originally, but they become numbers later, unless single quotes are included
            sql_statement = insert into spatial (the_geom, latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, confidence, version, bright_t31, frp)  \
                            values (ST_SetSRID(ST_Point(%s, %s),4326), %s, %s, %s, %s, %s, '%s', %s, '%s', %s, %s, %s, %s)"  \
                            %(lat, lon, lat, lon, bright, scan, trk, date, time, satlt, conf, v, bright_t, frp)
            try:
                cl.sql(sql_statement)
            except CartoDBException as e:
                print ("some error ocurred", e)
