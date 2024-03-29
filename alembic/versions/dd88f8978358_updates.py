"""updates

Revision ID: dd88f8978358
Revises: c6e95f0c9a06
Create Date: 2024-03-10 11:37:12.727009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd88f8978358'
down_revision: Union[str, None] = 'c6e95f0c9a06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('credit_hours', sa.Integer(), nullable=True))
    op.add_column('programs', sa.Column('duration_in_years', sa.Integer(), nullable=True))
    op.drop_column('programs', 'credit_hours')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('programs', sa.Column('credit_hours', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('programs', 'duration_in_years')
    op.drop_column('courses', 'credit_hours')
    # ### end Alembic commands ###
