import datetime
import random
from typing import List, Set
from tables import Book, Author
from faker import Faker
from faker.providers import BaseProvider, date_time, person, lorem

# List of book genres that will be used for random category.
GENRES = [
    "Fantasy", "Science Fiction", "Dystopian", "Action & Adventure", "Mystery",
    "Horror", "Thriller & Suspense", "Historical Fiction", "Romance",
    "Graphic Novel", "Children’s", "Biography", "Self-help", "History",
    "True Crime", "Essays"
]


class DataGenerator(Faker):
    def __init__(self) -> None:
        """
        A subclass of Faker, and adds necessary providers for generating
        fake data such as text, names, dates.
        """
        super().__init__()
        self.add_provider(lorem)
        self.add_provider(date_time)
        self.add_provider(BaseProvider)
        self.add_provider(person)

    def generate_authors(self, num: int) -> List[Author]:
        """
        Generates a list of Author objects with random data.

        Arguments:
            num {int} -- The number of authors to generate.

        Returns:
            List[Author] -- A list containing Author objects, with randomly
            generated first name, last name, date of birth, and city of birth.
        """
        authors_list: List[Author] = []
        for i in range(1, num + 1):
            first_name: str = self.first_name()
            last_name: str = self.last_name()
            dob: datetime.date = self.date_between(
                datetime.date(1960, 1, 1),
                datetime.date(1999, 12, 31)
            )
            city: str = self.city()
            author = Author(
                id=i,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                birth_city=city
            )
            authors_list.append(author)
        return authors_list

    def generate_books(self, num: int, authors: List[Author]) -> List[Book]:
        """
        Generates a list of Book objects with random data and
        assigns them to authors. We have two set of data for
        authors with books and without. if num authors generates
        0 authors there will be books without an assigned author.

        Arguments:
            num {int} -- The number of books to generate.
            authors {List[Author]} -- A list of Author objects
            to assign to books.

        Returns:
            List[Book] -- A list of Book objects, with a random name, category,
            number of pages, and publication date. A random number of authors
            from the input list are assigned to each book.
        """
        books_list: List[Book] = []
        all_authors_set: Set[Author] = set(authors)
        num_authors_without_books = random.randint(15, 100)
        authors_without_books: Set[Author] = set(
            random.sample(
                authors,
                num_authors_without_books
            )
        )
        authors_with_books: List[Author] = list(
            all_authors_set - authors_without_books
        )

        for i in range(1, num + 1):
            random_digit: int = self.random_int(min=15, max=1000)
            date: datetime.date = self.date_this_century()
            text: str = self.text(max_nb_chars=20).rstrip('.')  # Removing '.'
            category: str = random.choice(GENRES)
            book = Book(
                id=i,
                name=text,
                category=category,
                num_of_pages=random_digit,
                date=date
            )
            num_authors = random.randrange(0, 3)
            book_authors: List[Author] = random.sample(
                authors_with_books,
                num_authors
            )
            for author in book_authors:
                book.authors.append(author)

            books_list.append(book)

        return books_list
