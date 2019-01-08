"""migrations Message

Revision ID: 75d6072e335b
Revises: 6046c7c7c022
Create Date: 2018-12-14 07:47:58.034013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75d6072e335b'
down_revision = '6046c7c7c022'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('abbreviation', sa.String(), nullable=False),
    sa.Column('country', sa.Enum('Uganda', 'Kenya', 'Nigeria', name='countrytype'), nullable=True),
    sa.Column('time_zone', sa.Enum('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME', name='timezonetype'), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('device_health_notification', sa.Boolean(), nullable=True),
    sa.Column('meeting_update_notification', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('offices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('office_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['office_id'], ['offices.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('floors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['blocks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('floor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['floor_id'], ['floors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('room_type', sa.String(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('calendar_id', sa.String(), nullable=True),
    sa.Column('floor_id', sa.Integer(), nullable=True),
    sa.Column('wing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['floor_id'], ['floors.id'], ),
    sa.ForeignKeyConstraint(['wing_id'], ['wings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.String(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('event_title', sa.String(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=False),
    sa.Column('end_time', sa.String(), nullable=False),
    sa.Column('checked_in', sa.Boolean(), nullable=True),
    sa.Column('cancelled', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('creation_time', sa.String(), nullable=False),
    sa.Column('overall_rating', sa.String(), nullable=True),
    sa.Column('cleanliness_rating', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('device_type', sa.String(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.Column('last_seen', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'wings', ['name'])
    # ### end Alembic commands ###

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('devices')
    op.drop_table('resources')
    op.drop_table('feedback')
    op.drop_table('events')
    op.drop_table('rooms')
    op.drop_table('wings')
    op.drop_table('floors')
    op.drop_table('blocks')
    op.drop_table('users_roles')
    op.drop_table('offices')
    op.drop_table('notifications')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('locations')

    # ### end Alembic commands ###
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wings', type_='unique')
    # ### end Alembic commands ###