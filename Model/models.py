# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Data(models.Model):
    passengerid = models.CharField(db_column='PassengerID', max_length=255)  # Field name made lowercase.
    driverid = models.CharField(db_column='DriverID', max_length=255)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=255)  # Field name made lowercase.
    reservationtime = models.CharField(db_column='ReservationTime', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    startingpoint = models.CharField(db_column='StartingPoint', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    startinglongitude = models.CharField(db_column='StartingLongitude', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase.
    startinglatitude = models.CharField(db_column='StartingLatitude', max_length=255)  # Field name made lowercase.
    endingpoint = models.CharField(db_column='EndingPoint', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    endinglongitude = models.CharField(db_column='EndingLongitude', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    endinglatitude = models.CharField(db_column='EndingLatitude', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    type = models.PositiveIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    sideid = models.CharField(db_column='SideID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dispatchtime = models.CharField(db_column='DispatchTime', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    boardingtime = models.CharField(db_column='BoardingTime', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    departuretime = models.CharField(db_column='DepartureTime', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    driverstartinglongitude = models.CharField(db_column='DriverStartingLongitude', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase.
    driverstartinglatitude = models.CharField(db_column='DriverStartingLatitude', max_length=255, blank=True,
                                              null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'data'

'''
class administrators(models.Model):  # 管理员
    A_id = models.CharField(primary_key=True, max_length=10, default='abc')  # 账号
    password = models.CharField(max_length=50)  # 密码'''




class Appointment(models.Model):
    passengerid = models.CharField(db_column='PassengerID', primary_key=True, max_length=255)  # Field name made lowercase.
    reservationid = models.CharField(db_column='ReservationID', max_length=255)  # Field name made lowercase.
    astate = models.IntegerField(db_column='AState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'appointment'
        unique_together = (('passengerid', 'reservationid'),)


class Car(models.Model):
    carid = models.CharField(db_column='CarID', primary_key=True, max_length=255)  # Field name made lowercase.
    carstate = models.IntegerField(db_column='CarState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'car'



class DataNew(models.Model):
    passengerid = models.CharField(db_column='PassengerID', max_length=255)  # Field name made lowercase.
    driverid = models.CharField(db_column='DriverID', max_length=255)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=255)  # Field name made lowercase.
    reservationtime = models.CharField(db_column='ReservationTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startingpoint = models.CharField(db_column='StartingPoint', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startinglongitude = models.CharField(db_column='StartingLongitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startinglatitude = models.CharField(db_column='StartingLatitude', max_length=255)  # Field name made lowercase.
    endingpoint = models.CharField(db_column='EndingPoint', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endinglongitude = models.CharField(db_column='EndingLongitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endinglatitude = models.CharField(db_column='EndingLatitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.PositiveIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    sideid = models.CharField(db_column='SideID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    driverstartinglongitude = models.CharField(db_column='DriverStartingLongitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    driverstartinglatitude = models.CharField(db_column='DriverStartingLatitude', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'data_new'



class Driver(models.Model):
    driverid = models.CharField(db_column='DriverID', max_length=255)  # Field name made lowercase.
    driverstate = models.IntegerField(db_column='DriverState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'driver'


class Driving(models.Model):
    driverid = models.CharField(db_column='DriverID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    carid = models.CharField(db_column='CarID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startingtime = models.CharField(db_column='StartingTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endingtime = models.CharField(db_column='EndingTime', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'driving'


class Order(models.Model):
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=255)  # Field name made lowercase.
    dispatchtime = models.CharField(db_column='DispatchTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boardingtime = models.CharField(db_column='BoardingTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    departuretime = models.CharField(db_column='DepartureTime', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'order'


class Passenger(models.Model):
    passengerid = models.CharField(db_column='PassengerID', primary_key=True, max_length=255)  # Field name made lowercase.
    passengerstate = models.IntegerField(db_column='PassengerState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'passenger'


class Reservation(models.Model):
    reservationid = models.CharField(db_column='ReservationID', primary_key=True, max_length=255)  # Field name made lowercase.
    reservationtime = models.CharField(db_column='ReservationTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startingpoint = models.CharField(db_column='StartingPoint', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startinglatitude = models.CharField(db_column='StartingLatitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startinglongitude = models.CharField(db_column='StartingLongitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endingpoint = models.CharField(db_column='EndingPoint', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endinglongitude = models.CharField(db_column='EndingLongitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endinglatitude = models.CharField(db_column='EndingLatitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reservation'


class Riding(models.Model):
    passengerid = models.CharField(db_column='PassengerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    carid = models.CharField(db_column='CarID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='OrderID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'riding'


class User(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=255)  # Field name made lowercase.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
