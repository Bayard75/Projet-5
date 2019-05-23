# In this file we will find our constants such as mysql identification
#along a list of the categories and product available
import requests, json
mysql_host = "localhost"
mysql_user = "root"
mysql_password="Vongola75"
mysql_database ="projet5"

categories_to_display =[(None,"Pizzas"),(None,"boissons-gazeuses"),(None,"snacks"),(None,"produits-laitiers"),(None,"frommage"),(None,"petit-dejeuners"),(None,"epicerie"),(None,"boissons-alcoolisees"),(None,"viandes")]
with open(r"files\Category.sql","r") as file:
    Category_table = file.read()
with open(r"files\Aliment.sql","r") as file:
    Aliment_table =file.read()

"""link = "https://fr.openfoodfacts.org/categorie/pizzas.json"
response = requests.get(link)
category_json = json.loads(response.text)
category_array =[]
for i in range(0,19):
    try :
        category_array.append(category_json["products"][i]["stores_tags"])
    except KeyError:
        category_array.append(None)
print (category_array)"""