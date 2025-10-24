from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from .models import Product, ExternalPostSummary
from .serializers import ProductSerializer, ExternalPostSummarySerializer
from django.db.models import Count
import requests
from django.utils.text import Truncator

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer

class ExternalPostSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExternalPostSummary.objects.all().order_by("-fetched_at")
    serializer_class = ExternalPostSummarySerializer

def dashboard(request):
    data = Product.objects.values("category").annotate(count=Count("id"))
    categories = [d["category"] for d in data]
    counts = [d["count"] for d in data]
    return render(request, "products/dashboard.html", {"categories": categories, "counts": counts})
