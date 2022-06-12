from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'party_name', 'contact', 'rent_period', 'estimated_rent_fee', 'is_returned')