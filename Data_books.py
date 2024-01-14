import sqlalchemy



from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import date


db = 'postgresql://postgres:postgres@localhost:5432/database'
engine = create_engine(db)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    id_publisher = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship("Publisher", backref="books")

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey('books.id'))
    id_shop = Column(Integer, ForeignKey('shops.id'))
    count = Column(Integer)

    book = relationship("Book", backref="stocks")
    shop = relationship("Shop", backref="stocks")

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    date_sale = Column(Date)
    id_stock = Column(Integer, ForeignKey('stocks.id'))
    count = Column(Integer)

    stock = relationship("Stock", backref="sales")

Base.metadata.create_all(engine)



publisher1 = Publisher(name="Издательство1")
publisher2 = Publisher(name="Издательство2")
session.add_all([publisher1, publisher2])
session.commit()

book1 = Book(title="Книга1", publisher=publisher1)
book2 = Book(title="Книга2", publisher=publisher1)
book3 = Book(title="Книга3", publisher=publisher2)
session.add_all([book1, book2, book3])
session.commit()

shop1 = Shop(name="Магазин1")
shop2 = Shop(name="Магазин2")
session.add_all([shop1, shop2])
session.commit()

stock1 = Stock(book=book1, shop=shop1, count=20)
stock2 = Stock(book=book1, shop=shop2, count=30)
stock3 = Stock(book=book2, shop=shop1, count=25)
stock4 = Stock(book=book3, shop=shop2, count=15)
session.add_all([stock1, stock2, stock3, stock4])
session.commit()

sale1 = Sale(price=500, date_sale=date(2022, 1, 15), stock=stock1, count=5)
sale2 = Sale(price=600, date_sale=date(2022, 2, 20), stock=stock2, count=10)
sale3 = Sale(price=450, date_sale=date(2022, 3, 25), stock=stock3, count=7)
sale4 = Sale(price=700, date_sale=date(2022, 4, 30), stock=stock4, count=8)
session.add_all([sale1, sale2, sale3, sale4])
session.commit()


session.close()
engine.dispose()
