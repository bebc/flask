"""empty message

Revision ID: e2520ea04132
Revises: 3291bac745da
Create Date: 2017-09-24 13:40:08.969691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2520ea04132'
down_revision = '3291bac745da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ops_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('ops_type', sa.String(length=64), nullable=False),
    sa.Column('service_type', sa.String(length=64), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ops_record_name'), 'ops_record', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ops_record_name'), table_name='ops_record')
    op.drop_table('ops_record')
    # ### end Alembic commands ###
