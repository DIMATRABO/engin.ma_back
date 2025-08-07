"""populate roles and create admin

Revision ID: 230720252054
Revises: 190720252148
Create Date: 2025-07-23 20:54:00.000000
"""
from datetime import datetime
import uuid
import bcrypt
from alembic import op


# revision identifiers, used by Alembic.
revision = '230720252054'
down_revision = '190720252148'
branch_labels = None
depends_on = None


def upgrade():

    # Create admin user
    admin_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    password = bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    op.execute(f"""
        INSERT INTO users (
            id, username, password, full_name, email, birthdate, address,
            phone_number, user_status, email_verified_at,
            reset_password_otp, otp_expiration_date, created_at
        ) VALUES (
            '{admin_id}', 'Admin', '{password}', 'admin', 'admin@engin.ma',
            NULL, NULL, NULL, 'ACTIVE', '{now}',
            NULL, NULL, '{now}'
        )
    """)

    # Assign ADMIN role to admin user
    op.execute(f"""
        INSERT INTO user_roles (user_id, role)
        VALUES ('{admin_id}', 'ADMIN')
    """)


def downgrade():
    '''Remove admin user and roles.'''
    pass