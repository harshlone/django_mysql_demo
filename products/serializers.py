from rest_framework import serializers
from .models import Product, ExternalPostSummary

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ExternalPostSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalPostSummary
        fields = "__all__"
