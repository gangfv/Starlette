from sqlalchemy import Table, Column, Integer, String, Text

from config.database import metadata

support = Table(
    'support',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('username', String),
    Column('email', String),
    Column('message', Text),
)
