from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from neighbors.models import Neighborhood

# Create your tests here.


class UserTestClass(TestCase):

    def setUp(self):
        self.user1 = User(
            username = 'test1',
            password =  'tehsingpass'
        )
        self.neigborhood = Neighborhood(name='twst',
                                        location='testloc',
                                        address = '1234 Road',
                                        city = 'Nairobi')
        self.profile1 = Profile (
 
             user = self.user1,
             photo = 'pic.jpg',
             email = 'gabriel.oduori@gmail.com',
             neigborhood = self.neigborhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.user1, User))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile1, Profile))
        
