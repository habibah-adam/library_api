-- First Joined Query:
-- This query joins two Tables:
--    + Books
--    + Pages
-- and joins them on the 'book_id' from Pages and 'id' from books
SELECT p.id, p.page_number, b.id as book_id, b.title, p.page_content
FROM pages p
INNER JOIN books b
ON p.book_id = b.id;

-- Second Joined Query:
-- This query joins three tables:
--  + Books
--  + Pages
--  + Users
-- And shows:
-- + Title from Books
-- + Author from Books
-- + Email Address from Users
-- + Page contents from Pages
SELECT b.title, b.author, u.email, p.page_content
FROM users u
INNER JOIN books b
ON u.id = b.user_id
INNER JOIN pages p
ON b.id = p.book_id
;
