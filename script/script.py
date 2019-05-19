import os, mysql.connector, requests, json
import classes
import constants

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)

mycursor= mydb.cursor()

projet5 = classes.Database(mydb,mycursor)
projet5.create_category_table