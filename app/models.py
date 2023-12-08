from django.db import models
from django.contrib.auth.models import AbstractUser

from app.utils.utils import CustomPrimaryKeyField

from django.utils.text import slugify




#La connexion au système
class User(AbstractUser):
    EMPTY       = 'empty'
    ADMIN       = 'admin' 
    MANAGER_A   = 'manager_a' #Regisseur des unités
    MANAGER_B   = 'manager_b' #Regisseur des ecoles
    KEPPER_A    = 'kepper_a' #Magasinier a
    KEPPER_B    = 'kepper_b' #Magasinier b
   
    CHOICES_ROLE = (
        (EMPTY, 'Empty'),  
        (ADMIN, 'Admin'),
        (MANAGER_A, 'Manager_a'),
        (MANAGER_B, 'Manager_b'),
        (KEPPER_A , 'Kepper_a'),
        (KEPPER_B, 'Kepper_b'),
    ) 
    matricule       = models.CharField(max_length=50, unique=True)
    phone_number    = models.CharField(max_length=100, unique=True)
    email           = models.EmailField(max_length=150, unique=True)
    role            = models.CharField(choices=CHOICES_ROLE, default=EMPTY, max_length=20)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','role']

    def __str__(self) -> str:
        return self.email


#Toutes les unites
class Unit(models.Model):
    UNIT        = 'unit'
    SCHOOL      = 'school'
    MISSION     = 'mission'
    SERVICE     = 'service'
   
    CHOICES_TYPE = (
        (UNIT, 'Unit'),
        (SCHOOL, 'School'),
        (MISSION, 'Mission'),
        (SERVICE , 'Service')    
    ) 
    
    name           = models.CharField(max_length=255)
    type           = models.CharField(choices=CHOICES_TYPE, default=UNIT, max_length=20)
    description    = models.TextField()
    