create database priya;
use priya;

-- TASK 1

CREATE TABLE Members ( 
member_id INT primary key,
name_id varchar (50),
email_id varchar (50) UNIQUE,
join_date DATE
    );

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
);
select * from books;

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- TASK 2
INSERT INTO Members (member_id, name_id, email_id, join_date) VALUES
(101, 'Preethi', 'pree@123.gmail.com', '2025-10-3'),
(102, 'Pavan', 'pav@gmail.com', '2025-10-27'),
(103, 'Priya', 'pri@gmail.com', '2025-10-15');

INSERT INTO Books (book_id, title, author, available) VALUES
(110, 'Atomic Habits', 'James Clear', TRUE),
(120, 'Rich Dad Poor Dad', 'Robert Kiyosaki', TRUE),
(130, 'The Power of Habit', 'Charles Duhigg', FALSE),
(140, 'The Alchemist', 'Paulo Coelho', TRUE);

INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(1, 101, 130, '2025-10-10', NULL),
(2, 102, 110, '2025-10-12', '2025-10-20'),
(3, 103, 120, '2025-10-15', NULL);

-- TASK 3
SELECT*from Members WHERE join_date > '2025-09-01';
SELECT * FROM Members;
SELECT * FROM Books;
SELECT * FROM Loans;
SELECT 
    Books.book_id,
    Books.title,
    Books.author,
    Loans.loan_date,
    Loans.return_date
FROM Loans
JOIN Books ON Loans.book_id = Books.book_id
JOIN Members ON Loans.member_id = Members.member_id
WHERE Members.name_id = 'Priya';

-- TASK 4
UPDATE Books
SET available = FALSE
WHERE book_id = 110;

DELETE FROM Loans
WHERE member_id = 101;

SELECT * FROM Loans
WHERE member_id = 103 AND return_date IS NULL;

show tables;
select * from books;
select * from Loans;
select * from member;
