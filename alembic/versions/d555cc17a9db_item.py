"""item

Revision ID: d555cc17a9db
Revises: 
Create Date: 2023-01-04 18:13:09.453963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd555cc17a9db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(200)),
        sa.Column('password', sa.String(200), nullable=False),
    )


def downgrade():
    op.drop_table('account')