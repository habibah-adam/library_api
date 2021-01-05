-- First query:
-- show boosk that has empty pages
SELECT b.title, b.author
FROM books b
INNER JOIN pages p
ON b.id = p.book_id
WHERE p.page_content IS NULL;

--- Second Query:
-- Grouping books by its title and count the pages it has
SELECT b.title, count(p.page_number) as Number_Of_Pages
FROM books b
INNER JOIN pages p
ON b.id = p.book_id
GROUP BY b.title;

-- Query Three:
-- Find out large volumed books
-- Books with over 500 pages
SELECT b.title
FROM books b
INNER JOIN pages p
ON b.id = p.book_id
GROUP BY b.title
HAVING count(p.page_number) > 500;