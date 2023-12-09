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
    chief          = models.CharField(max_length=255) # Chef d'unité
    effective      = models.IntegerField(default=0)
    description    = models.TextField()
    
    
    
#Les fournisseurs
class Provider(models.Model):
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='F')
    name                = models.CharField(max_length=255)
    phone_number        = models.CharField(max_length=50)
    email               = models.EmailField(max_length=100, null=True)
    address             = models.CharField(max_length=200)
    
    
#Les articles 
#Les peuvent fournires les produits
class Item(models.Model):
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='P')
    name                = models.CharField(max_length=100)
    image               = models.ImageField(upload_to="Articles/%Y/")
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_person     = models.DecimalField(max_digits=5, decimal_places=2)
    description         = models.TextField()
    
#Les stocks des articles
#Les fournisseurs peuvent fournires les produits
class itemStock(models.Model):
    STORE_A = 'store_a'
    STORE_B = 'store_b'
    
    CHOICES_STORE = (
        (STORE_A, 'Store_a'),
        (STORE_B, 'Store_b'),
    )
    
    
    provider            = models.ForeignKey(Provider, related_name='providers', on_delete=models.CASCADE)
    item                = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    quantity            = models.IntegerField(default=0)
    store_type          = models.CharField(choices=CHOICES_STORE, default=STORE_A)
    modified_at         = models.DateTimeField(auto_now_add=True)
    
    
#Les bons de commandes
#On peut faire un bon de commande vue la quantité en stock 
class Order(models.Model):
    
    STORE_A = 'store_a'
    STORE_B = 'store_b'
    
    CHOICES_STORE = (
        (STORE_A, 'Store_a'),
        (STORE_B, 'Store_b'),
    )
    
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='BC')
    provider            = models.ForeignKey(Provider, related_name='provider_order', on_delete=models.CASCADE)
    item                = models.ForeignKey(Item, related_name='item_order', on_delete=models.CASCADE)
    store_type          = models.CharField(choices=CHOICES_STORE, default=STORE_A)
    quantity            = models.IntegerField(default=0)
    created_at          = models.DateTimeField(auto_now_add=True)

    
#Apres avoir fait les bons de commande
#Les fournisseurs doivent livrer les articles commandé
class Delivery(models.Model):
    
    STORE_A = 'store_a'
    STORE_B = 'store_b'
    
    CHOICES_STORE = (
        (STORE_A, 'Store_a'),
        (STORE_B, 'Store_b'),
    )
    
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='L')
    provider            = models.ForeignKey(Provider, related_name='provider_delivery', on_delete=models.CASCADE)
    item                = models.ForeignKey(Item, related_name='item_delivery', on_delete=models.CASCADE)
    store_type          = models.CharField(choices=CHOICES_STORE, default=STORE_A)
    quantity            = models.IntegerField(default=0)
    created_at          = models.DateTimeField(auto_now_add=True)

    
    