from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name 


class Items(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Items"
    
    def __str__(self):
        return self.name
