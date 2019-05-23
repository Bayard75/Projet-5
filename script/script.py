import os, mysql.connector, requests, json, constants,classes

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)

mycursor= mydb.cursor()
projet5 = classes.Database(mydb,mycursor,constants.Category_table,constants.Aliment_table)
print("Les tables on bien été créees.")
projet5.insert_values(1,"pizzas")
print("Les données on été inséré pour les pizzas.")
print("Tous c'est bien passé.")
os.system("pause")