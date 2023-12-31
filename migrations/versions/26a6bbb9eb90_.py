"""empty message

Revision ID: 26a6bbb9eb90
Revises: 
Create Date: 2023-08-20 12:43:24.456282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26a6bbb9eb90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sample',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('User_Name', sa.String(length=200), nullable=False),
    sa.Column('User_Email', sa.String(length=350), nullable=False),
    sa.Column('User_Password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('User_Name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sample')
    # ### end Alembic commands ###
