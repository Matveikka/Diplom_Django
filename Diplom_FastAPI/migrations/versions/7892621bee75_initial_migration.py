"""Initial migration

Revision ID: 7892621bee75
Revises: 21d289d5c1ed
Create Date: 2024-12-15 21:16:46.167996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7892621bee75'
down_revision: Union[str, None] = '21d289d5c1ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('rezume', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_index(op.f('ix_posts_slug'), 'posts', ['slug'], unique=True)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_index(op.f('ix_posts_slug'), table_name='posts')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
