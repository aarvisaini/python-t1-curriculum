def make_greeting():
    greeting = "Hello world!"
    return greeting

def build_face():
    message = make_greeting()
    return message

#print(build_face())

def personalized_greeting(name):
    new_message = "Hello " + name
    return new_message

print(personalized_greeting("Bob"))

def favorite_fruit():
    fav_fruit = "mangoes"
    print(fav_fruit)
    favorite_fruit()