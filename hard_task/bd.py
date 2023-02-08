from sqlalchemy import (
    String, Column, DateTime, ForeignKey,
    Integer, create_engine, Boolean, delete, update
)

from sqlalchemy.orm import declarative_base, relationship, sessionmaker, backref

ENGINE = 'postgresql://admin:01233210@localhost:5432/SpaceX'
Base = declarative_base()
engine = create_engine(ENGINE, echo=True)
Session = sessionmaker(engine)


class Rockets(Base):
    __tablename__ = 'rockets'
    id = Column(String, primary_key=True, index=True)
    active = Column(Boolean)
    boosters = Column(Integer)
    company = Column(String)
    cost_per_launch = Column(Integer)
    stages = Column(Integer)
    success_rate_pct = Column(Integer)
    type = Column(String)
    wikipedia = Column(String)


Base.metadata.create_all(engine)

from download_data import *

a = get_data_api([LAUNCHES, MISSIONS, ROCKETS], API)

with Session() as session:
    session.add(RocketsModel(**a['rockets'][0]))
