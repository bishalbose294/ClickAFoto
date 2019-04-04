from django.contrib import admin
from .models import ContestRegisters, Contests, Categories

# Register your models here.
admin.site.register(ContestRegisters)
admin.site.register(Contests)
admin.site.register(Categories)