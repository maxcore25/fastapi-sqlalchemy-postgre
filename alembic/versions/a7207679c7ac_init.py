"""init

Revision ID: a7207679c7ac
Revises: 
Create Date: 2022-02-07 12:06:38.123798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7207679c7ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('jobs')
