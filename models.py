from django.db import models

class Vehicle_info(models.Model):
    ownwr_name = models.CharField(max_length=100,null=True)
    ownwr_mob = models.CharField(max_length=100, null=True)
    ownwr_add = models.CharField(max_length=100, null=True)
    rfid_no = models.CharField(max_length=12, null=True)
    vehicle_no = models.CharField(max_length=100, null=True)
    vehicle_type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ownwr_name +' Type- ' + self.vehicle_type

class Vehicle_status(models.Model):
    vehicle = models.ForeignKey(Vehicle_info,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100, null=True)
    entry_time = models.CharField(max_length=100,null=True)
    entry_date = models.CharField(max_length=100,null=True)
    fine = models.IntegerField(null=True)

    def __str__(self):
        return self.vehicle.vehicle_no +' Type- ' + self.status


class Fine_of_vehicle(models.Model):
    v_type = models.CharField(max_length=100,null=True)
    fine = models.IntegerField(null=True)

    def __str__(self):
        return self.v_type + " Fine- " + str(self.fine)

