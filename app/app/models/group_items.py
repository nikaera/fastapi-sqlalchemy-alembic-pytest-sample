import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from sqlalchemy_utils import UUIDType

from .crud import Crud
from .model_base import ModelBase


class GroupItem(ModelBase, Crud):
    __tablename__ = 'group_items'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, nullable=False)
    group_id = Column(UUIDType(binary=False), ForeignKey("groups.id"))
    item_id = Column(UUIDType(binary=False), ForeignKey("items.id"))

    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=current_timestamp())

    item = relationship("Item", back_populates="groups")
    group = relationship("Group", back_populates="items")
