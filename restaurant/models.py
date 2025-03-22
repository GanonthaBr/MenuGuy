from django.db import models
from account.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100);

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100);
    price = models.DecimalField(max_digits=5, decimal_places=2);
    category = models.ForeignKey(Categories, on_delete=models.CASCADE);
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE);
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"