"""empty message

Revision ID: 36271309d1f6
Revises: None
Create Date: 2014-11-28 16:10:55.461905

"""

# revision identifiers, used by Alembic.
revision = '36271309d1f6'
down_revision = '24a62117b067'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workflowstepresults')
    op.drop_table('organizationsusers')
    op.drop_table('documentskeywords')
    op.drop_table('workflowsteps')
    op.drop_table('documentsproposals')
    op.drop_table('workflows')
    op.drop_table('keywords')
    op.drop_table('proposals')
    op.drop_table('contents')
    op.drop_table('documents')
    op.drop_table('organizations')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('name')
        batch_op.drop_column('title')

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organizations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('duns', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('ein', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'organizations_pkey'),
    postgresql_ignore_search_path=False
    )

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False))

    op.create_table('documents',
    sa.Column('id', sa.INTEGER(),  nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('filepath', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('organization_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], [u'organizations.id'], name=u'documents_organization_id_fkey', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'documents_pkey'),
    postgresql_ignore_search_path=False
    )

    op.create_table('proposals',
    sa.Column('id', sa.INTEGER(),  nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('sbir_topic_reference', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('start_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('end_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('organization_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], [u'organizations.id'], name=u'proposals_organization_id_fkey', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'proposals_pkey'),
    postgresql_ignore_search_path=False
    )

    op.create_table('workflows',
    sa.Column('id', sa.INTEGER(),  nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('proposal_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], [u'proposals.id'], name=u'workflows_proposal_id_fkey', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'workflows_pkey'),
    postgresql_ignore_search_path=False
    )

    op.create_table('contents',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('start_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('end_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('change_log', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('content', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('document_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['document_id'], [u'documents.id'], name=u'contents_document_id_fkey', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'contents_pkey')
    )
    op.create_table('workflowsteps',
    sa.Column('id', sa.INTEGER(),  nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('work', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('workflow_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['workflow_id'], [u'workflows.id'], name=u'workflowsteps_workflow_id_fkey', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'workflowsteps_pkey'),
    postgresql_ignore_search_path=False
    )


    op.create_table('documentsproposals',
    sa.Column('document_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('proposal_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['document_id'], [u'documents.id'], name=u'documentsproposals_document_id_fkey'),
    sa.ForeignKeyConstraint(['proposal_id'], [u'proposals.id'], name=u'documentsproposals_proposal_id_fkey')
    )

    op.create_table('organizationsusers',
    sa.Column('organization_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], [u'organizations.id'], name=u'organizationsusers_organization_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], name=u'organizationsusers_user_id_fkey')
    )


    op.create_table('workflowstepresults',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('result', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('completed_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('workflowstep_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['workflowstep_id'], [u'workflowsteps.id'], name=u'workflowstepresults_workflowstep_id_fkey', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'workflowstepresults_pkey')
    )
    op.create_table('keywords',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('keyword', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'keywords_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('documentskeywords',
    sa.Column('document_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('keyword_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['document_id'], [u'documents.id'], name=u'documentskeywords_document_id_fkey'),
    sa.ForeignKeyConstraint(['keyword_id'], [u'keywords.id'], name=u'documentskeywords_keyword_id_fkey')
    )


    ### end Alembic commands ###