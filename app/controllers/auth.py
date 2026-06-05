from app.models.user_model import (
    create_user,
    authenticate
)


def register_user(nome, email, senha):
    return create_user(nome, email, senha)


def login_user(email, senha):
    return authenticate(email, senha)