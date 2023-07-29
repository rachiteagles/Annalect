# Use the official Jupyter PySpark base image
FROM jupyter/pyspark-notebook:latest

# Set the working directory in the container
WORKDIR /home/jovyan/work

# Copy the files to the container
COPY . .

# Run the PySpark script and save the output to 'result.txt'
CMD ["spark-submit", "--master", "local[1]", "--name", "PokemonAnalysis", "pokemon_analysis.py"]
