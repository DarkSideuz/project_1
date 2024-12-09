from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return super().__str__()
    
class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self) -> str:
        return super().__str__()
