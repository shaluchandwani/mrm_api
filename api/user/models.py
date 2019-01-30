from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType
from utilities.validations import validate_empty_fields
from api.user_role.models import UsersRole  # noqa: F401
from api.notification.models import Notification  # noqa: F401


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    email = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=True)
    name = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    roles = relationship('Role', secondary='users_roles')
    state = Column(Enum(StateType), default="active")
    notification_settings = relationship(
        'Notification', cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.email = kwargs['email']
        self.name = kwargs['name']
        self.picture = kwargs['picture']
