from sqlalchemy import (
    String, Column, DateTime,
    Integer, create_engine, Boolean
)

from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = 'postgresql://admin:01233210@postgres:5432/SpaceX'
engine = create_engine(ENGINE, echo=True)
session = sessionmaker(engine)

Base = declarative_base()


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


class Launches(Base):
    __tablename__ = 'launches'
    id = Column(String, primary_key=True, index=True)
    details = Column(String)
    is_tentative = Column(Boolean)
    launch_date_local = Column(DateTime)
    launch_date_utc = Column(DateTime)
    launch_success = Column(Boolean)
    launch_year = Column(String)
    mission_name = Column(String)
    static_fire_date_utc = Column(DateTime)
    tentative_max_precision = Column(String)
    upcoming = Column(Boolean)


class Missions(Base):
    __tablename__ = 'missions'
    id = Column(String, primary_key=True, index=True)
    description = Column(String)
    manufacturers = Column(String)
    name = Column(String)
    twitter = Column(String)
    website = Column(String)
    wikipedia = Column(String)


Base.metadata.create_all(engine)






