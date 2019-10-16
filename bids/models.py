from django.db import models
from artefacts.models import Artefact
from customer.models import Customer

class BidHistory(models.Model):
    artefact_id = models.ForeignKey(Artefact, null=False)
    customer_id = models.ForeignKey(Customer, null=False)
    bid = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name


# Create your models here.

