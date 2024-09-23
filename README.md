# DB Operation with SqlAlchemy

## Description
Books database with fake random data created and managed with sqlAlchemy.
database consists of three tables for '**books**' with 1000 records, '**authors**' with 500 records
and an association table for '**authors_and_books**'. Uses many-to-many relationship.

**The Books Database holds detailed information about published books and authors for effective data management.** 
### **'books' table fields.**

| id | Name   | Category   | Number_of_Pages | Date   | Author_ID |
|----|--------|------------|-----------------|--------|-----------|
| 1  | _name_ | _category_ |  _num of pages_ | _date_ | _id_num_  |

**'books'** table **primary key** is **'id'** 

### **'authors' table fields.**
| id | First_Name   | Last_Name   | DoB    | Birth_City |
|----|--------------|-------------|--------|------------|
| 1  | _first name_ | _last name_ | _date_ | _city_     |

**'authors'** table **primary key** is **'id'**

### **'authors_and_books' table fields.**
| id | author_id | book_id  |
|----|-----------|----------|
| 1  | _id_num_  | _id_num_ |

**'authors_and_books'** table **primary key** is **id** and also has an autoincrement constraint.

## Components
* **Database**: Handles the database operations like initializing database and inserting data. 
* **AuthorBook**: An association table for many-to-many relationship
* **Author**: Author table that creates author fields and relationship
* **Book**: Book table that creates book fields and relationship
* **DataGenerator**: Uses Faker class and different providers from faker library. 
Is responsible for generating random data and associating data to authors and books.
* **Tasks**: Fetches the records from the database tables according to tasks provided.

### Provided Tasks
* Find and print all fields of the book with maximum number of pages
* Find and print the average of the number of pages
* Print the youngest author
* Print the authors who have not written any books yet
* Find 5 authors with more than 3 books (Bonus Task)


## Usage

To run the application, use the following command in your terminal:
```bash
python main.py
```

## Dependencies
* **Python 3.X**
* **Faker**: external library for generating random data using different providers: BaseProvider, lorem, date_time, person
* **SQLAlchemy**: Python library that provides an SQL toolkit and an Object Relational Mapper for database interactions

#### Python Standard Library modules used:
* **sqlite3**: DB-API 2.0 interface for SQLite databases.
* **random**: Generate pseudo-random numbers.
* **datetime**: Basic date and time types.
