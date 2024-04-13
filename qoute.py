import random

quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
    "Dream bigger. Do bigger. - Unknown",
    "It does not matter how slowly you go as long as you do not stop. - Confucius"
]

def generate_quote():
    return random.choice(quotes)

print(generate_quote())