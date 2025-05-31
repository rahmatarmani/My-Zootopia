import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load the data
animals_data = load_data('animals_data.json')

# Iterate through each animal
for animal in animals_data:
    # Check if all required fields exist
    has_name = 'name' in animal
    has_diet = 'characteristics' in animal and 'diet' in animal['characteristics']
    has_locations = 'locations' in animal and len(animal['locations']) > 0
    has_type = 'characteristics' in animal and 'type' in animal['characteristics']

    # Skip if any field is missing
    if not (has_name and has_diet and has_locations and has_type):
        continue

    # Print all fields (since we confirmed they exist)
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print(f"Location: {animal['locations'][0]}")
    print(f"Type: {animal['characteristics']['type']}")
    print()  # Blank line between animals