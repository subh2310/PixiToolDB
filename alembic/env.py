from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from pixi_db.sqlalchemy_models import Base  # Import SQLAlchemy Base object
from pixi_db import settings  # Import Django settings

# Use your Django database settings
DATABASE_NAME = settings.DATABASES['default']['NAME']
DATABASE_USER = settings.DATABASES['default']['USER']
DATABASE_PASSWORD = settings.DATABASES['default']['PASSWORD']
DATABASE_HOST = settings.DATABASES['default']['HOST']
DATABASE_PORT = settings.DATABASES['default']['PORT']

# Construct the database URL for SQLAlchemy
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Configure SQLAlchemy engine
config = context.config
config.set_main_option('sqlalchemy.url', DATABASE_URL)

# Bind the engine to the Base object
engine = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)
Base.metadata.bind = engine

# This function allows Alembic to run migrations against the SQLAlchemy models
def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )

        with context.begin_transaction():
            context.run_migrations()
