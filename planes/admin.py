from django.contrib import admin
from .models import Plan

# Register your models here.

<<<<<<< HEAD
admin.site.register(Plan)
=======
@admin.register(Plan)
class AutorAdmin(admin.ModelAdmin):
    pass

class registro1Admin(admin.ModelAdmin):
    list_display = ('nombre','apellido','rut','comuna','email','nombre_usario')
    fields=[('nombre','apellido','rut'),'comuna','email','nombre_usario']

#admin.site.register(registro1)
>>>>>>> master
