"""empty message

Revision ID: 65da40760a2e
Revises: 
Create Date: 2022-12-07 00:53:25.022865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65da40760a2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('publicId', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('firstName', sa.String(length=128), nullable=False),
    sa.Column('lastName', sa.String(length=128), nullable=False),
    sa.Column('isActive', sa.Boolean(), nullable=False),
    sa.Column('isStaff', sa.Boolean(), nullable=False),
    sa.Column('isAdmin', sa.Boolean(), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('passwordHash', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('publicId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###