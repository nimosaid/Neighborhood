from django import forms
from neighbors.models import Neighborhood, Business, Contact, Post

class AddNeighborhoodForm(forms.ModelForm):
    class Meta:
        
        model = Neighborhood
        fields = (
            'name',
            'location',
            'address',
            'city'
            )
    
    

class AddBusinessForm(forms.Form):
    class Meta:
        model = Business
        fields = (
            'name',
            'address',
            'city'
        )
        
class AddContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = (
            'contact_type',
            'phone',
            'email',
            'neighborhood',
            'posted_by'
        )
        
        
class AddPostForm(forms.Form):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'author',
            'neighborhood',
            'pub_date'
        )