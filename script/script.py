import os, mysql.connector, requests, json, constants,classes

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)

mycursor= mydb.cursor()
print(constants.mysql_host)
projet5 = classes.Database(mydb,mycursor,constants.Category_table,constants.Aliment_table)

os.system("pause")