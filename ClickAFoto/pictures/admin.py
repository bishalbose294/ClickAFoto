from django.contrib import admin
from .models import  Pictures, Ratings, Comments, Likes

# Register your models here.
admin.site.register(Pictures)
admin.site.register(Ratings)
admin.site.register(Comments)
admin.site.register(Likes)