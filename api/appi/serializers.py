from .models import *
from rest_framework import serializers

class BuildersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builders
        fields = '__all__'
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'