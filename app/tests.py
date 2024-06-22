# from django.test import TestCase

# Create your tests here.
# import calendar
# from datetime import datetime

# # Obtenir le mois et l'année courants
# current_date = datetime.now()
# current_year = current_date.year
# current_month = current_date.month

# # Obtenir le nombre de jours du mois courant
# days_in_month = calendar.monthrange(current_year, current_month)[1]

# print(f"Le nombre de jours dans le mois courant ({current_month}/{current_year}) est : {days_in_month}")


from datetime import datetime

# Liste des dates
dates = [
    "2024-06-15 06:19:45.536379",
    "2024-06-15 06:22:42.784420",
    "2024-06-15 06:23:37.725327",
    "2024-06-15 06:24:06.041552",
    "2024-06-18 23:26:56.401293",
    "2024-06-19 07:19:31.105015",
    "2024-07-19 07:28:03.598786",
    "2024-07-19 07:28:35.091167",
    "2024-07-19 09:29:45.594623",
    "2024-07-19 09:35:34.402269",
    "2024-08-19 09:37:38.470233",
]

# Utilisation d'un set pour stocker les couples (année, mois) uniques
unique_year_month = set()

for date_str in dates:
    # Conversion de la chaîne de caractères en objet datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    # Ajout du tuple (année, mois) au set
    unique_year_month.add((date_obj.year, date_obj.month))

# Conversion du set en liste et tri pour l'affichage
unique_year_month = list(unique_year_month)

print("Les valeurs distinctes d'année et de mois sont :")
print(unique_year_month)
for year, month in unique_year_month:
    print(f"Année: {year}, Mois: {month}")
