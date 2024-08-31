from django.db import models

class Producer(models.Model):
    producer_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.id} : {self.producer_name}"
    
    
#relation with the category OnetoMany
class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.cat_name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, default = 1)
    Category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name


#ManytoMany: order and product 
# class Order(models.Model):
#     order_name = models.CharField()
