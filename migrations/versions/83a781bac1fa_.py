"""empty message

Revision ID: 83a781bac1fa
Revises: 
Create Date: 2018-12-11 17:57:23.715711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83a781bac1fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('piguser',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pigid', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reqhead', sa.String(length=5000), nullable=False),
    sa.Column('reqbody', sa.String(length=5000), nullable=False),
    sa.Column('regtime', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userinfo')
    op.drop_table('piguser')
    # ### end Alembic commands ###
