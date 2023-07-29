# Annalect

This repository contains a Dockerized standalone single-node Spark cluster designed to analyze the Pokemon dataset from Kaggle.

## How to Run
1. Clone this repository to your local machine.
2. Navigate to the cloned repository's directory.
3. Run the exec.sh script.

```./exec.sh```

After the script runs successfully, you will find the result.txt file in the current directory.

## Dataset
The Pokemon dataset used for analysis can be found on Kaggle. Please refer to the [Pokemon Dataset](https://www.kaggle.com/datasets/abcsds/pokemon) on Kaggle for more details.


## Analysis
The Spark cluster will perform analysis tasks on the Pokemon dataset to answer the following questions:

1. What are the top 5 strongest non-legendary monsters?
2. Which Pokemon type has the highest average HP?
3. Which is the most common special attack?

The results of the analysis will be saved to the result.txt file in the current directory.



