from django.db import models

class Current_Bid(models.Model):
    artefact_name = models.CharField(max_length=50, default='')
    user_email =  models.CharField(max_length=50, default='')
    bid = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

# Create your models here.

