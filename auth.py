from user import User

users = {
    User(1, 'admin', '123456')
}

username_mapping = {u.username: u for u in users}
print(username_mapping)

userid_mapping = {u.id: u for u in users}
print(userid_mapping)


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
