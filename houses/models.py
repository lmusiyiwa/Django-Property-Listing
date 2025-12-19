from django.db import models

CATEGORIES = ["Bedrooms", "Bathrooms", "Kitchen", "Living", "Exterior", "Other"]

class House(models.Model):
    title = models.CharField(max_length=200, default="Waterfall Estate Residence")
    description = models.TextField(default="Your full house description here...")
    price = models.CharField(max_length=50, default="Price on request")
    bedrooms = models.IntegerField(default=5)
    bathrooms = models.IntegerField(default=5)
    location = models.CharField(max_length=200, default="Waterfall Estate, Midrand")

    def __str__(self):
        return self.title


class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    category = models.CharField(max_length=50, choices=[(c, c) for c in CATEGORIES])
    image = models.CharField(max_length=255)  # static path like 'photos/1/Exterior/exterior1.jpg'

    def __str__(self):
        return f"{self.house.title} - {self.category}"
