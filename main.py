from database import Database
from tasks import Tasks


def main():
    # Initialize the database
    db = Database("books.db")

    # Generate and insert fake data
    books_data, authors_data = db.generate_fake_data(1000, 500)
    db.insert_data(books_data)
    db.insert_data(authors_data)

    # Create and execute tasks
    tasks = Tasks(db)
    print(tasks)
    tasks.get_biggest_book()  # Task 1
    tasks.get_avg_page_count()  # Task 2
    tasks.get_youngest_authors()  # Task 3
    tasks.get_authors_with_no_books()  # Task 4
    tasks.bonus()  # Bonus Task


if __name__ == "__main__":
    main()
