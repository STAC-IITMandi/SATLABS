from sense_hat import SenseHat
import time
from datetime import datetime
import csv
sense = SenseHat()
timestamp = datetime.now()
delay=1
with open('movement_records.csv', 'w', newline='') as f:
    data_writer = csv.writer(f)
    data_writer.writerow(['datetime',
	                  'yaw','pitch','roll',
                      'mag_x','mag_y','mag_z',
                      'acc_x','acc_y','acc_z',
                      'gyro_x', 'gyro_y', 'gyro_z'])
    while(True):
        move_data=[]
        rec_time = datetime.now()
        move_data.append(rec_time)

        orientation = sense.get_orientation()
        move_data.append(orientation["yaw"])
        move_data.append(orientation["pitch"])
        move_data.append(orientation["roll"])

        mag = sense.get_compass_raw()
        move_data.append(mag["x"])
        move_data.append(mag["y"])
        move_data.append(mag["z"])

        acc = sense.get_accelerometer_raw()
        move_data.append(acc["x"])
        move_data.append(acc["y"])
        move_data.append(acc["z"])

        gyro = sense.get_gyroscope_raw()
        move_data.append(gyro["x"])
        move_data.append(gyro["y"])
        move_data.append(gyro["z"])

        dt = rec_time - timestamp
        if dt.seconds > delay:
            data_writer.writerow(move_data)
            timestamp = datetime.now()