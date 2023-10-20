## Projet : Application de Calcul de l'IMC avec Sauvegarde en Base de Données
## Développez une interface où l'utilisateur pourra saisir son poids (en kg),
 ## sa taille (en cm) et d'autres informations telles que le pseudo, nom, prénom, adresse, etc

pseudo_utilisateur = str(input("Entrez votre pseudo: "))
prenom_utilisateur = str(input("Quel est votre prénom ? "))
nom_utilisateur = str(input("Quel est votre nom de famille? "))
mail_utilisateur = str(input("Quelle est votre adresse mail? "))
adresse_utilisateur = str(input("Quelle est votre adresse postale? "))

#calcul de l'IMC avec la création d'une fonction calcul_imc

def calcul_imc(masse, taille):
    return masse/(taille**2)
poids_utilisateur = float(input("Poids en kg (exemple : 70 pour 70kg) : "))
taille_utilisateur = float(input("Taille en m (exemple: 1.70 pour 1 mètre 70) : "))
imc = calcul_imc(poids_utilisateur, taille_utilisateur)

if imc < 18:
	print("Vous avez un IMC de {}, vous êtes en sous-poids.".format(imc))
elif 18 < imc < 25:
	print("Vous avez un IMC de {}, vous avez une corpulence normale.".format(imc))
elif 25 < imc < 30:
	print("Vous avez un IMC de {}, vous êtes en surpoids.".format(imc))
elif imc > 30:
	print("Vous avez un IMC de {}, vous êtes en situation d'obésité.".format(imc))


## Initialisation du schéma de la base de données 

import sqlite3
from datetime import datetime
now = datetime.now()
date_actuelle = now.strftime('%Y-%m-%d %H:%M:%S')
con = sqlite3.connect("imc.db")
cur = con.cursor()
cur.execute('''
    CREATE TABLE users_imc (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE,
        address TEXT,
		date_created DATETIME
    )
''')
#res = cur.execute("SELECT name FROM sqlite_master") 
#res.fetchone()
insert_query = "INSERT INTO users_imc (username, first_name, last_name, email, address, date_created) VALUES (?, ?, ?, ?, ?, ?)"
user_data = (pseudo_utilisateur, prenom_utilisateur, nom_utilisateur, mail_utilisateur, adresse_utilisateur, date_actuelle )

cur.execute(insert_query, user_data)

con.commit()
con.close()
#res = cur.execute("SELECT username FROM user")
# res.fetchall() pour voir si les valeurs ont bien été intégrées



	


