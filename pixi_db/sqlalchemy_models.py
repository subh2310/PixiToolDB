from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SQLAlchemyConnectNE(Base):
    __tablename__ = 'connectne'

    id = Column(Integer, primary_key=True)
    handle = Column(String(100))
    username = Column(String(100), default="temp")
    password = Column(String(100), default="root")
    hostname = Column(String(100))
    port = Column(Integer, default=22)
    interface = Column(String(50), default="CLI")

class SQLAlchemyDisconnectNE(Base):
    __tablename__ = 'disconnectne'

    id = Column(Integer, primary_key=True)
    handle = Column(String(100), default='', nullable=True)
    username = Column(String(100), default="temp")
    password = Column(String(100), default="root")
    hostname = Column(String(100))
    port = Column(Integer, default=22)
    interface = Column(String(50), default="CLI")

class SQLAlchemySendRCV(Base):
    __tablename__ = 'sendrcv'

    id = Column(Integer, primary_key=True)
    handle = Column(String(100), nullable=False, default="CLI")
    command = Column(String(500), nullable=True)


class SQLAlchemyComparePairs(Base):
    __tablename__ = 'compare_pairs'

    id = Column(Integer, primary_key=True)
    stash = Column(String(100), nullable=True, default="notStash")
    compare_input = Column(String(150), nullable=True, default=None)
    compare_result = Column(String(150), nullable=True, default=None)


# SQLAlchemy engine creation
DATABASE_NAME = 'Pixi_DB'
DATABASE_USER = 'temproot'
DATABASE_PASSWORD = 'infinera'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'  # default PostgreSQL port

# Construct the database URL for SQLAlchemy
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL)

# Create tables defined by Base
Base.metadata.create_all(engine)
