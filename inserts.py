import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = 'postgresql://postgres:Markouno123@localhost:5432/sql-alchemy'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def load_database():
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()
