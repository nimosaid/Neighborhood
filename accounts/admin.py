from django.contrib import admin

# Register your models here.
from accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','email',]
    
    
    
    
admin.site.register(Profile, ProfileAdmin)
