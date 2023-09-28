from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), unique=True)

engine = create_engine('sqlite:///minhabasededados.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
