"""Another Test

Revision ID: bce6a987a9ae
Revises: 000af4e83e48
Create Date: 2024-02-21 02:11:35.855240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bce6a987a9ae'
down_revision: Union[str, None] = '000af4e83e48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
