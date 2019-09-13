
from django.test import TestCase
from neighbors.models import Neighborhood, Business, Contact, Post
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class NeighborhoodTestClass(TestCase):
    
    def setUp(self):
        self.hood = Neighborhood(
             name ='Kasarani',
             location = 'Kasarani',
             address = '1234 SpringRoad',
             city = 'Nairobi')
         
         
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood))
         
        
        
    def tearDown(self):
        Neighborhood.objects.all().delete()

   

    
    