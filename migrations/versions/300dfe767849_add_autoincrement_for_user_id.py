"""ADD: Autoincrement for user.id

Revision ID: 300dfe767849
Revises: 5dc4d86c7312
Create Date: 2023-11-20 07:57:58.562027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '300dfe767849'
down_revision: Union[str, None] = '5dc4d86c7312'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
