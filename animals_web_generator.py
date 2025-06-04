import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_cards(animals_data):
    """Generates HTML cards for each animal"""
    cards_html = ""

    for animal in animals_data:
        # Check if all required fields exist
        has_name = 'name' in animal
        has_diet = 'characteristics' in animal and 'diet' in animal['characteristics']
        has_locations = 'locations' in animal and len(animal['locations']) > 0
        has_type = 'characteristics' in animal and 'type' in animal['characteristics']

        # Skip if any field is missing
        if not (has_name and has_diet and has_locations and has_type):
            continue

        # Create HTML card for each animal
        card = f"""
        <li class="cards__item">
            <div class="card__content">
                <h2 class="card__title">{animal['name']}</h2>
                <div class="card__text">
                    <p><strong>Type:</strong> {animal['characteristics']['type']}</p>
                    <p><strong>Diet:</strong> {animal['characteristics']['diet']}</p>
                    <p><strong>Locations:</strong> {', '.join(animal['locations'])}</p>
        """

        # Add additional characteristics if available
        if 'lifespan' in animal['characteristics']:
            card += f'<p><strong>Lifespan:</strong> {animal["characteristics"]["lifespan"]}</p>'
        if 'habitat' in animal['characteristics']:
            card += f'<p><strong>Habitat:</strong> {animal["characteristics"]["habitat"]}</p>'

        card += """
                </div>
            </div>
        </li>
        """
        cards_html += card

    return cards_html


def main():
    # Load the data
    animals_data = load_data('animals_data.json')

    # Generate HTML cards
    animals_html = generate_animal_cards(animals_data)

    # Load template
    with open('animals_template.html', 'r') as template_file:
        template = template_file.read()

    # Replace placeholder with generated HTML
    output_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    # Write to new file
    with open('animals.html', 'w') as output_file:
        output_file.write(output_html)

    print("HTML file generated successfully: animals.html")


if __name__ == "__main__":
    main()