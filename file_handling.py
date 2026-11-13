import csv
import json

# --- 1. Plain Text File ---
txt_filename = "names.txt"
names_list = ["Moin", "Alice", "Bob", "Charlie"]

# Write one name per line
with open(txt_filename, "w") as txt_file:
    for name in names_list:
        txt_file.write(f"{name}\n")

# Read one name per line
print("--- Text File Output ---")
with open(txt_filename, "r") as txt_file:
    for line in txt_file:
        print(line.strip())

# --- 2. CSV File ---
csv_filename = "users.csv"
csv_data = [
    {"name": "Moin", "role": "AI Engineer"},
    {"name": "Alice", "role": "Data Scientist"},
    {"name": "Bob", "role": "Developer"}
]
fieldnames = ["name", "role"]

# Write with csv.DictWriter
with open(csv_filename, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(csv_data)

# Read with csv.DictReader
print("\n--- CSV File Output ---")
with open(csv_filename, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(f"Name: {row['name']}, Role: {row['role']}")

# --- 3. JSON File ---
json_filename = "data.json"
json_data = {
    "project": "File Handling Assignment",
    "languages": ["Python", "JavaScript"],
    "completed": True
}

# Write with json.dump
with open(json_filename, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

# Read with json.load
print("\n--- JSON File Output ---")
with open(json_filename, "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
