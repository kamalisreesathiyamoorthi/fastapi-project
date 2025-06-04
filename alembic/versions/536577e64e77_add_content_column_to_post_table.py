"""add content column to post table

Revision ID: 536577e64e77
Revises: 298223dcc789
Create Date: 2025-06-04 20:16:42.842624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '536577e64e77'
down_revision: Union[str, None] = '298223dcc789'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
