from django.db import models
from account.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100);

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100);
    price = models.DecimalField(max_digits=10, decimal_places=2);
    category = models.ForeignKey(Categories, on_delete=models.CASCADE);
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/',null=True)

    def __str__(self):
        return f"{self.name}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE);
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"

class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="order_items")
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"
    
class Order(models.Model):
    STATUS = (
        ('En attente', 'En attente'),
        ('Servi', 'Servi'),
        ('Annulé', 'Annulé'),
        ('Payé', 'Payé'),
        

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=50,default='En attente')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_total(self):
        # Recalculate total price based on ordered items.
        self.total_price = sum(item.item.price * item.quantity for item in self.order_items.all())
        self.save()

    def __str__(self):
        return f"Order #{self.id} - {self.user.phone}"