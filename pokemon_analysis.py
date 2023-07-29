import zipfile
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Pokemon Analysis") \
    .getOrCreate()

# unzip pokemon.zip file
with zipfile.ZipFile('pokemon.zip', 'r') as zip_ref:
    zip_ref.extractall('')

# Create a result variable to add the text to it
# We will store the result into a file at the end of all computation

result = ''

# Load the Pokemon dataset into a DataFrame
pokemon_df = spark.read.csv("Pokemon.csv", header=True, inferSchema=True)

# Question 1 - Top 5 strongest non-legendary Pokemon
top_strongest_non_legendary = pokemon_df \
    .filter(col("Legendary") == False) \
    .orderBy(col("Total").desc()) \
    .select(col("Name")) \
    .limit(5)

result += "Top 5 strongest non-legendary Pokemon:"
result += '\n'+', '.join([name["Name"] for name in top_strongest_non_legendary.collect()])+'\n'

# Question 2 - Pokemon type with the highest average HP
highest_avg_hp_type1 = pokemon_df \
    .groupBy("Type 1") \
    .avg("HP") \
    .orderBy(col("avg(HP)").desc()) \
    .first()

highest_avg_hp_type2 = pokemon_df \
    .groupBy("Type 2") \
    .avg("HP") \
    .orderBy(col("avg(HP)").desc()) \
    .first()

best_type = highest_avg_hp_type1["Type 1"] \
        if highest_avg_hp_type1["avg(HP)"] >= highest_avg_hp_type2["avg(HP)"] \
        else highest_avg_hp_type2["Type 2"]

result += "\nPokemon type with the highest average HP:"
result += f'\n{best_type}\n'

# Question 3 - Most common special Attack
most_common_special_attack = pokemon_df \
    .groupBy("`Sp. Atk`") \
    .count() \
    .orderBy(col("count").desc()) \
    .first()["Sp. Atk"]

result += "\nMost common special Attack:\n"
result += str(most_common_special_attack)

# write the results in "results.txt" file

with open('result.txt', 'w') as f:
    f.write(result)

# Stop the SparkSession
spark.stop()