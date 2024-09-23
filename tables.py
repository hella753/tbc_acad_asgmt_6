from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # type: ignore


class AuthorBook(Base):  # type: ignore
    """
    Represents the association table between the Author and Book tables
    for the many-to-many relationship between authors and books.

    Columns:
        id {int} -- The primary key, auto-incremented.
        author_id {int} -- Foreign key referencing the Author table.
        book_id {int} -- Foreign key referencing the Book table.
    """
    __tablename__ = "authors_and_books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column("author_id", Integer, ForeignKey("authors.id"))
    book_id = Column("book_id", Integer, ForeignKey("books.id"))


class Author(Base):  # type: ignore
    """
    Represents an author with personal details.

    Columns:
        id {int} -- The primary key.
        first_name {str} -- The first name of the author (non-nullable).
        last_name {str} -- The last name of the author (non-nullable).
        dob {date} -- The date of birth of the author (non-nullable).
        birth_city {str} -- The birth city of the author (non-nullable).

    Relationships:
        books -- Book objects associated with the author,
        representing the many-to-many relationship through
        the `authors_and_books` table.
    """
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
    """
    Represents a book with details about its publication and content.

    Columns:
        id {int} -- The primary key.
        name {str} -- The name of the book (non-nullable).
        category {str} -- The genre or category of the book (non-nullable).
        num_of_pages {int} -- The number of pages in the book (non-nullable).
        date {date} -- The publication date of the book (non-nullable).

    Relationships:
        authors -- Author objects associated with the book,
        representing the many-to-many relationship through
        the `authors_and_books` table.
    """
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
