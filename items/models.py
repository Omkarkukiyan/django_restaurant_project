from django.db import models

# Create your models here.


class Category(models.Model):
    section = models.CharField(max_length=200)

    def __str__(self):
        return self.section 


class FoodProducts(models.Model):
    section = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') 

    def __str__(self):
        return self.name 
     

     