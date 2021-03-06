"""Add state column to Response table

Revision ID: 20dd40a4c970
Revises: 472c199d7d44
Create Date: 2019-07-18 07:55:11.675124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20dd40a4c970'
down_revision = '472c199d7d44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('responses', sa.Column('state', sa.Enum('active', 'archived', 'deleted', name='statetype'), nullable=False, server_default='active'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('responses', 'state')
    # ### end Alembic commands ###
