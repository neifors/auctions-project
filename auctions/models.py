from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics/', null=True, blank=True)

   
    def __str__(self):
       return self.name


class Auction(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
   title = models.CharField(max_length=100, null=False)
   description = models.TextField(max_length=1000, null=False)
   initial_price = models.IntegerField(null=False)
   date = models.DateField(default=datetime.date.today)
   photo = models.ImageField(upload_to='pics/', null=True, blank=True)
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
   active = models.BooleanField(default=True)
   last_bid = models.IntegerField(blank=True, null=True)

   def __str__(self):
       return self.title
   
   def deactivate(self):
       self.active = False
       return self

class Bid(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
   auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=False)
   amount = models.IntegerField()
   date = models.DateField(default=datetime.date.today)
   
   def __str__(self):
       return f"{self.amount}"


class Comment(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
   title = models.CharField(max_length=50)
   message = models.TextField(max_length=400)
   auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=False)
   date = models.DateField(default=datetime.date.today)
   
   def __str__(self):
       return self.title

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=False)

