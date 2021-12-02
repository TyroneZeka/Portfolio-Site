from django.db import models
import uuid

from django.utils.translation import deactivate 

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,null=False,blank=False,unique=True)
    author = models.CharField(max_length=100, default='Tyrone',editable=False)
    sub_title = models.CharField(max_length=255,null=True,blank=True)
    thumbnail = models.ImageField(null=True, blank =True, default="default.jpg")
    body = models.TextField(null = True,blank = True)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default = False)
    tags = models.ManyToManyField('Tag', blank=True) 
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True,blank=True,default='default.jpg')
    body = models.TextField(null = True,blank = True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    slug = models.CharField(max_length=255,null=False,blank=False,unique=True)

    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # blank is for making a post request/form upload and null for database
    thumbnail = models.ImageField(null=True, blank =True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null = True, blank=True)
    source_link = models.CharField(max_length=2000, null= True, blank = True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    slug = models.CharField(max_length=255,null=False,blank=False,unique=True)

    def __str__(self) -> str:
        return self.title