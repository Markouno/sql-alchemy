import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from inserts import load_database


DSN = 'postgresql://postgres:Markouno123@localhost:5432/sql-alchemy'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

load_database()  # Загрузка данных в базу

need_author = input('Введите автора: ')

publisher = session.query(Publisher).filter_by(name=need_author).first()
if not publisher:
    print('Нету такова')
else:
    sales = session.query(Sale).join(Stock).join(Book).join(
        Publisher).join(Shop).filter(Publisher.id == publisher.id).all()

    for sale in sales:
        print(
            f'{sale.stock.book.title} | {sale.stock.shop.name} | {sale.price} | {sale.date_sale}')
session.close()
