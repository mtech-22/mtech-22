import random

quotes = {
    "motivation": [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        # Add more motivational quotes here
    ],
    "inspiration": [
        "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
        "Dream bigger. Do bigger. - Unknown",
        # Add more inspirational quotes here
    ],
    # Add more categories here
}

def generate_quote(category):
    if category not in quotes:
        return "Quote category not found."
    return random.choice(quotes[category])

category = input("Enter a quote category: ")
print(generate_quote(category))