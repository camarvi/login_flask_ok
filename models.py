from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def buscar_usuario(name, password):
        # buscar en la base de datos el usuario
        return User(1,name,password)

    @staticmethod
    def get_by_id(id):
        return User(1,'carlos','123')

    