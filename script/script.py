import os, mysql.connector, requests, json, classes, constants

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)

mycursor= mydb.cursor()

sqlFormula_categories ="INSERT INTO categorie (id,nom) VALUES (%s,%s)"

