"""empty message

Revision ID: 64a5a2e27b10
Revises: 
Create Date: 2023-05-19 10:01:50.880390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a5a2e27b10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricula', sa.String(length=9), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('professores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricula', sa.String(length=9), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('chamadas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('chave', sa.String(length=5), nullable=True),
    sa.Column('prof_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prof_id'], ['professores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chave')
    )
    op.create_table('presencas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aluno_id', sa.Integer(), nullable=True),
    sa.Column('chamada_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aluno_id'], ['alunos.id'], ),
    sa.ForeignKeyConstraint(['chamada_id'], ['chamadas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('presencas')
    op.drop_table('chamadas')
    op.drop_table('professores')
    op.drop_table('alunos')
    # ### end Alembic commands ###
