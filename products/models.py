from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("electronics", "Electronics"),
        ("books", "Books"),
        ("clothing", "Clothing"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ExternalPostSummary(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=300)
    body_excerpt = models.TextField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.external_id} - {self.title[:40]}"
