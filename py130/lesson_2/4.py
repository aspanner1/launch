def find_person(**names):
    if "Antonina" in names:
        print(f"Antonina's profession is {names["Antonina"]}")
    else:
        print(f"Antonina not found")
        
find_person(John="Engineer", Antonina="Software Engineer")
# Antonina's profession is Software Engineer

find_person(John="Engineer", Ginni="Software Engineer")