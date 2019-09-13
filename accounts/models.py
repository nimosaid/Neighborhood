from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from neighbors.models import Neighborhood
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = 'profiles/')
    email = models.EmailField(blank=True)
    neigborhood = models.ForeignKey(Neighborhood,  on_delete=models.CASCADE, related_name='area')
    
    def __str__(self):
        return f'{self.user.username}'

'''
We dont have to create profiles every time a user signs up. Instead,
we are going to use django signals to get that done automatically.
'''


