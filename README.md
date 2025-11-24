# LIBRARY-MANAGEMENT-SYSTEM
Library Management System
#Overview of the Project
This Python application is a simple command-line library management system using SQLite3 for data storage. It allows users to view available books, issue books to students, and submit books, calculating fines for late returns.

#Features
List all available books

Issue books to students and record loan details

Submit books and check for late return fines

Update the book and student records in the SQLite database

User-friendly text-based menu for navigation

Technologies/Tools Used
Python 3 (Primary programming language)

SQLite3 (Database management)

datetime module (Date calculations for book returns)

#Steps to Install & Run the Project
Clone or download the repository to your local machine.

Ensure Python 3 is installed.

Create the SQLite database library.db with the required tables:

Book table with columns: book_name (text), status (text: "available"/"issued")

Student table with columns: student_id (primary key), name, book_taken, issue_date, return_date

Place the Python script in the project directory.

Run the script with:

bash
python your_script_name.py
Follow the menu prompts in the terminal.

#Instructions for Testing
Use option 1 to list available books.

Use option 2 to issue a book by entering required student and book information.

Use option 3 to submit a book and test late submission by providing a return date later than the scheduled date.

Use option 4 to exit.
