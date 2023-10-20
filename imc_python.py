## Projet : Application de Calcul de l'IMC avec Sauvegarde en Base de Données


import sqlite3
con = sqlite3.connect("imc.db")
cur = con.cursor()
#cur.execute("CREATE TABLE user(user_id, username, first_name, last_name, email, adress, date_created)")
#res = cur.execute("SELECT name FROM sqlite_master") 
#res.fetchone()
cur.execute("""
    INSERT INTO user VALUES
        (1, "Melobgn", "Melody", "Bugnon", "melodybugnon@gmail.com", "1 Cour Paternotte", 2023-10-20 )
""")
con.commit()
res = cur.execute("SELECT username FROM user")
res.fetchall()

## Développez une interface où l'utilisateur pourra saisir son poids (en kg),
 ## sa taille (en cm) et d'autres informations telles que le pseudo, nom, prénom, adresse, etc

pseudo_utilisateur = str(input("Entrez votre pseudo: "))
prenom_utilisateur = str(input("Quel est votre prénom ? "))
nom_utilisateur = str(input("Quel est votre nom de famille? "))
adresse_utilisateur = str(input("Quelle est votre adresse? "))

def calcul_imc(masse, taille):
    return masse/(taille**2)
poids_utilisateur = float(input("Poids en kg (exemple : 70 pour 70kg) : "))
taille_utilisateur = float(input("Taille en m (exemple: 1.70 pour 1 mètre 70) : "))
imc = calcul_imc(poids_utilisateur, taille_utilisateur)

if imc < 18:
	print("Vous êtes en sous-poids.")
elif 18 < imc < 25:
	print("Vous avez une corpulence normale.")
elif 25 < imc < 30:
	print("Vous êtes en surpoids.")
elif imc > 30:
	print("Vous êtes en situation d'obésité.")

	


