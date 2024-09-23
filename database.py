from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Union
from data_generator import DataGenerator
from tables import Base, Author, Book


class Database:
    def __init__(self, db_name: str) -> None:
        self._books: List[Book] = []
        self._authors: List[Author] = []
        self.db_name = f"{db_name}.sqlite3"
        self.engine = create_engine(f"sqlite:///{self.db_name}", echo=False)
        Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.session = Session()

    def insert_data(self, new_data: List[Union[Book, Author]]) -> None:
        self.session.add_all(new_data)
        self.session.commit()

    def generate_fake_data(
        self, books_range: int, authors_range: int
    ) -> List[List[Union[Book, Author]]]:
        data_gen = DataGenerator()
        self._authors = data_gen.generate_authors(authors_range)
        self._books = data_gen.generate_books(books_range, self._authors)

        return [self._books, self._authors]
