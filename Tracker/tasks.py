from celery.decorators import task
from time import sleep
import serial
from TrackerApp.models import *
from datetime import date,datetime

@task
def MyTask():
    try:
        port = '/dev/cu.usbmodem14101'
        ard = serial.Serial(port, 9600, timeout=5)
        x = 0
        while x == 0:
            msg = ard.readline()
            if msg:
                status = ""
                from datetime import datetime as dt
                now = dt.now().strftime('%H:%M:%S')
                time = now
                today_date = date.today()
                upload_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d-%m-%Y')
                msg = msg.decode("ascii")
                msg = msg.split("&")
                print(msg[0], msg[1])
                print(msg[1])
                data = Vehicle_info.objects.filter(rfid_no=msg[0][:12]).first()
                if data:
                    if msg[1] == "Red":
                        status = "Wrong"
                        data2 = Fine_of_vehicle.objects.filter(v_type=data.vehicle_type).first()
                        fine = data2.fine
                    else:
                        status = "Right"
                        fine = 0
                    Vehicle_status.objects.create(vehicle=data, status=status, entry_time=time
                                                  , entry_date=upload_date, fine=fine)
                    print("Vehicel Created")
                else:
                    error = True

    except:
        print("Please Connect Device ")