import sqlite3
import os
import pandas as pd
import uuid



def create_database():
    # Nom de la base de données
    database_file = "ma_base_de_donnees.db"
    # Vérification de l'existence de la base de données
    if not os.path.exists(database_file):
        # Connexion à la base de données SQLite
        conn = sqlite3.connect(database_file)

        # Création d'un curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()

        # Création de la table "utilisateurs"
        cursor.execute("""
        CREATE TABLE utilisateurs (
            id  TEXT ,
            nom TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)

        # Sauvegarde des modifications
        conn.commit()

    conn = sqlite3.connect(database_file)
    return conn



def get_users():
    conn = create_database()
    df = pd.read_sql_query("SELECT * FROM utilisateurs", conn)
    print(df)
    return df


def add_user( nom, password):
    conn = create_database()
    unique_id = str(uuid.uuid4())
    df = pd.read_sql_query("SELECT * FROM utilisateurs", conn)
    unique_id = str(uuid.uuid4())
    df = df.append({"id":unique_id,"nom": nom, "password":password}, ignore_index=True)
    df.to_sql("utilisateurs", conn, if_exists="append", index=False)
    print(df)

# # Lecture des données de la base de données dans un DataFrame
# df = pd.read_sql_query("SELECT * FROM utilisateurs", conn)
# unique_id = str(uuid.uuid4())
# df = df.append({"id":unique_id,"nom": "dddd", "password": "Jacqudddddes"}, ignore_index=True)
# print(df)
# # Écriture du DataFrame modifié dans la base de données
# df.to_sql("utilisateurs", conn, if_exists="append", index=False)

# # Lecture des données de la base de données dans un DataFrame
# df = pd.read_sql_query("SELECT * FROM  utilisateurs", conn)

# # Affichage du DataFrame
# print(df)