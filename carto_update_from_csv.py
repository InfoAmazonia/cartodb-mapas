from cartodb import CartoDBAPIKey, CartoDBException
import csv

user =  'laura.kurtzberg@gmail.com'
API_KEY ='adfa3ceeaf052aaa42e2e2ec96d4df80ea42e950'
cartodb_domain = 'lauragator'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)

def spatialfromcsv(filename):
    with open(filename) as csvfile:
        datatable = csv.DictReader(csvfile)
        for row in datatable:
            lat = row['latitude'] #float
            lon = row['longitude'] #float
            bright = row['brightness'] #float
            scan = row['scan'] #float
            trk = row['track'] #float
            date = str(row['acq_date']) #string
            time = row['acq_time'] #int
            satlt = str(row['satellite']) #string
            conf = row['confidence'] #int
            v = row['version'] #float
            bright_t = row['bright_t31'] #float
            frp = row['frp'] #float

            sql_statement = "insert into spatial (latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, confidence, version, bright_t31, frp) values (ST_SetSRID(ST_Point(%g, %g),4326), %g, %g, %g, '%s', %d, '%s', %d, %g, %g, %g)" %(lat, lon, bright, scan, trk, date, time, satlt, conf, v, bright_t, frp)
            try:
                cl.sql(sql_statement)
            except CartoDBException as e:
                print ("some error ocurred", e)

spatialfromcsv('firesJan.csv')
