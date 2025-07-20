''' This module provides a context manager for managing database sessions using SQLAlchemy.'''
from config.config_handler import ConfigHandler
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

class SessionContext:
    ''' A context manager for handling database sessions. It ensures that sessions are properly committed or rolled back and closed after use. '''

    def __init__(self):
        config = ConfigHandler()
        dbname = config.db_name
        user = config.db_user
        password = config.db_password
        password="" if password is None else password
        port = config.db_port
        host = config.db_host

        if port == "_":
            engine = create_engine("postgresql+psycopg2://"+user+":"+password+"@"+host+"/"+dbname)
        else:
            engine = create_engine("postgresql+psycopg2://"+user+":"+password+"@"+host+":"+str(port)+"/"+dbname)

        session = sessionmaker(bind=engine)
        self.session = session()
        self.engine = engine


    def __enter__(self):
        return self.session


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
        self.engine.dispose()
