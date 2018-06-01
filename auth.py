from user import User

users = {
    User(1, 'admin', '123456'),
    User(2, 'charles', '1234'),
    User(3, 'bes', '1234'),
    User(4, 'ivan', '1234'),
    User(5, 'mary', '1234'),
    User(6, 'ruganda', '1234'),
    User(7, 'johnz', '1234')
}

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
