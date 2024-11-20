import pandas as pd

# Load the CSV file
df = pd.read_csv('./data/chemical_name_for_open_alex.csv')  # Replace with your actual file path

# Extract the chemical names into a list
chemical_names = df['structure_nameTraditional'].tolist()

# Set the chunk size
chunk_size = 10000

# Create text files
for i in range(0, len(chemical_names), chunk_size):
    chunk = chemical_names[i:i + chunk_size]
    file_name = f'chemical_list_{i // chunk_size + 1}.txt'
    with open(file_name, 'w') as f:
        for name in chunk:
            f.write(f"{name}\n")

print("Text files created successfully!")
