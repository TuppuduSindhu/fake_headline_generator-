#import random module 


import random
#create subjects 
subjects=[
    "prabhas",
    "virat kohli",
    "Amumbai cat",
    "A group of monkeys",
    "Auto driver from delhi",
    "monalisa"
]
actions=[
    "eats",
    "dances",
    "meets",
    "celebrates",
    "orders",
    "declares war on"
]
places_or_things=[
    "At indian gate",
    "at hyderabad metro",
    "at railway station",
    "during ipl match",
    "at mahakumbh",
    "at kashi"
]
#start the headline generation tool 
while True:
    subject=random.choice(subjects) 
    action=random.choice(actions) 
    place_or_thing=random.choice(places_or_things)
    headline=f" Breaking News:{subject} {action} {place_or_thing}"
    print("/n"+headline)
    #strip() is used to remove extra spaces 
    user_input=input("Do you want  another headline ? (yes/no)").strip()
    if user_input=="no":
        break
#print goodbye messsage 
print("\n thanks for using the fake news Generator .Have a fun")

