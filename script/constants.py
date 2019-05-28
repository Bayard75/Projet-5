# In this file we will find our constants such as mysql identification
#along a list of the categories and product available

mysql_host = "localhost"
mysql_user = "root"
mysql_password="Vongola75"
mysql_database ="Pur_beurre"

categories_to_display =[(None,"Pizzas"),(None,"volailles"),(None,"snacks"),(None,"desserts"),(None,"fromage"),(None,"petit-dejeuners"),(None,"epicerie"),(None,"produits-a-tartiner"),(None,"charcuteries")]

with open(r"files\Category.sql","r") as file:
    Category_table = file.read()
with open(r"files\Aliment.sql","r") as file:
    Aliment_table =file.read()
with open(r"files\substitut.sql","r") as file:
    Substitut_table =file.read()
