"""init

Revision ID: 4d2c8ddc27db
Revises: 
Create Date: 2017-04-17 17:25:31.389849

"""

# revision identifiers, used by Alembic.
revision = '4d2c8ddc27db'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###