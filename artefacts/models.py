from django.db import models

# Create your models here.

class Artefact(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    history = models.TextField()
    century = models.DecimalField(max_digits=3, decimal_places=0)

    ERA_CHOICES = (('AD', 'Anno Domini'),
          ('BC', 'Before Christ'),
    )
    era = models.CharField(max_length=2, choices=ERA_CHOICES)

    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images')
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    email = models.CharField(max_length=254, default='')
    full_name = models.CharField(max_length=60, default='')
    street_Address1 = models.CharField(max_length=40, default='')
    street_Address2 = models.CharField(max_length=40, default='')
    town_or_city = models.CharField(max_length=40, default='')
    county = models.CharField(max_length=40, default='')
    country = models.CharField(max_length=40, default='')
    postcode = models.CharField(max_length=20, default='')
    phone_number = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name

class BidHistory(models.Model):
    artefact_id = models.ForeignKey(Artefact, null=False)
    customer_id = models.ForeignKey(Customer, null=False)
    bid = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
