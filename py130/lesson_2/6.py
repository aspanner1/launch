def register(username, /, age=None, *, password):
    return(username, age, password)
    
print(register('user1', password='pass123', age=30))
# {'username': 'user1', 'password': 'pass123', 'age': 30}

print(register('user2', password='pass132', age=45))
# {'username': 'user2', 'password': 'pass132', 'age': 45}

print(register('user3', password='pass321'))
# {'username': 'user3', 'password': 'pass321', 'age': None}