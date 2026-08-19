import random

subjects = {
    "Science": [
        "Scientists",
        "Researchers",
        "A team of engineers",
        "Medical experts",
        "Space researchers"
    ],

    "Technology": [
        "A tech company",
        "Software developers",
        "A group of programmers",
        "Cybersecurity researchers",
        "An unknown inventor"
    ],

    "Politics": [
        "The government",
        "The mayor",
        "Local officials",
        "A government committee",
        "Political researchers"
    ],

    "Entertainment": [
        "A famous celebrity",
        "A movie director",
        "A popular singer",
        "A group of actors",
        "A television company"
    ]
}

actions = [
    "discovered",
    "announced",
    "revealed",
    "launched",
    "built",
    "opened",
    "closed",
    "investigated",
    "uncovered",
    "reported"
]

places_or_things = [
    "an abandoned laboratory",
    "a secret underground tunnel",
    "a mysterious machine",
    "a giant robot",
    "an ancient statue",
    "a hidden cave",
    "a new smartphone",
    "a remote island",
    "a strange-looking device",
    "an experimental vehicle"
]

locations = [
    "Mumbai",
    "Pune",
    "Delhi",
    "London",
    "New York",
    "Tokyo",
    "Paris",
    "Sydney",
    "a remote village",
    "an undisclosed location"
]

breaking_words = [
    "BREAKING NEWS",
    "DEVELOPING STORY",
    "JUST IN",
    "EXCLUSIVE",
    "LATEST REPORT"
]

templates = [
    "{subject} {action} {thing} in {location}.",
    "{subject} have reportedly {action} {thing} near {location}.",
    "{breaking}: {subject} {action} {thing} in {location}.",
    "Shocking discovery: {subject} {action} {thing} near {location}.",
    "Officials say {subject} {action} {thing} in {location}."
]


def generate_news(category):

    subject = random.choice(subjects[category])
    action = random.choice(actions)
    thing = random.choice(places_or_things)
    location = random.choice(locations)
    breaking = random.choice(breaking_words)

    template = random.choice(templates)

    headline = template.format(
        subject=subject,
        action=action,
        thing=thing,
        location=location,
        breaking=breaking
    )

    return headline


print("=" * 50)
print("       FICTIONAL NEWS GENERATOR")
print("=" * 50)
print("All generated stories are fictional.\n")

while True:

    print("\nChoose a category:")
    print("1. Science")
    print("2. Technology")
    print("3. Politics")
    print("4. Entertainment")
    print("5. Random")

    choice = input("\nEnter your choice: ").strip()

    categories = {
        "1": "Science",
        "2": "Technology",
        "3": "Politics",
        "4": "Entertainment"
    }

    if choice == "5":
        category = random.choice(list(subjects.keys()))

    elif choice in categories:
        category = categories[choice]

    else:
        print("Invalid choice!")
        continue

    news = generate_news(category)

    print("\n" + "-" * 50)
    print("FICTIONAL STORY")
    print("-" * 50)
    print(news)
    print("-" * 50)

    again = input("\nGenerate another story? (yes/no): ").strip().lower()

    if again != "yes":
        break

print("\nThank you for using the Fictional News Generator!")