"""add users table

Revision ID: c28294379b94
Revises: 48161d0bf479
Create Date: 2022-10-25 19:26:11.789552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c28294379b94'
down_revision = '48161d0bf479'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    				sa.Column('id',sa.Integer(),nullable=False),
    				sa.Column('email',sa.String(),nullable=False),
    				sa.Column('password',sa.String(),nullable=False),
    				sa.Column('created_at',sa.TIMESTAMP(timezone=True),
    						server_default=sa.text('now()'),nullable=False),
    				sa.PrimaryKeyConstraint('id'), # add constrain primary key
    				sa.UniqueConstraint('email')
    				)

def downgrade():
    os.drop_table('users')
