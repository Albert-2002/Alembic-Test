"""Added Roll No.

Revision ID: 07beeaa38e47
Revises: 0f4f0b01732d
Create Date: 2025-03-10 11:59:21.383135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07beeaa38e47'
down_revision: Union[str, None] = '0f4f0b01732d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('roll_no', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'roll_no')
    # ### end Alembic commands ###
