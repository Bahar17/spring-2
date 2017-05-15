"""game_init

Revision ID: 3269d4280da1
Revises: 4d2c8ddc27db
Create Date: 2017-05-15 17:29:50.163605

"""

# revision identifiers, used by Alembic.
revision = '3269d4280da1'
down_revision = '4d2c8ddc27db'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import core


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('_avatar', sa.String(length=256), nullable=True),
    sa.Column('true_name', sa.String(length=64), nullable=False),
    sa.Column('profession_id', sa.Integer(), nullable=False),
    sa.Column('hidden_profession_id', sa.Integer(), nullable=True),
    sa.Column('character', core.JsonText(), nullable=False),
    sa.Column('play_script', core.JsonText(), nullable=False),
    sa.Column('date_created', core.DateTime(timezone=True), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('date_updated', core.DateTime(timezone=True), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_role_date_created'), 'game_role', ['date_created'], unique=False)
    op.create_index(op.f('ix_game_role_date_updated'), 'game_role', ['date_updated'], unique=False)
    op.create_index(op.f('ix_game_role_game_id'), 'game_role', ['game_id'], unique=False)
    op.create_table('larp_game',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('icon', sa.String(length=256), nullable=True),
    sa.Column('desc', core.JsonText(), nullable=True),
    sa.Column('price', sa.Integer(), server_default=u'314', nullable=True),
    sa.Column('min_required_num', sa.Integer(), server_default=u'0', nullable=False),
    sa.Column('max_required_num', sa.Integer(), server_default=u'0', nullable=False),
    sa.Column('ap_num', sa.Integer(), server_default=u'10', nullable=False),
    sa.Column('manual', core.JsonText(), nullable=True),
    sa.Column('type', sa.String(length=16), server_default='discovery', nullable=False),
    sa.Column('date_created', core.DateTime(timezone=True), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('date_updated', core.DateTime(timezone=True), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_larp_game_date_created'), 'larp_game', ['date_created'], unique=False)
    op.create_index(op.f('ix_larp_game_date_updated'), 'larp_game', ['date_updated'], unique=False)
    op.create_index(op.f('ix_larp_game_price'), 'larp_game', ['price'], unique=False)
    op.create_index(op.f('ix_larp_game_type'), 'larp_game', ['type'], unique=False)
    op.create_table('place_clue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place_id', sa.Integer(), nullable=False),
    sa.Column('order_score', sa.Integer(), server_default=u'0', nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('imgs', core.JsonText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('place_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('imgs', core.JsonText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_profession',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role_profession')
    op.drop_table('place_file')
    op.drop_table('place_clue')
    op.drop_index(op.f('ix_larp_game_type'), table_name='larp_game')
    op.drop_index(op.f('ix_larp_game_price'), table_name='larp_game')
    op.drop_index(op.f('ix_larp_game_date_updated'), table_name='larp_game')
    op.drop_index(op.f('ix_larp_game_date_created'), table_name='larp_game')
    op.drop_table('larp_game')
    op.drop_index(op.f('ix_game_role_game_id'), table_name='game_role')
    op.drop_index(op.f('ix_game_role_date_updated'), table_name='game_role')
    op.drop_index(op.f('ix_game_role_date_created'), table_name='game_role')
    op.drop_table('game_role')
    ### end Alembic commands ###
