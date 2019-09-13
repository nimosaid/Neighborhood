from django.db import models
from django.contrib.auth.models import User
# from accounts.models import Profile




# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    
    
    class Meta:
        verbose_name  = "Neighborhood"
        verbose_name_plural  = "Neighborhoods"
    
    def __str__(self):
        return f'{self.name}'
    
    
    def count_occupants(self):
        pass

class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    
    
    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'

    
    def __str__(self):
        return f'{self.name}'
    
      
class Contact(models.Model):
    contact_type = models.CharField(max_length=70)# specifies whether its a fire, police, hosptial etc
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.contact_type}, {self.phone}'
    
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    body  = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
