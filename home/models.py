from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Student (models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Customer (models.Model):
    customer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name