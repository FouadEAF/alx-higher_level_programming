#!/usr/bin/python3
""" Print all Cities objects from the database hbtn_0e_14_usa """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    stat_city = session\
        .query(State, City)\
        .filter(State.id == City.state_id)\
        .order_by(City.id)\
        .all()

    for state, city in stat_city:
        print(f"{state.name}: ({city.id}) {city.name}")
