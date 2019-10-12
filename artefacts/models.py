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