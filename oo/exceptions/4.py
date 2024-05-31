students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        age = students[name]
    except KeyError:
        return "Student not found"
    
print(get_age("John"))
print(get_age("Joe Smocosedfso"))

