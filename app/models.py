from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.text import slugify
from django.db.models.signals import pre_save


# Table "Utilisateurs" :

#La connexion au système
class User(AbstractUser):
    EMPTY       = 'empty'
    ADMIN       = 'admin' 
    MODERATOR   = 'moderator' #Ceux la qui mettent les offres d'emplois en ligne
   
    CHOICES_ROLE = (
        (EMPTY, 'Empty'),  
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
    ) 
    matricule       = models.CharField(max_length=50, unique=True)
    phone_number    = models.CharField(max_length=100, unique=True)
    email           = models.EmailField(max_length=150, unique=True)
    role            = models.CharField(choices=CHOICES_ROLE, default=EMPTY, max_length=20)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','role']

    def __str__(self) -> str:
        return self.email

