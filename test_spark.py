"""Pour résoudre ce problème avec PySpark,
 vous devez d'abord télécharger le fichier CSV depuis l'URL et
 le charger dans un DataFrame PySpark. Ensuite, vous pouvez effectuer les opérations
 de filtrage et de calcul d'âge moyen par attribut "native-country".
 Voici comment vous pouvez le faire :"""
 
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Initialisez SparkSession
spark = SparkSession.builder.appName("PySparkExample").getOrCreate()

# Téléchargez le fichier CSV depuis l'URL
url = "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/adult_data.csv"
df = spark.read.csv(url, header=True, inferSchema=True)

# Filtrer les personnes ayant "Private" comme attribut workclass
private_workers = df.filter(df["workclass"] == "Private")

# Calculer l'âge moyen par attribut "native-country"
average_age_by_country = private_workers.groupBy("native-country").agg(avg("age").alias("average_age"))

# Afficher le résultat
average_age_by_country.show()

# Arrêtez SparkSession
spark.stop()


"""
Ce code effectue les étapes suivantes :

    Initialise une session Spark.
    Télécharge le fichier CSV depuis l'URL et le charge dans un DataFrame PySpark.
    Filtre le DataFrame pour sélectionner uniquement les personnes ayant "Private" comme attribut workclass.
    Regroupe les données par attribut "native-country" et calcule l'âge moyen pour chaque groupe.
    Affiche le résultat avec les attributs "native-country" et leur âge moyen correspondant.

Assurez-vous d'avoir installé PySpark et que votre environnement est configuré correctement pour exécuter ce code.
"""