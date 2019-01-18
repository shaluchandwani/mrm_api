"""decouple device and resource entity

Revision ID: c8a866f85fd7
Revises: 87582873ea02
Create Date: 2019-01-24 13:21:00.368195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8a866f85fd7'
down_revision = '87582873ea02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('room_id', sa.Integer(), nullable=True))
    op.drop_constraint('devices_resource_id_fkey', 'devices', type_='foreignkey')
    op.create_foreign_key(None, 'devices', 'rooms', ['room_id'], ['id'])
    op.drop_column('devices', 'resource_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('resource_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'devices', type_='foreignkey')
    op.create_foreign_key('devices_resource_id_fkey', 'devices', 'resources', ['resource_id'], ['id'])
    op.drop_column('devices', 'room_id')
    # ### end Alembic commands ###
