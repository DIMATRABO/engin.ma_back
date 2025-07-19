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
    op.create_table('users',
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
def downgrade() -> None:
    '''Drop the users table.'''
    op.drop_table('users')