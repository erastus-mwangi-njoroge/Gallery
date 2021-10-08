from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', default=None)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    uploader = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

