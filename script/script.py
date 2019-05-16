import os, mysql.connector, requests, json, classes, constants

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)

mycursor= mydb.cursor()

"""r= requests.get("https://fr.openfoodfacts.org/categories.json")

categories_json = json.loads(r.text)
categories_count =categories_json["count"]
sqlFormula_categories_names ="INSERT INTO categorie (id, nom) VALUES (%s, %s)"
categorie_name=[]
i = 0
while i < categories_count:
    try :
       categorie_name.append((i,categories_json["tags"][i]["name"]))
    except:
        break
    i+=1

mycursor.executemany(sqlFormula_categories_names,categorie_name)
mydb.commit()
"""
show_categories = "SELECT * FROM categorie"
mycursor.execute(show_categories)

for categorie in mycursor:
    print(categorie)
os.system("pause")