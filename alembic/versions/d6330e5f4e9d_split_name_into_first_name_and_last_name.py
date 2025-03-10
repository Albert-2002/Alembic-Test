"""Split name into first_name and last_name

Revision ID: d6330e5f4e9d
Revises: 07beeaa38e47
Create Date: 2025-03-10 15:24:15.677732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String


# revision identifiers, used by Alembic.
revision: str = 'd6330e5f4e9d'
down_revision: Union[str, None] = '07beeaa38e47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Step 1: Add new columns first_name and last_name
    op.add_column('students', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('students', sa.Column('last_name', sa.String(), nullable=True))

    # Step 2: Migrate data from name to first_name/last_name
    students_table = table('students',
        column('id', sa.Integer),
        column('name', sa.String),
        column('email', sa.String),
        column('age', sa.Integer),
        column('first_name', sa.String),
        column('last_name', sa.String)
    )

    connection = op.get_bind()

    # Migrate data - split name
    result = connection.execute(sa.text("""
        SELECT id, name FROM students
    """))

    for row in result:
        full_name = row[1]
        if full_name:
            # Split name into first_name and last_name
            split_name = full_name.split(' ', 1)
            first_name = split_name[0]
            last_name = split_name[1] if len(split_name) > 1 else ''

            # Update the database
            connection.execute(sa.text("""
                UPDATE students
                SET first_name = :first_name,
                    last_name = :last_name
                WHERE id = :id
            """), {
                'first_name': first_name,
                'last_name': last_name,
                'id': row[0]
            })

    # Step 3 (Optional): Drop the name column
    op.drop_column('students', 'name')


def downgrade() -> None:
    # Step 1: Add the name column back (if you roll back)
    op.add_column('students', sa.Column('name', sa.String(), nullable=True))

    # Step 2: Merge first_name + last_name back into name
    connection = op.get_bind()
    connection.execute(sa.text("""
        UPDATE students
        SET name = first_name || ' ' || last_name
    """))

    # Step 3: Drop first_name and last_name
    op.drop_column('students', 'first_name')
    op.drop_column('students', 'last_name')
