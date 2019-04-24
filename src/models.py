from django.db import models

# Create your models here.


class Nut(models.Model):

    name     = models.CharField(max_length=200)
    image    = models.ImageField(upload_to='media/upload/')
    price    = models.IntegerField()
    discount = models.IntegerField()


class Oil(models.Model):

    name     = models.CharField(max_length=200)
    image    = models.ImageField(upload_to='media/upload/')
    price    = models.IntegerField()
    discount = models.IntegerField()
    

class PastaNoodle(models.Model):

    name     = models.CharField(max_length=200)
    image    = models.ImageField(upload_to='media/upload/')
    price    = models.IntegerField()
    discount = models.IntegerField()



class Offer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/upload/')
    price = models.IntegerField()
    saveprice  = models.IntegerField()



class ContactUs(models.Model):
    name    = models.CharField(max_length=200)
    subject = models.CharField(max_length=250)
    email   = models.EmailField()
    massege = models.TextField(max_length=1000)     
        
    




