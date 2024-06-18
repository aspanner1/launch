def create_user(username, *, email, age):
    return {username=, }

print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception