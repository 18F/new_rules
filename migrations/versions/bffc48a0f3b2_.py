"""empty message

Revision ID: bffc48a0f3b2
Revises: 2684dcf3b305
Create Date: 2018-12-03 14:20:47.353456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bffc48a0f3b2'
down_revision = '2684dcf3b305'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('disaster', sa.Column('uses_DSED', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('disaster', 'uses_DSED')
    # ### end Alembic commands ###
