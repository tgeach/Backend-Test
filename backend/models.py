from django.db import models
from datetime import datetime, date

class Destination(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Donation(models.Model):
    creation_time = models.DateField(auto_now_add=True)
    store = models.ForeignKey('Store', on_delete=models.DO_NOTHING, default='')
    weight_kg = models.FloatField()
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
    destination = models.ForeignKey('Destination', on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f" {self.id} {self.department} - {self.destination} - {str(self.weight_kg)}"

class DiversionType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Stage(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=120)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, blank=True, null=True)
    diversion_type = models.ForeignKey('DiversionType', on_delete=models.CASCADE, default='App Only')

    def __str__(self):
        return self.name



