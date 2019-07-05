from sense_hat import SenseHat
import time
from datetime import datetime
import csv
sense = SenseHat()
with open('env_records.csv', 'w', newline='') as f:
    data_writer = csv.writer(f)
    data_writer.writerow(['datetime','temp','pres','hum'])
    while(True):
        data_writer.writerow([datetime.now(), sense.get_temperature(), sense.get_humidity(), sense.get_pressure()])
        time.sleep(1)