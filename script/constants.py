"""In this file we will find our constants such as mysql identification
along a list of the categories and product available"""

#The user only has to enter these 4 parameters before starting the program
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD="Vongola75"
MYSQL_DATABASE ="Pur_beurre"

CATEGORIES_TO_DISPLAY =[(None,"Pizzas"),(None,"volailles"),(None,"snacks"),(None,"desserts"),(None,"fromage"),(None,"petit-dejeuners"),(None,"epicerie"),(None,"produits-a-tartiner"),(None,"charcuteries")]

with open(r"files\Category.sql","r") as file:
    CATEGORY_TABLE = file.read()
with open(r"files\Aliment.sql","r") as file:
    ALIMENT_TABLE =file.read()
with open(r"files\substitut.sql","r") as file:
    SUBSTITUT_TABLE =file.read()
with open(r"files\Favorite.sql","r") as file:
    FAVORITE_TABLE =file.read()

try :
    with open(r"files\aliment_status.txt","r") as file:
        ALIMENT_STATUS = file.read()
except:
        ALIMENT_STATUS = "Not Done"
