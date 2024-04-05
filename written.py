messed_pokemon = 'BulbAsaur-ChaRMAndeR-pikaCHU-chariZard-SQuirtlE'

all_pokemon = messed_pokemon.replace("-", " ").title().split()
pokedex = all_pokemon.remove('Charizard')
print(all_pokemon)

#print(pokedex) # ['Bulbasaur', 'Charmander', 'Pikachu', 'Squirtle']

secret_number = "77"
friends = {1: "Bill", 2: "Bob", 3: "Jake", 4: "Aaron"}

def play_round(item):
    key, name = item
    print(f"{name} wants the secret number")
    if name == "Bob":
        print("'Ok', says Joey. Here is the secret number:")
        print(f"{secret_number}")
    else:
        print("No way!")

for item in friends.items():
    play_round(item)