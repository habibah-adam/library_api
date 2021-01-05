# Library API Extension

## Introduction

This project is to extend the exisiting project demonstrated for CCC students in the Coder Academy Class. The original project can be found [here]("https://github.com/CoderAcademyEdu/ccc-03-16").

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
    - Erratta 
    - Typos
    - Update outdated information
- Delete pages not needed
- Read the contents of their books page by page.

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

### PRG1048-5.1
Refer to: [R9.sql]("./database_queries/R10.sql")

### PRG1048-5.2
Refer to: [R9.sql]("./database_queries/R11.sql")

### PRG1048-5.3
Refer to: [R9.sql]("./database_queries/R12.sql")
