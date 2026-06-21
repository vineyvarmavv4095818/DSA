# FAKE NEWS HEADLINE GENERATOR
import random

Subjects = [
    "Prime minister",
    "Virat kohli",
    "Akshay kumar",
    "A group of animals",
    "Optimus prime",
    "Megatron",
]

Actions = [
    "celebrates IPl",
    "hit the balloon",
    "kill a man",
    "watching TV",
    "playing cricket",
    "dancing",
]

Places = [
    "at cricket ground",
    "in the air",
    "in a house",
    "on the road",
    "on the rooftop",
    "at the red fort",
]

while True:
    subject = random.choice(Subjects)
    action = random.choice(Actions)
    place = random.choice(Places)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want to print another headline?(yes/no): ").strip().lower()  #strip for removes unwanted spaces and lower used for only lower case yes or no
    if (user_input == "no"):
        break

print("\nThank you for using fake news headline generator....")    




