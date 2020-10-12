from django.contrib import admin
from .models import Login

class LoginAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'telefono', 'mail']

admin.site.register(Login, LoginAdmin)


# Register your models here.
