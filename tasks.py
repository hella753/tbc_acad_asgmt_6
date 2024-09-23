from database import Database
from tables import Book, Author, AuthorBook
from sqlalchemy import func


class Tasks:
    def __init__(self, db: Database) -> None:
        """
        Initializes the Tasks class with a database instance.

        Arguments:
            db {Database} -- An instance of the Database class,
            providing access to the database session.
        """
        self.db = db

    def get_biggest_book(self) -> None:
        """
        fetches and prints the books with the maximum number of pages
        from the database.
        """
        max_pages = self.db.session.query(func.max(Book.num_of_pages)).scalar()
        biggest_book = (
            self.db.session.query(Book)
            .where(Book.num_of_pages == max_pages)
            .all()
        )
        print("Books with the maximum number of pages:")
        for book in biggest_book:
            print(
                f"{book.id}, "
                f"{book.name}, "
                f"{book.category}, "
                f"{book.num_of_pages}, "
                f"{book.date}"
            )
        print()

    def get_avg_page_count(self) -> None:
        """
        fetches and prints the average number of pages of all the books.
        """
        average_page_count = (
            self.db.session.query(
                func.avg(Book.num_of_pages)
            ).scalar()
        )
        print(f"Average number of pages in books: {average_page_count}\n")

    def get_youngest_authors(self) -> None:
        """
        fetches and prints the youngest author by date of birth.
        """
        max_dob = self.db.session.query(func.max(Author.dob)).scalar()
        youngest_authors = (
            self.db.session.query(
                Author.first_name,
                Author.last_name,
                Author.dob
            )
            .filter(Author.dob == max_dob)
            .all()
        )
        print(f"Youngest Authors")
        for author in youngest_authors:
            first_name, last_name, dob = author
            print(first_name, last_name)
        print()

    def get_authors_with_no_books(self) -> None:
        """
        fetches and prints all authors who have no books associated with them
        """
        authors_with_no_books = (
            self.db.session.query(
                Author.id,
                Author.first_name,
                Author.last_name
            )
            .select_from(Author)
            .outerjoin(AuthorBook)
            .outerjoin(Book)
            .filter(Book.id.is_(None))
            .all()
        )
        print(f"Authors with no books:")
        for author in authors_with_no_books:
            auth_id, first_name, last_name = author
            print(auth_id, first_name, last_name)
        print()

    def bonus(self) -> None:
        """
        fetches and prints up to 5 authors who have written
        more than three books.
        """
        authors_with_more_than_three_books = (
            self.db.session.query(
                Author.id,
                Author.first_name,
                Author.last_name,
            )
            .outerjoin(AuthorBook)
            .outerjoin(Book)
            .group_by(Author.id, Author.first_name, Author.last_name)
            .having(func.count(Book.id) > 3)
            .limit(5)
            .all()
        )
        print(f"5 authors with more than three books:")
        for author in authors_with_more_than_three_books:
            auth_id, first_name, last_name = author
            print(auth_id, first_name, last_name)
        print()

    def __str__(self) -> str:
        return f"\nTASKS: "
