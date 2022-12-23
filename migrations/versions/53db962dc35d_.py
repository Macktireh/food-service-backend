"""empty message

Revision ID: 53db962dc35d
Revises: 3b18c060693e
Create Date: 2022-12-23 21:59:55.572461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53db962dc35d'
down_revision = '3b18c060693e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=128), nullable=True))
        batch_op.drop_column('urlImage')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('urlImage', sa.VARCHAR(length=128), nullable=True))
        batch_op.drop_column('image')

    # ### end Alembic commands ###
