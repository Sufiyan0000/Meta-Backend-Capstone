from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.slug

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    featured = models.BooleanField()
    
    def __str__(self):
        return self.title
    
    def get_item(self):
        return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=6)
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f'Booking by {self.name} for {self.no_of_guests} guests on {self.booking_date}'

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f'Cart of {self.user.username} has {self.menu_item} in cart.'