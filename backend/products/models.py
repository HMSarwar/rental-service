from django.db import models
# Create your models here.


class Products(models.Model):
    code = models.CharField(max_length=127)
    name = models.CharField(max_length=512)
    type = models.CharField(max_length=50)
    availability = models.BooleanField(null=True, blank=True)
    needing_repair = models.BooleanField(null=True, blank=True)
    durability = models.IntegerField(null=True, blank=True)
    max_durability = models.IntegerField(null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    minimum_rent_period = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'products'


