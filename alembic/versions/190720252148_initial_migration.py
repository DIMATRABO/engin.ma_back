"""initial migration

Revision ID: 190720252148
Revises: 
Create Date: 2025-07-19 21:48:00

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '190720252148'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    '''Create the users table with the specified columns and constraints.'''
    op.create_table(
        'users',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('birthdate', sa.DateTime(), nullable=True),
        sa.Column('address', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(), nullable=True),
        sa.Column('user_status', sa.String(), nullable=True),
        sa.Column('email_verified_at', sa.String(), nullable=True),
        sa.Column('reset_password_otp', sa.String(), nullable=True),
        sa.Column('otp_expiration_date', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )

    op.create_table(
        'user_roles',
        sa.Column('user_id', sa.String(), sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('role', sa.String(), primary_key=True)
    )

    op.create_table(
        'cities',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False)
    )

    op.create_table(
        'equipment_brands',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False)
    )

    op.create_table(
        'equipment_models',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False)
    )

    op.create_table(
        'equipment',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('owner_id', sa.String(), sa.ForeignKey('users.id', ondelete='SET NULL')),
        sa.Column('pilot_id', sa.String(), sa.ForeignKey('users.id', ondelete='SET NULL')),
        sa.Column('brand_id', sa.String(), sa.ForeignKey('equipment_brands.id')),
        sa.Column('model_id', sa.String(), sa.ForeignKey('equipment_models.id')),
        sa.Column('model_year', sa.Integer),
        sa.Column('construction_year', sa.Integer),
        sa.Column('date_of_customs_clearance', sa.Integer),
        sa.Column('city_id', sa.String(), sa.ForeignKey('cities.id')),
        sa.Column('title', sa.String(255)),
        sa.Column('description', sa.Text),
        sa.Column('price_per_day', sa.Numeric),
        sa.Column('is_available', sa.Boolean, default=True),
        sa.Column('rating_average', sa.Float, default=0.0),
        sa.Column('fields_of_activity', sa.Text),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.now())
    )

    op.create_table(
        'equipment_images',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('equipment_id', sa.String(), sa.ForeignKey('equipment.id', ondelete='CASCADE')),
        sa.Column('url', sa.String(500), nullable=False)
    )

    op.create_table(
        'pilot_profiles',
        sa.Column('user_id', sa.String(), sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('experience_years', sa.Integer),
        sa.Column('rating_average', sa.Float, default=0.0),
        sa.Column('fields_of_experience', sa.Text)
    )

    op.create_table(
        'bookings',
        sa.Column('id', sa.String(), primary_key=True, default=uuid.uuid4),
        sa.Column('client_id', sa.String(), sa.ForeignKey('users.id')),
        sa.Column('equipment_id', sa.String(), sa.ForeignKey('equipment.id')),
        sa.Column('pilot_id', sa.String(), sa.ForeignKey('users.id')),
        sa.Column('start_date', sa.Date),
        sa.Column('end_date', sa.Date),
        sa.Column('status', sa.String(50)),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.now())
    )

    op.create_table(
        'reviews',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('client_id', sa.String(), sa.ForeignKey('users.id')),
        sa.Column('equipment_id', sa.String(), sa.ForeignKey('equipment.id')),
        sa.Column('pilot_id', sa.String(), sa.ForeignKey('users.id')),
        sa.Column('rating', sa.Integer),
        sa.Column('comment', sa.Text),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.now())
    )


def downgrade():
    op.drop_table('reviews')
    op.drop_table('bookings')
    op.drop_table('pilot_profiles')
    op.drop_table('equipment_images')
    op.drop_table('equipment')
    op.drop_table('equipment_brands')
    op.drop_table('equipment_models')
    op.drop_table('cities')
    op.drop_table('user_roles')
    op.drop_table('users')
