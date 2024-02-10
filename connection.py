from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values(".env")

CONNECTION_STRING = f"postgresql+psycopg://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"

engine = create_engine(CONNECTION_STRING, pool_size=80)

Session = sessionmaker(bind=engine)

session = Session()
