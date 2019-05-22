# In this file we will find our constants such as mysql identification
#along a list of the categories and product available

mysql_host = "localhost"
mysql_user = "root"
mysql_password="Vongola75"
mysql_database ="projet5"

categories_to_display =[(None,"Pizzas"),(None,"boissons-gazeuses"),(None,"snacks"),(None,"produits-laitiers"),(None,"frommage"),(None,"petit-dejeuners"),(None,"epicerie"),(None,"boissons-alcoolisees"),(None,"viandes")]

with open(r"files\Category.sql","r") as file:
    Category_table = file.read()
with open(r"files\Aliment.sql","r") as file:
    Aliment_table =file.read()
    