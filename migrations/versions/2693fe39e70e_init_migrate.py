"""init_migrate

Revision ID: 2693fe39e70e
Revises: 
Create Date: 2018-11-02 17:34:23.020184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2693fe39e70e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tells',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visit_url', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visit_url', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visit',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visit_url', sa.String(length=256), nullable=True),
    sa.Column('visit_time', sa.DateTime(), nullable=True),
    sa.Column('success', sa.Enum('True', 'False'), nullable=True),
    sa.Column('tells_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visit')
    op.drop_table('user')
    op.drop_table('tells')
    # ### end Alembic commands ###
