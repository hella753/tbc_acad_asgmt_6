from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # type: ignore


class AuthorBook(Base):  # type: ignore
    __tablename__ = "authors_and_books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column("author_id", Integer, ForeignKey("authors.id"))
    book_id = Column("book_id", Integer, ForeignKey("books.id"))


class Author(Base):  # type: ignore
    __tablename__ = 'authors'
    id = Column("id", Integer, primary_key=True)
    first_name = Column("First_Name", String, nullable=False)
    last_name = Column("Last_Name", String, nullable=False)
    dob = Column("DoB", Date, nullable=False)
    birth_city = Column("Birth_City", String, nullable=False)

    books = relationship(  # type: ignore
        'Book',
        back_populates='authors',
        secondary="authors_and_books"
    )


class Book(Base):  # type: ignore
    __tablename__ = 'books'
    id = Column("id", Integer, primary_key=True)
    name = Column("Name", String, nullable=False)
    category = Column("Category", String, nullable=False)
    num_of_pages = Column("Number_of_Pages", Integer, nullable=False)
    date = Column("Date", Date, nullable=False)

    authors = relationship(  # type: ignore
        'Author',
        secondary="authors_and_books",
        back_populates='books'
    )
