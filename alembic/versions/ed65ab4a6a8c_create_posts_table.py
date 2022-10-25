"""create posts table

Revision ID: ed65ab4a6a8c
Revises: 
Create Date: 2022-10-25 18:57:06.674156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed65ab4a6a8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('posts',sa.Column('id',sa.Integer(),nullable = False, primary_key = True),sa.Column('title',sa.String(),nullable=False))


def downgrade():
	op.drop_table('posts')
