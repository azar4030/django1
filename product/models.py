from django.db import models

# Create your models here.
class catagory(models.Model):
    name=models.CharField(max_length=50)
    parent_id=models.IntegerField(max_length=10)
class product(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    comment = models.TextField()
    view = models.IntegerField(20)
    acttive = models.IntegerField(default=1)
    create_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(20)
    catagory_id = models.IntegerField(20)
class product_catogory(models.Model):
    catagory_id = models.IntegerField(20)
    product_id = models.IntegerField(max_length=10)
class image (models.Model):
    product_id = models.IntegerField(max_length=10)
    url = models.CharField(max_length=200)
    cover = models.IntegerField(default=0)
class group(models.Model):
    name = models.CharField(max_length=50)
class group_product (models.Model):
    group_id = models.IntegerField(20)
    product_id = models.IntegerField(max_length=10)
class combine(models.Model):
    product_id = models.IntegerField(max_length=10)
    attribute_id = models.CharField(max_length=100)
    price = models.IntegerField(20)
    count = models.IntegerField(20)
class attribute(models.Model):
    group_id = models.IntegerField(20)
    name = models.CharField(max_length=50)
    value = models.IntegerField(20)
class feature (models.Model):
    pass
class feature_value (models.Model):
    pass













