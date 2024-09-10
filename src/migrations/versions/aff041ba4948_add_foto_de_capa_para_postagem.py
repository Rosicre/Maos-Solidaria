"""Add foto de capa para postagem

Revision ID: aff041ba4948
Revises: 8d854e4f3ae2
Create Date: 2024-09-09 21:26:25.255220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aff041ba4948'
down_revision = '8d854e4f3ae2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('foto_cover', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('foto_cover')

    # ### end Alembic commands ###
