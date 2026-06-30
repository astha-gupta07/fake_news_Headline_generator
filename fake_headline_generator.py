#import the random module
import random

#create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala",
    "Mumbai cat",
    "a  group of Monkeys",
    "Prime minister Modi ji",
    "Auto Rikshaw driver from delhi",
]

# create actions
actions = [
    "launches",
    "cancels",
    "dances",
    "eats vegetable",
    "declares war",
    "order's food",
    "celebrates",
]

#create places
places_or_things= [
    "red fort",
    "in pakistan lahore",
    "in dhurandhar movie",
    "at samosa centre",
    "in rewa with raja ji",
    "in movie kunfu panda",
    "india gate",
]

#start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS:{subject},{action},{places_or_thing}"
    print(f"\n {headline}")

    user_input = input("Do you want another headline?(yes/no)").strip().lower() 
    if user_input == "no":
        break
#.strip help if a user is normally using extra space

#print("GOOD BYE")

print("\nThanks for using the Fake News Headline Generator .Have a GoodDay")
