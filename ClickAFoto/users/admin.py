from django.contrib import admin
from .models import Login, Photographers, Statistics
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Login, UserAdmin)
admin.site.register(Photographers)
admin.site.register(Statistics)

#https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#a-full-example