from django.contrib import admin
from .models import Post,Tag,Service, Project
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Service)
admin.site.register(Project)