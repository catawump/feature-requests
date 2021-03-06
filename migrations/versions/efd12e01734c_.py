"""empty message

Revision ID: efd12e01734c
Revises: 5d8520bcc675
Create Date: 2018-08-13 18:19:20.370000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd12e01734c'
down_revision = '5d8520bcc675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_request_target_date'), 'request', ['target_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_request_target_date'), table_name='request')
    # ### end Alembic commands ###
