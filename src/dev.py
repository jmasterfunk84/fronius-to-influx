from fronius_to_influx import FroniusToInflux
from influxdb import InfluxDBClient
from astral import Location

import pytz


client = InfluxDBClient(host='localhost', port=8087, username='grafana', password='grafana', ssl=False)
client.switch_database('grafana')
location = Location(('Poznan', 'Europe', 52.408078, 16.933618, 'Europe/Warsaw', 87))
tz = pytz.timezone('Europe/Warsaw')
endpoints = [
    'http://172.30.1.11:5000/3PInverterData.json',
    'http://172.30.1.11:5000/CommonInverterData.json',
    'http://172.30.1.11:5000/MinMaxInverterData.json'
]

archiveendpoints = [
    'http://172.30.1.11:5000/solar_api/v1/GetArchiveData.cgi?Scope=System&Channel=Temperature_Powerstage&Channel=Current_DC_String_1&Channel=Current_DC_String_2&Channel=Voltage_DC_String_1&Channel=Voltage_DC_String_2'
]


z = FroniusToInflux(client, location, endpoints, tz)
z.IGNORE_SUN_DOWN = True
z.run()
