from django.contrib import admin

# Register your models here.
from .models import CrudUser,Creador

admin.site.register(CrudUser)
admin.site.register(Creador)
