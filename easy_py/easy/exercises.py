def ends_with_exclamation(string):
    return string.endswith("!")

famous_words = "seven years ago..."

munsters_description = "the Munsters are CREEPY and Spooky."

print(munsters_description.lower().capitalize())

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

if str2.find("Dino") == 0 or str2.find("Dino"):
    print("Dino is here")

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])

print(flintstones)

advice = "Few things in life are as important as house training your pet dinosaur."
short_advice = advice[:advice.find("house")]
print(short_advice)
