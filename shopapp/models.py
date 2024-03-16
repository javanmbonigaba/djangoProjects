from django.db import models

class category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
class product(models.Model):
    title= models.CharField(max_length = 100)
    price = models.IntegerField()
    discription = models.TextField()
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Buyer(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    def __str__(self):
        return self.first_name
class order(models.Model):
    product_id = models.ForeignKey(product, on_delete = models.CASCADE)
    buyer_id = models.ForeignKey(Buyer, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.quantity
    




# Create your models here.
