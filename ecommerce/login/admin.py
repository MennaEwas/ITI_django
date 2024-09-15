from django.contrib import admin
from .models import Login

# Register your models here.
admin.site.site_header = 'New Django Admin Panel'

class LoginAdmin(admin.ModelAdmin):
    list_display = ['username']
    # list_editable = ['password']
    
admin.site.register(Login, LoginAdmin)
