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
    REQUIRED_FIELDS = ['email','role', 'matricule', 'phone_number', 'get_full_name', 'get_short_name', 'image']

    def __str__(self) -> str:
        return self.email
    
    
class CustomFields(models.Model):
    name                = models.CharField(max_length=255, unique=True)
    status              = models.BooleanField(default=True)
    description         = models.TextField(blank=True,null=True)


#Toutes les unites
class Unit(CustomModel, CustomFields):
    UNIT        = 'unit' # Pour les unites
    SCHOOL      = 'school' # pour les ecoles;
    SERVICE     = 'service' # pour les services
    
    CHOICES_CATEGORY = (
        (UNIT, 'Unit'),
        (SCHOOL, 'School'),
        (SERVICE, 'Service'),
    ) 
    
    CURRENT     = 'current' # courant
    MISSION     = 'mission'
    SINGLE      = 'single'
    
    CHOICES_TYPE_OF_UNIT = (
        (CURRENT , 'Current'),
        (MISSION, 'Mission'),
        (SINGLE, 'Single')  
    ) 
    
    EMAT = 'emat'
    EMAA = 'emaa'
    EMAM = 'emam'
    HCGN = 'hcgn'
    
    GENERAL_STAFF = (
        (EMAT, 'Emat'),
        (EMAA, 'Emaa'),
        (EMAM, 'Emam'),
        (HCGN, 'Hcgn'),
    )
    
    SPECIALE_AREA   = 'speciale'    #Zone sepeciale
    FIRST_AREA      = 'first'       #Prèmire region
    SECOND_AREA     = 'second'      # Deuxième region Militaire
    THIRD_AREA      = 'third'       # Troisième region Militaire
    FOURTH_AREA     = 'fourth'      # Quatrième region Militaire
    
    MILITARY_AREA = (
        (SPECIALE_AREA, 'Speciale'),
        (FIRST_AREA, 'First'),
        (SECOND_AREA, 'Second'),
        (THIRD_AREA, 'Third'),
        (FOURTH_AREA, 'Fourth'),
    )

    image          = models.ImageField(upload_to="Unit/%Y/",default='user_images/default.jpg')
    short_name     = models.CharField(max_length=50, default="NULL", unique=True)
    recipient      = models.CharField(max_length=200, default="NULL")
    g_staff        = models.CharField(choices=GENERAL_STAFF, default=EMAT, max_length=20)
    area           = models.CharField(choices=MILITARY_AREA, default=SPECIALE_AREA, max_length=100)
    type_of_unit   = models.CharField(choices=CHOICES_TYPE_OF_UNIT, default=CURRENT, max_length=20)
    category       = models.CharField(choices=CHOICES_CATEGORY, default=UNIT, max_length=20)
    effective      = models.IntegerField(default=1)
  
    
    
#Chaque unité doit appartenir a une zone
class SubArea(CustomModel, CustomFields):
    
    SPECIALE_AREA   = 'speciale'    #Zone sepeciale
    FIRST_AREA      = 'first'       #Prèmire region
    SECOND_AREA     = 'second'      # Deuxième region Militaire
    THIRD_AREA      = 'third'       # Troisième region Militaire
    FOURTH_AREA     = 'fourth'      # Quatrième region Militaire
    
    MILITARY_AREA = (
        (SPECIALE_AREA, 'Speciale'),
        (FIRST_AREA, 'First'),
        (SECOND_AREA, 'Second'),
        (THIRD_AREA, 'Third'),
        (FOURTH_AREA, 'Fourth'),
    )
    
    
    area                = models.CharField(choices=MILITARY_AREA, default=SPECIALE_AREA, max_length=100)
    
   
#Les peuvent fournires les produits
class Item(CustomModel, CustomFields):      
    
    BAG       = 'bag' #Sac
    CAN       = 'can' #Bidon
    CARDBOARD = 'cardboard' # carton
    
    CHOICES_TYPE = (
        (BAG, 'Bag'),
        (CAN, 'Can'),
        (CARDBOARD, 'Cardboard'),
    )
    

    
    image               = models.ImageField(upload_to="Articles/%Y/",default='user_images/default.jpg')
    price               = models.IntegerField(default=0)
    rate_per_days       = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    unite               = models.CharField(choices=CHOICES_TYPE, default=BAG, max_length=20)
    divider             = models.IntegerField(default=0) 
    weight              = models.FloatField(default=0) # Le poid 
    

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
    provider            = models.ForeignKey(User, related_name='provider_order', on_delete=models.CASCADE)
    status              = models.BooleanField(default=True)
    
