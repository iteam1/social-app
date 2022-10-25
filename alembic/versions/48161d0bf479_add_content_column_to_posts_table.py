"""add content column to posts table

Revision ID: 48161d0bf479
Revises: ed65ab4a6a8c
Create Date: 2022-10-25 19:08:35.525518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48161d0bf479'
down_revision = 'ed65ab4a6a8c'
branch_labels = None
depends_on = None

def upgrade():
	op.add_column('posts',sa.Column('content',sa.String(),nullable=False))

def downgrade():
	op.drop_column('posts','content')
