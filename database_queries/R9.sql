
-- BookImage Table
CREATE TABLE book_images (
    id integer NOT NULL,
    filename character varying NOT NULL,
    book_id integer NOT NULL,
    PRIMARY KEY (id)
);

-- Books Table
CREATE TABLE books (
    id integer NOT NULL,
    title character varying,
    author character varying,
    user_id integer NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Pages Table:
CREATE TABLE pages (
    id integer NOT NULL,
    page_number integer NOT NULL,
    page_content text,
    book_id integer NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_book_id FOREIGN KEY (book_id) REFERENCES books (id)
);

-- Users table:
CREATE TABLE users (
    id integer NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL, 
    PRIMARY KEY (id)
);
