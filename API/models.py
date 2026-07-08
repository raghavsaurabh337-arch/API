from django.db import models

# Create your models here.
class create_model(models.Model):     
     email=models.EmailField(max_length=100)
     password=models.CharField(max_length=100)
     
class student(models.Model):
     name=models.CharField(max_length=100)
     father_name=models.CharField(max_length=100)
     age=models.IntegerField()
     course=models.CharField(max_length=10)
class employee(models.Model):
     name=models.CharField(max_length=100)
     salary=models.DecimalField(max_digits=10, decimal_places=2)
     villege=models.CharField(max_length=50)
     Department=models.CharField(max_length=10)
class school_library(models.Model):
     name=models.CharField(max_length=100)
     course=models.CharField(max_length=10)
     book_no=models.IntegerField()
     bookName=models.CharField(max_length=100)
     address=models.CharField(max_length=200)