# C'est une table qui relie la table order et la commande
#Ligne de commande
class OrderLine(models.Model):
    item                = models.ForeignKey(Item, related_name='item_order', on_delete=models.CASCADE)
    order               = models.ForeignKey(Order, related_name='orderItem', on_delete=models.CASCADE)
    quantity            = models.IntegerField(default=0)
   


#Les regies peuvent faire les boredereaux afin de servire les unites
#ou les indivudus.CustomModel
class Discharge(CustomModel):
    SLIP  = 'slip' #Bordereau
    CERT  = 'cert' #Bon de sorti
    
    CHOICES_TYPE = (
        (SLIP, 'Slip'),
        (CERT, 'Cert')
    )
        
    FULL        = 'full' # BORDEREAUX COMPLET
    KIND        = 'espece' # BORDEREAUX ESPECE;
    
  
    CHOICES_CATEGORY = (
        (FULL, 'Full'), #COMPLETE
        (KIND, 'Kind'), #ESPECE
    )
  
    discharged          = models.BooleanField(default=False)
    
    type_disch          = models.CharField(choices=CHOICES_TYPE, default=SLIP, max_length=10)
    category            = models.CharField(choices=CHOICES_CATEGORY, default=FULL, max_length=10)
    file                = models.FileField(upload_to="Decharges/%Y/", blank=True, null=True)
    start_at            = models.DateTimeField(default=None , blank=True, null=True)
    end_at              = models.DateTimeField(default=None , blank=True, null=True)

    def __str__(self):
        return f"Event from {self.start} to {self.end}"  
    
#Les lignes des bordereaux
class DischargedLines(models.Model):
    discharge       = models.ForeignKey(Discharge, related_name='discharge_line', on_delete=models.CASCADE)
    unit            = models.ForeignKey(Unit, related_name='dischargelines_units', on_delete=models.CASCADE)
    offset          = models.IntegerField(default=0)  # La compensation de pour les unites
    forfait         = models.BooleanField(default=False)
    item            = models.ForeignKey(Item, related_name='item_line_disch', on_delete=models.CASCADE)
    
#les unités peuvent avoir besion des depenses en plus les denrees
class Spend(CustomModel, CustomFields):
    
    FOOD  = 'food'# Les menu depenses
    OTHER = 'other'# Les autres dépenses
    SPEND = 'spend'# Les dépenses
    
    CHOICES_TYPE = (
        (FOOD, 'Food'),
        (OTHER, 'Other'),
        (SPEND, 'Spend'),
    )
    
    image               = models.ImageField(upload_to='menu_images/', default='user_images/default.jpg', blank=True, null=True)
    type_menu           = models.CharField(choices=CHOICES_TYPE, default=FOOD, max_length=10)
    rate                = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price               = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    discharges          = models.ForeignKey(Discharge, related_name='spens_disch', on_delete=models.CASCADE, null=True)
      



#La gestion du temps
################################
 
class Archives(models.Model):
    order            = models.ForeignKey(Order, related_name='order_archiv', on_delete=models.CASCADE, null=True)
    discharge        = models.ForeignKey(Discharge, related_name='discharge_archiv', on_delete=models.CASCADE, null=True)
    date             = models.DateField(auto_now_add=True)
    nomber_of_days   = models.IntegerField(default=0)
  
        
## LES CLASSES 

##Les signateurs
class SignalOperators(CustomModel):

    DEFAULT = 'default'
    LEFT    = 'left' #Premier signateur
    RIGHT   = 'right' # Deuxième signateur
    CENTER  = 'center' # Troisième signateur
    
    CHOICES_POS = (
       (DEFAULT, 'Default'), (LEFT, 'Left'), (RIGHT, 'Right'), (CENTER, 'Center'),
    )# Les différentes position des signatures
    
    grade           = models.CharField(max_length=200)
    first_name      = models.CharField(max_length=200)
    last_name       = models.CharField(max_length=200)
    function_name   = models.CharField(max_length=200)
    title           = models.CharField(max_length=200)
    position        = models.CharField(choices=CHOICES_POS, default=DEFAULT, max_length=20,  unique=True)
    
    
