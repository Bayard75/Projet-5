# In this file we will find our constants such as mysql identification
#along a list of the categories and product available
mysql_host = "localhost"
mysql_user = "root"
mysql_password="Vongola75"
mysql_database ="Pur_beurre"

categories_to_display =[(None,"Pizzas"),(None,"volailles"),(None,"snacks"),(None,"desserts"),(None,"frommage"),(None,"petit-dejeuners"),(None,"epicerie"),(None,"produits-a-tartiner"),(None,"charcuteries")]

with open(r"files\Category.sql","r") as file:
    Category_table = file.read()
with open(r"files\Aliment.sql","r") as file:
    Aliment_table =file.read()
with open(r"files\substitut.sql","r") as file:
    Substitut_table =file.read()


"""link = "https://fr.openfoodfacts.org/categorie/pizzas.json"

response = requests.get(link)
category_json = json.loads(response.text)
print(category_json["products"][5]["url"].replace("'","-"))
#sql_formula_aliment = f"INSERT INTO Aliment(id_aliment,name_aliment,category,store,grade,link) VALUES ({i},'{products['product_name_fr']}',{id_category},'{products['stores']}','{products['nutrition_grade_fr']}','{products['url']}')"
"""