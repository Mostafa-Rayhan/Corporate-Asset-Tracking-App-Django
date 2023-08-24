from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    DEVICE_TYPES = (
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.TextField()
    condition_on_return = models.TextField(null=True, blank=True)