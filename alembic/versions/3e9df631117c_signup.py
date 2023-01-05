"""signup

Revision ID: 3e9df631117c
Revises: d555cc17a9db
Create Date: 2023-01-05 11:14:53.481712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e9df631117c'
down_revision = 'd555cc17a9db'
branch_labels = None
depends_on = None


def upgrade() -> None:
  op.create_table(
      'users',
      sa.Column('id', sa.Integer(), nullable=False),
      sa.Column('email', sa.String(length=255), nullable=False),
  )

def downgrade() -> None:
    pass
