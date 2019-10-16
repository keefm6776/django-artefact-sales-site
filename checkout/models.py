from django.db import models
from artefacts.models import Artefact
from customer.models import Customer

# Adapted from Course Instiute Notes

class Order(models.Model):
    date = models.DateField()
    del_full_name = models.CharField(max_length=60, blank=False)
    del_street_address1 = models.CharField(max_length=40, blank=False)
    del_street_address2 = models.CharField(max_length=40, blank=False)
    del_town_or_city = models.CharField(max_length=40, blank=False)
    del_county = models.CharField(max_length=40, blank=False)
    del_country = models.CharField(max_length=40, blank=False)
    del_postcode = models.CharField(max_length=20, blank=True)
    del_phone_number = models.CharField(max_length=20, blank=False)
    del_email = models.CharField(max_length=254, blank=False)
    customer_id = models.ForeignKey(Customer, null=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    artefact = models.ForeignKey(Artefact, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.artefact.name, self.artefact.price)
