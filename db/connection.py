from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values
import logging

config = dotenv_values(".env")

CONNECTION_STRING = f"postgresql+psycopg://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"

engine = create_engine(CONNECTION_STRING, pool_size=80)

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

try:
    result = session.execute(text("SELECT 1"))
    print("\033[92mConnected to the database successfully.\033[0m")
except Exception as e:
    print("\033[91mFailed to connect to the database:", e, "\033[0m")
finally:
    session.close()

# Enable logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
