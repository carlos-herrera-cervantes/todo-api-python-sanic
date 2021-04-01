from mongoengine import *
from mongoengine import signals
from datetime import datetime
from bcrypt import hashpw, gensalt

from models.role import Role


class User(Document):
    email = EmailField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    password = StringField(required=True, min_length=8)
    role = StringField(required=False, default=Role.CLIENT.value)
    todos = ListField(required=False)
    created_at = DateTimeField(required=False, default=datetime.now())
    updated_at = DateTimeField(required=False, default=datetime.now())

    @classmethod
    def pre_save(cls: any, sender: any, document: Document, **kwargs: dict) -> None:
        """
        Executes before save the user
        """
        document.updated_at = datetime.now()

    @classmethod
    def post_save(cls: any, sender: any, document: Document, **kwargs: dict) -> None:
        """
        Executes after save the user
        """
        is_new = kwargs.get('created')
        
        if not is_new:
            return

        password = document.password.encode('utf-8')
        hashed_password = hashpw(password, gensalt())
        document.password = hashed_password.decode('utf-8')
        document.save()


signals.pre_save.connect(User.pre_save, sender=User)
signals.post_save.connect(User.post_save, sender=User)
