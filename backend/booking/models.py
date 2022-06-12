
from django.db import models
# Create your models here.
from products.models import Products


class Booking(models.Model):
    party_name = models.CharField(max_length=127)
    contact = models.CharField(max_length=512)
    rent_period = models.IntegerField()
    estimated_rent_fee = models.IntegerField()
    is_returned = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        app_label = 'booking'


