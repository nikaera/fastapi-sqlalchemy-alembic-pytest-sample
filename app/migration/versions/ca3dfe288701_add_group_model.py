"""Add Group model

Revision ID: ca3dfe288701
Revises: 8a20f21a30c3
Create Date: 2021-06-25 15:33:59.509499

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType


# revision identifiers, used by Alembic.
revision = 'ca3dfe288701'
down_revision = '8a20f21a30c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', UUIDType(binary=False), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups')
    # ### end Alembic commands ###
