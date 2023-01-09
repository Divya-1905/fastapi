"""profile

Revision ID: 46392d2f848d
Revises: 3e9df631117c
Create Date: 2023-01-09 11:01:05.537154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46392d2f848d'
down_revision = '3e9df631117c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'profile',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
    )


def downgrade() -> None:
    pass
