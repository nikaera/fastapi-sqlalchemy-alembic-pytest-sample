import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, DateTime
from sqlalchemy_utils import UUIDType

from .crud import Crud
from .model_base import ModelBase


class Group(ModelBase, Crud):
    __tablename__ = 'groups'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=current_timestamp())

    items = relationship("GroupItem", back_populates="group")
