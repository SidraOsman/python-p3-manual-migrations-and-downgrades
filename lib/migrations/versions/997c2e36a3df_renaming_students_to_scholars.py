"""Renaming students to scholars

Revision ID: 997c2e36a3df
Revises: 791279dd0760
Create Date: 2023-12-19 19:02:32.517354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '997c2e36a3df'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
