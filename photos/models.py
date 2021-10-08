from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=20)

    
class Category(models.Model):
    name = models.CharField(max_length=20)