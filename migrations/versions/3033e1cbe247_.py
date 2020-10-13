"""empty message

Revision ID: 3033e1cbe247
Revises: 53e4c20b645e
Create Date: 2020-10-13 01:48:55.114384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3033e1cbe247'
down_revision = '53e4c20b645e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip_blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('city_country', sa.String(length=140), nullable=False),
    sa.Column('stayed_where', sa.String(length=140), nullable=False),
    sa.Column('went_where', sa.String(length=140), nullable=False),
    sa.Column('trip_image', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip_blog')
    # ### end Alembic commands ###