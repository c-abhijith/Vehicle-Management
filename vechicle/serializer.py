from rest_framework import serializers
from .models import *

class VechicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VechicleDetails
        fields="__all__"

    # def validate(self, attrs):
    #     if VechicleDetails.objects.filter(vehicle_number=attrs['vehicle_number']).exists():
    #         raise serializers.ValidationError(
    #             {"vehicle_number": "vehicle_number already exits."}) 


    #     return attrs            
        