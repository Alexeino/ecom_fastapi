"""empty message

Revision ID: 9860f7f8f635
Revises: ab2b1cf1b201
Create Date: 2023-11-10 19:04:05.759737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9860f7f8f635'
down_revision: Union[str, None] = 'ab2b1cf1b201'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'is_active')
    # ### end Alembic commands ###
