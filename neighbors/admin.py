from django.contrib import admin
# Register your models here.

from neighbors.models import Neighborhood, Business, Contact, Post



    
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ['name','address','city']


class BusinessAdmin(admin.ModelAdmin):

    list_display = ['name','user','neighborhood','city']
    
    
    
    
class ContactsAdmin(admin.ModelAdmin):
    
    list_display = ['contact_type','phone','email','posted_by']
    
    
    
    
class PostsAdmin(admin.ModelAdmin):
    
    list_display = ['title','author','neighborhood','pub_date']



admin.site.register(Business, BusinessAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Contact, ContactsAdmin)
admin.site.register(Post, PostsAdmin)