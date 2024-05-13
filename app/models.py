from django.db import models
from django.contrib.auth.models import AbstractUser
from app.utils.utils import CustomModel

from django.utils.text import slugify



#La connexion au système
class User(AbstractUser):
    EMPTY       = 'empty'
    ADMIN       = 'admin' 
    MANAGER_A   = 'manager_a' #Regisseur des unités
    MANAGER_B   = 'manager_b' #Regisseur des ecoles
    KEPPER_A    = 'kepper_a' #Magasinier a
    KEPPER_B    = 'kepper_b' #Magasinier b
    PROVIDER    = 'provider' #Fournisseur
   
    CHOICES_ROLE = (
        (EMPTY, 'Empty'),  
        (ADMIN, 'Admin'),
        (MANAGER_A, 'Manager_a'),
        (MANAGER_B, 'Manager_b'),
        (KEPPER_A , 'Kepper_a'),
        (KEPPER_B,  'Kepper_b'),
        (PROVIDER,  'Provider')
    ) 
    matricule       = models.CharField(max_length=50, unique=True, blank=True, null=True)
    phone_number    = models.CharField(max_length=100, unique=True)
    email           = models.EmailField(max_length=150, unique=True)
    address         = models.CharField(max_length=200, blank=True, null=True)
    role            = models.CharField(choices=CHOICES_ROLE, default=EMPTY, max_length=20)
    image           = models.ImageField(upload_to='user_images/', default='user_images/default.jpg', blank=True, null=True)
    
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email','role', 'matricule', 'phone_number']

    def __str__(self) -> str:
        return self.email
    
    
#Chaque unité doit appartenir a une zone
class Area(CustomModel):
    name                = models.CharField(max_length=255)
    description         = models.TextField()


#Toutes les unites
class Unit(CustomModel):
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
    chief          = models.CharField(max_length=255, blank=True, null=True) # Chef d'unité
    effective      = models.IntegerField(default=1)
    duration       = models.IntegerField(default=0) #la durée de la mission ou formation
    description    = models.TextField()
    

    
#Les articles 
#Les peuvent fournires les produits
class Item(CustomModel):
    
    BAG       = 'bag' #Sac
    CAN       = 'can' #Bidon
    CARDBOARD = 'cardboard' # carton
    
    CHOICES_TYPE = (
        (BAG, 'Bag'),
        (CAN, 'Can'),
        (CARDBOARD, 'Cardboard'),
    )
    
    name                = models.CharField(max_length=100, unique=True)
    image               = models.ImageField(upload_to="Articles/%Y/",default='user_images/default.jpg')
    price               = models.IntegerField(default=0)
    rate_per_days       = models.DecimalField(max_digits=5, decimal_places=2)
    unite               = models.CharField(choices=CHOICES_TYPE, default=BAG, max_length=20)
    divider             = models.IntegerField(default=0) 
    description         = models.TextField(null=True, blank=True,)
    
#Apres avoir fait les bons de commande
#Les fournisseurs doivent livrer les articles commandés
#Les stocks des articles
#Les fournisseurs peuvent fournitures les produits
class itemStock(CustomModel):
    STORE_A = 'store_a'
    STORE_B = 'store_b'
    
    CHOICES_STORE = (
        (STORE_A, 'Store_a'),
        (STORE_B, 'Store_b'),
    )
    provider            = models.ForeignKey(User, related_name='providers', on_delete=models.CASCADE, blank=True, null=True)
    item                = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    quantity            = models.IntegerField(default=0)
    store_type          = models.CharField(choices=CHOICES_STORE, default=STORE_A, max_length=10)
    
#Les bons de commandes
#On peut faire un bon de commande vue la quantité en stock 
class Order(CustomModel):
    
    provider            = models.ForeignKey(User, related_name='provider_order', on_delete=models.CASCADE, blank=True, null=True)
    item                = models.ForeignKey(Item, related_name='item_order', on_delete=models.CASCADE)
    status              = models.BooleanField(default=True)
    quantity            = models.IntegerField(default=0)


#les unités peuvent avoir besion des depenses en plus les denrees
class Menu(CustomModel):
    
    FOOD  = 'food'
    OTHER = 'other'
    
    CHOICES_TYPE = (
        (FOOD, 'Food'),
        (OTHER, 'Other')
    )
    
    name                = models.CharField(max_length=255)
    type                = models.CharField(choices=CHOICES_TYPE, default=FOOD, max_length=10)
    #amount              = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    description         = models.TextField()
    
    
#Les regies peuvent faire les boredereaux afin de servire les unites
#ou les indivudus.
class Discharge(CustomModel):
    SLIP  = 'slip' #Bordereau
    CERT  = 'cert' #Bon de sorti
    
    CHOICES_TYPE = (
        (SLIP, 'Slip'),
        (CERT, 'Cert')
    )
    
    type                = models.CharField(choices=CHOICES_TYPE, default=SLIP, max_length=10)
    offset              = models.IntegerField(default=0)  # La compensation de pour les unites
    item                = models.ForeignKey(Item, related_name='items_disch', on_delete=models.CASCADE,blank=True, null=True)
    Menu                = models.ForeignKey(Menu, related_name='menus', on_delete=models.CASCADE)
    unit                = models.ForeignKey(Unit, related_name='units', on_delete=models.CASCADE)
    discharged          = models.BooleanField(default=False)
    file                = models.FileField(upload_to="Decharges/%Y/", blank=True, null=True)


