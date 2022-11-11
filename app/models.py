from django.db import models

# Create your models here.
class Form(models.Model):
    name= models.CharField(max_length=100),
    phone= models.IntegerField(),
    email= models.EmailField(),
    address=models.CharField(max_length=200)

    class Meta:
      db_table = 'Form'


# class Sorm(models.Model):
#     name= models.CharField(max_length=100),
#     phone= models.IntegerField(),
#     email= models.EmailField(),
#     address=models.CharField(max_length=200)

#     class Meta:
#       db_table = 'Sorm'