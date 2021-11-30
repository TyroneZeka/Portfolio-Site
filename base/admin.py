from django.contrib import admin
from .models import Post,Tag,Services, Project
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Services)
admin.site.register(Project)