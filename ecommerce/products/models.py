from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.PositiveIntegerField()
    name=models.CharField(max_length=25)
    cost=models.IntegerField()
    date=models.DateField()
    description=models.TextField()
    
    def __str__(self):
        return self.name