import os, mysql.connector, requests, json, constants,classes

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)

mycursor= mydb.cursor()
projet5 = classes.Database(mydb,mycursor,constants.Category_table,constants.Aliment_table)
print("Les tables on bien été créees.\n")

projet5.insert_values()
print("Les données ont été inséré dans toutes les catégories sans soulever d'expections.\n")
print("Tous c'est bien passé.\n")
print("Veuillez selectionner une catégorie dans la table suivante :")

projet5.category_choice()

os.system("pause")