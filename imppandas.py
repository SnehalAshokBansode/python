import pandas as pd

# Define the dataset
fruit_dataset = {
    'fruits': ["Apple", "Banana", "Cherry"],
    'quantities': [5, 10, 15]
}

# Create a DataFrame
fruit_df = pd.DataFrame(fruit_dataset)

# Print the DataFrame
print(fruit_df)
