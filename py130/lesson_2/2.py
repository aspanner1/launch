def describe_pet(animal_type, /, *, name= " "):
    print(f"The animal is a {animal_type} and its name is {name}.")
    
describe_pet("Hamster", name="Harry")