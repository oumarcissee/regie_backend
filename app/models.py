from django.db import models
from django.contrib.auth.models import AbstractUser

from app.utils.utils import CustomPrimaryKeyField, CustomDate

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
    
    
#Chaque unité doit appartenir a une zone
class Area(CustomDate, models.Model):
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='Z')
    name                = models.CharField(max_length=255)
    description         = models.TextField()

#Toutes les unites
class Unit(CustomDate, models.Model):
    UNIT        = 'unit'
    SCHOOL      = 'school'
    MISSION     = 'mission'
    SERVICE     = 'service'
    SINGLE      = 'single'
   
    CHOICES_TYPE = (
        (UNIT, 'Unit'),
        (SCHOOL, 'School'),
        (MISSION, 'Mission'),
        (SERVICE , 'Service'),
        (SINGLE, 'Single')  
    ) 
    area           = models.ForeignKey(Area, related_name='area_unit', on_delete=models.CASCADE)
    name           = models.CharField(max_length=255)
    type           = models.CharField(choices=CHOICES_TYPE, default=UNIT, max_length=20)
    chief          = models.CharField(max_length=255) # Chef d'unité
    effective      = models.IntegerField(default=0)
    duration       = models.IntegerField(default=0) #la durée de la mission ou formation
    description    = models.TextField()
    
    
#Les fournisseurs                                       
class Provider(CustomDate, models.Model):
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='F')
    name                = models.CharField(max_length=255)
    phone_number        = models.CharField(max_length=50)
    email               = models.EmailField(max_length=100, null=True)
    address             = models.CharField(max_length=200)
    
    
#Les articles 
#Les peuvent fournires les produits
class Item(CustomDate, models.Model):
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='P')
    name                = models.CharField(max_length=100)
    image               = models.ImageField(upload_to="Articles/%Y/")
    price               = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    rate_per_person     = models.DecimalField(max_digits=5, decimal_places=2)
    divider             = models.IntegerField(default=0) 
    description         = models.TextField()
    
#Apres avoir fait les bons de commande
#Les fournisseurs doivent livrer les articles commandé
#Les stocks des articles
#Les fournisseurs peuvent fournitures les produits
class itemStock(CustomDate, models.Model):
    STORE_A = 'store_a'
    STORE_B = 'store_b'
    
    CHOICES_STORE = (
        (STORE_A, 'Store_a'),
        (STORE_B, 'Store_b'),
    )
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='S')
    provider            = models.ForeignKey(Provider, related_name='providers', on_delete=models.CASCADE)
    item                = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    quantity            = models.IntegerField(default=0)
    store_type          = models.CharField(choices=CHOICES_STORE, default=STORE_A)
    
  
#Les bons de commandes
#On peut faire un bon de commande vue la quantité en stock 
class Order(CustomDate, models.Model):
    
    STORE_A = 'store_a'
    STORE_B = 'store_b'
    
    CHOICES_STORE = (
        (STORE_A, 'Store_a'),
        (STORE_B, 'Store_b'),
    )
    
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='C')
    provider            = models.ForeignKey(Provider, related_name='provider_order', on_delete=models.CASCADE)
    item                = models.ForeignKey(Item, related_name='item_order', on_delete=models.CASCADE)
    store_type          = models.CharField(choices=CHOICES_STORE, default=STORE_A)
    quantity            = models.IntegerField(default=0)


#les unités peuvent avoir besion des depenses en plus les denrees
class Menu(CustomDate, models.Model):
    
    FOOD  = 'food'
    OTHER = 'other'
    
    CHOICES_TYPE = (
        (FOOD, 'Food'),
        (OTHER, 'Other')
    )
    
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='D')
    name                = models.CharField(max_length=255)
    type                = models.CharField(choices=CHOICES_TYPE, default=FOOD)
    #amount              = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    description         = models.TextField()
    
    
#Les regies peuvent faire les boredereaux afin de servire les unites
#ou les indivudus.
class Discharge(CustomDate, models.Model):
    SLIP  = 'slip' #Bordereau
    CERT  = 'cert' #Bon de sorti
    
    CHOICES_TYPE = (
        (SLIP, 'Slip'),
        (CERT, 'Cert')
    )
    
    custom_id           = CustomPrimaryKeyField(primary_key=True, prefix='B')
    type                = models.CharField(choices=CHOICES_TYPE, default=SLIP)
    item                = models.ForeignKey(Item, related_name='items_disch', on_delete=models.CASCADE,blank=True, null=True)
    Menu                = models.ForeignKey(Menu, related_name='menus', on_delete=models.CASCADE)
    unit                = models.ForeignKey(Unit, related_name='units', on_delete=models.CASCADE)
    discharged          = models.BooleanField(default=False)
    file                = models.FileField(upload_to="Decharges/%Y/", blank=True, null=True)

    