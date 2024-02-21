"""Expired and Category Update

Revision ID: 5d4b8eac1312
Revises: bce6a987a9ae
Create Date: 2024-02-21 14:11:06.983231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d4b8eac1312'
down_revision: Union[str, None] = 'bce6a987a9ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
