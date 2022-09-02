from django.db import models
from datetime import datetime, date

class Donations(models.Model):
    Bakery = 'Bakery'
    Diary = 'Dairy'
    Deli = 'Deli'
    Grocery = 'Grocery'
    MeatSeafood = 'Meat/Seafood'
    Produce = 'Produce'
    Other = 'Other'
    DEPARTMENT_CHOICES = [
        ('Bakery', 'Bakery'),
        ('Dairy', 'Dairy'),
        ('Deli', 'Deli'),
        ('Grocery', 'Grocery'),
        ('MeatSeafood', 'Meat/Seafood'),
        ('Produce', 'Produce'),
        ('Other', 'Other')
    ]
    Charity = 'Charity'
    Farm = 'Farm'
    Compost = 'Compost'
    DESTINATION_CHOICES = [
        ('Charity', 'Charity'),
        ('Farm', 'Farm'),
        ('Compost', 'Compost')
    ]

    creation_time = models.DateField(auto_now_add=True)
    store = models.CharField(max_length=200)
    weight_kg = models.FloatField()
    department = models.CharField(
        max_length = 11,
        choices = DEPARTMENT_CHOICES,
    )
    destination = models.CharField(
        max_length= 7,
        choices = DESTINATION_CHOICES
    )
    notes = models.CharField(max_length=1024, blank=True, null=True)


