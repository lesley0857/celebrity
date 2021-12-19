from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save

class Images(models.Model):
    title  = models.CharField(null=True,max_length=200)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    picture = models.ImageField(default="images/propic.jpeg/",null=True,blank=True)

    def __str__(self):
        return str(self.title)


class Customer(models.Model):
    user = models.OneToOneField(User,null = True,on_delete = models.CASCADE,default=True)
    name  = models.CharField(null=True,max_length=200)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    profile_pic = models.ImageField(default="images/propic.jpeg/",null=True,blank=True)

    def __str__(self):
        return str(self.user)

class Team(models.Model):
    name  = models.CharField(null=True,max_length=200)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    teamimaage = models.ImageField(null=True,blank=True)
    role = models.CharField(null=True, max_length=200)
    details = models.TextField(null=True)

    def __str__(self):
        return str(self.name)



class Posts(models.Model):
    #customer = models.OneToOneField(Customer,null = True,on_delete = models.CASCADE,default=True)
    title  = models.CharField(null=True,max_length=200)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    filefield = models.FileField(upload_to='images')
    details = models.TextField(null=True)

    def __str__(self):
        return str(self.title)

class Comments(models.Model):
    customer = models.ForeignKey(Customer,null = True,on_delete=models.SET_NULL)
    posts = models.ForeignKey(Posts, null=True, on_delete=models.SET_NULL)
    title  = models.CharField(null=True,max_length=200)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    filefield = models.FileField(null=True,upload_to='images')
    comment_text = models.TextField(null=True)

    def __str__(self):
        return str(self.title)

class Replies(models.Model):
    customer =  models.ForeignKey(Customer,null = True,on_delete=models.SET_NULL)
    comments = models.ForeignKey(Comments, null=True, on_delete=models.SET_NULL)
    title  = models.CharField(null=True,max_length=200)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    filefield = models.FileField(null=True,upload_to='images')
    reply_text = models.TextField(null=True)

    def __str__(self):
        return str(self.title)