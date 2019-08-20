# Projet-5
Utilisation d'une API pour créer une base de données permetant la substitution d'aliments grâce à Python
=======
Ce programme a pour but de reprondre à la demande suivante :

-En tant qu'utilisateur je veux pouvoir trouver un substitut pour mieux m'alimenter

Pour ce faire il aura les fonctionnalités suivantes :

-L'utilisateur aura le choix entre plusieurs catégories d'aliments
-Apres avoir fait son choix dans ses catégories il aurait accés aux aliments de cette catégorie
-Ensuite il choisira un aliment à substitué et le programme lui renvoira un autre aliment de la même catégorie avec le nutri-score le plus élévé
-L'utilsateur aura, alors, la possiblité d'enregistrer cette recherche pour y accéder ultérieurement

Notre programme répond donc aux besoins suivant :                                                                                         
-En tant qu'utilisateur je veux avoir un catalogue de produits pour visualiser les différents choix possibles et/ou me donner des idées de substitutions

-En tant qu’utilisateur je veux pouvoir sélectionner un aliment précis pour trouver un substitut rapidement

-En tant qu'utilisateur je veux pouvoir retrouver mes anciennes recherches pour y retrouver les informations sur les produits

L'utilisateur devra obligatoirement rentrer ses identifiants/mot de passe/base de données dans le fichier constants.py.

Ce programme fera appel à l'API d'OPENFOODFACTS, utilisera mysql pour créer une base de données et des scripts python pour intéragir entre les différentes table de la base de données.

###Installation de MySQL
=======
Il vous faudra  installer mySQL:
Vous pouvez suivre les indications donner par ce tutoriel:
https://openclassrooms.com/fr/courses/1959476-administrez-vos-bases-de-donnees-avec-mysql/1959969-installez-mysql#/id/r-2064496

##Prérequis
=======

Pour faire fonctionner ce programme il vous faudra installer un environnement virtuel.
Pour cela il faudra taper les lignes suivantes dans votre **prompt**
```
cd Chemin\vers\le\dossier
virtualenv nom_de_votre_env
```
Ensuite sous Windows :
```
nom_env\Scripts\activate
pip install -r requirements.txt
```
Sous Mac/Linux :
```
source mypython/bin/activate
pip install -r requirements.txt
```

##Renseignez vos informations
=======
Maintenant que vous avez tout installé il ne vous reste plus qu'à ouvrir le fichier **constants.py** avec votre editeur de texte préferé (bloc notes marche très bien) et à remplir les lignes suivantes:
```
MYSQL_HOST = "    "
MYSQL_USER = "    "
MYSQL_PASSWORD = "    "
```
**Attention laissé bien les " "**

##Lancement du programme
=======
Retour à votre prompt pour lancer le programme rentré la ligne suivante:
```
python script\script.py
```
Enjoy !


