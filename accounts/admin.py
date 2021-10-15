from django.contrib import admin

# Register your models here.
from .models import Person

admin.site.register(Person)

# class Personadmin(Person.ModelAdmin):
#     list_display= ('name', 'phone', 'city', 'address')
    
  
# admin.site.register(Person, Personadmin)