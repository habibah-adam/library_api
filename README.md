# Library API Extension

## Introduction

This project is to extend the existing project demonstrated for CCC students in the Coder Academy Class. The original project can be found [here]("https://github.com/CoderAcademyEdu/ccc-03-16").

As a quick briefing on the original project. The project's goal is to build an *RESTful API*. This API can:
 
- Return:
    - All books in the library
    - Single book when book ID is given
- Update:
    - A single book information when ID is given
- Delete:
    - the book when ID is given
- Create:
    - New book when details are passed

## Extension 
The extension I am providing here is to add a **Page** object to the application and provide full **CRUD** functionality for this interface. This particular *AP* is intended to be used by **Authors** where they can:
- Add new page to their books
- Update a page of their book
    - Errata
    - Typos
    - Update outdated information
- Delete pages not needed
- Read the contents of their books page by page.

### CMP1042-7.1
`Flask SQLAlchemy` ORM is used to avoid raw SQL queries, this way the SQL injection attack is avoided, hence a layer of security is added to the application. Application uses marshmello validations to ensure the data integrity and Postgresql engine security features are uses:
- configuring the Database to listen only on one adapter: IP is specified in `postgresql.conf` file
- configuring `pg_hba.conf` file added another layer of security where it allows only 
1. speficied user can access spefied database
2. from specific IP address 
3. password is MD5 hashed

### CMP1042-7.2

The project is developed to provide library books data to certain audiances:
- Library members who has access to the books
- Authors of the books who wish to update, change, remove books or parts of the books (digital version of the books)
The users access are separated, normal Library members are not able to access:
- Page Removal
- Book Removal
Only Librarians or Authors are able to perform these actions. 

### CMP1042-1.1
The application uses `FLASK` python micro web framework where its backend storage is `Postgresql` database. It uses the MVC pattern to separate the concern by implementing:
- Controller
- Model
- View (View is not implemented, fully as it is not required by the assignment)



### CMP1042-1.2
#### Create
`POST`ing http://localhost:5000/pages with request body:
```json
{
    "page_number": 5,
    "page_content": "Some Text here",
    "book_id": 20
}
```
Will create a new page in the application, please refer to: [pages_controller.py]("./controllers/page_controller.py")

#### Read
`GET`ting http://localhost:5000/pages with NO request body will return all the pages in the database, please refer to: [pages_controller.py]("./controllers/page_controller.py")

`GET`ting http://localhost:5000/pages/id with NO request body will return a single page in the database where `id` is the page id in the table (primary key), please refer to: [pages_controller.py]("./controllers/page_controller.py")

#### Update
`PUT`ting or `UPDATE`ing http://localhost:5000/pages/id with request body:
```json
{
    "page_content": "SOME TEXT HERE" 
}
```
will update the page content when provided the id of the page. please refer to: [pages_controller.py]("./controllers/page_controller.py")

#### Delete
`DELETE`ting http://localhost:5000/pages/id with NO request body will remove the Page from the database, lease refer to: [pages_controller.py]("./controllers/page_controller.py")


### CMP1042-1.3
Jinja templating is used to creat frontend interface to view some functionalities in `HTML` format. 
This approach is followed by the educators advise: https://github.com/brucemcclure/jinja
The templates folder holds the page layouts and Jinja templates:
- [layout.html]("./templates/layout.html") 
    - General Layouts
- [books.html]("./templates/books.html")
    - List of books in HTML cards list
- [pages.html]("./templates/pages.html")
    - List of pages in HTML cards list
- [page.html]("./templates/page.html")
    - A single Page which returns the information about the page requested



### CMP1042-4.2
To address this requirement, an endpoint is create:
- numberOfPages
This endpoind will run the following query:
```sql
SELECT b.title, count(p.page_number) 
FROM pages p
INNER JOIN books b
GROUP BY b.title;
```
and will run `count` operation by grouping by the book title and return how many pags does each book has in the database.

## Database Scripting and Queries

### PRG1048-2.1
Refer to: [R9.sql]("./database_queries/R9.sql")

### PRG1048-2.2
In this project users can be in need of finding a a phrase in a book. And the phrases are in the pages of the book. So we need to join `books` with `pages` tables and look for that phrase in each pages of the book, so user must first know the book title:
```sql
SELECT b.title, b.author, p.page_number, p.page_content
FROM books b
INNER JOIN pages p
ON b.id = p.book_id
WHERE p.page_content LIKE '%The Phrase User is looking for.%';
```
### PRG1048-2.3
When inserting data to `Pages` table, the `primary key` is auto generated, but the user is required to supply `book_id` to refer back to which book this page belong to as `book_id` is a `Foreign Key` in `pages` table along with contents of the page and its number in the book. If the user fails to do so, `postgresql` engine will refuse to insert that particular entry as it violates the `referential integrity` of the database. 

```sql
library=# INSERT INTO pages (page_number, page_content) VALUES (99, 'VERY LONG PAGE CONTENT');
ERROR:  null value in column "book_id" violates not-null constraint
DETAIL:  Failing row contains (101, 99, VERY LONG PAGE CONTENT, null).
```

### PRG1048-5.1
Refer to: [R9.sql]("./database_queries/R10.sql")

### PRG1048-5.2
Refer to: [R9.sql]("./database_queries/R11.sql")

### PRG1048-5.3
Refer to: [R9.sql]("./database_queries/R12.sql")
This scripts are create by using the `postgresql` command `pg_dump`:
```bash
> pg_dump -U postgres library > ~/library.sql
```
