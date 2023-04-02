"""empty message

Revision ID: 323c9b64e76d
Revises: 
Create Date: 2023-04-01 21:48:06.050744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323c9b64e76d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_index('ix_users_wallet_address', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_questions_id', table_name='questions')
    op.drop_table('questions')
    op.drop_index('ix_events_id', table_name='events')
    op.drop_table('events')
    op.drop_index('ix_participants_id', table_name='participants')
    op.drop_table('participants')
    op.drop_index('ix_prizes_id', table_name='prizes')
    op.drop_table('prizes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prizes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('base_prize', sa.INTEGER(), nullable=True),
    sa.Column('registration_prize_percentage', sa.FLOAT(), nullable=True),
    sa.Column('distribution', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_prizes_id', 'prizes', ['id'], unique=False)
    op.create_table('participants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('score', sa.INTEGER(), nullable=True),
    sa.Column('answered_questions', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('event_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_participants_id', 'participants', ['id'], unique=False)
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('private', sa.BOOLEAN(), nullable=True),
    sa.Column('max_registrations', sa.INTEGER(), nullable=True),
    sa.Column('number_registrations', sa.INTEGER(), nullable=True),
    sa.Column('entrance_fee', sa.FLOAT(), nullable=True),
    sa.Column('inicial_date', sa.DATETIME(), nullable=True),
    sa.Column('final_date', sa.DATETIME(), nullable=True),
    sa.Column('event_address', sa.VARCHAR(), nullable=True),
    sa.Column('event_state', sa.VARCHAR(), nullable=True),
    sa.Column('abi', sa.VARCHAR(), nullable=True),
    sa.Column('owner_id', sa.INTEGER(), nullable=True),
    sa.Column('prize_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['prize_id'], ['prizes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_events_id', 'events', ['id'], unique=False)
    op.create_table('questions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question', sa.VARCHAR(), nullable=True),
    sa.Column('options', sa.VARCHAR(), nullable=True),
    sa.Column('answer', sa.VARCHAR(), nullable=True),
    sa.Column('score', sa.INTEGER(), nullable=True),
    sa.Column('event_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_questions_id', 'questions', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('wallet_address', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_wallet_address', 'users', ['wallet_address'], unique=False)
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
