from app.models.json_helper import read_json, write_json

DATABASE = "app/controllers/database/users.json"


def get_users():
    return read_json(DATABASE)


def find_user_by_email(email):
    users = get_users()

    for user in users:
        if user["email"] == email:
            return user

    return None


def create_user(nome, email, senha):

    users = get_users()

    if find_user_by_email(email):
        return False

    new_user = {
        "id": len(users) + 1,
        "nome": nome,
        "email": email,
        "senha": senha
    }

    users.append(new_user)

    write_json(DATABASE, users)

    return True


def authenticate(email, senha):

    users = get_users()

    for user in users:

        if (
            user["email"] == email and
            user["senha"] == senha
        ):
            return user

    return None