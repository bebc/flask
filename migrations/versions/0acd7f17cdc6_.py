"""empty message

Revision ID: 0acd7f17cdc6
Revises: 1f8048c8a2c9
Create Date: 2017-09-09 13:51:32.117587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0acd7f17cdc6'
down_revision = '1f8048c8a2c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=64), nullable=False),
    sa.Column('applicationserver', sa.String(length=64), nullable=True),
    sa.Column('webproject', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_application_info_ip'), 'application_info', ['ip'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_application_info_ip'), table_name='application_info')
    op.drop_table('application_info')
    # ### end Alembic commands ###