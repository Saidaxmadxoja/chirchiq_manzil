from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Manzil(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='manzil/', null=True, blank=True)

    def __str__(self):
        return self.name