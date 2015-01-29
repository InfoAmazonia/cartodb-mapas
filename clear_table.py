#clear_table.py

from cartodb import CartoDBAPIKey, CartoDBException

user =  'laura.kurtzberg@gmail.com'
API_KEY ='adfa3ceeaf052aaa42e2e2ec96d4df80ea42e950'
cartodb_domain = 'lauragator'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)

sql_statement = "DELETE FROM spatial"

try:
    print cl.sql(sql_statement)
except CartoDBException as e:
    print ("some error ocurred", e)
