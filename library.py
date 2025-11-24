import sqlite3
from datetime import datetime

db_file = "library.db"

def list_available_books():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT book_name FROM book WHERE status='available'")
    books = cursor.fetchall()
    conn.close()
    if books:
        print("Available books:")
        for b in books:
            print("-", b[0])
    else:
        print("No books available right now.")

def issue_book():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    list_available_books()
    book_taken = input("Enter name of the book to issue: ")

    # Check if book is available
    cursor.execute("SELECT status FROM book WHERE book_name=?", (book_taken,))
    book_status = cursor.fetchone()
    if not book_status or book_status[0] != "available":
        print("Book is not available to issue.")
        conn.close()
        return

    issue_date = input("Enter issue date (YYYY-MM-DD): ")
    return_date = input("Enter return date (YYYY-MM-DD): ")

    # Insert or update student record
    cursor.execute("""
        INSERT INTO student (student_id, name, book_taken, issue_date, return_date)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(student_id) DO UPDATE SET
        name=excluded.name,
        book_taken=excluded.book_taken,
        issue_date=excluded.issue_date,
        return_date=excluded.return_date
    """, (student_id, name, book_taken, issue_date, return_date))

    # Update book status to issued
    cursor.execute("UPDATE book SET status='issued' WHERE book_name=?", (book_taken,))

    conn.commit()
    conn.close()
    print(f"Book '{book_taken}' issued to {name}.")

def submit_book():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    student_name = input("Enter student name: ")

    # Get student's record
    cursor.execute("SELECT student_id, book_taken, issue_date, return_date FROM student WHERE name=?", (student_name,))
    record = cursor.fetchone()
    if not record:
        print("No record found for this student.")
        conn.close()
        return

    student_id, book_taken, issue_date, return_date = record
    print(f"Book issued: {book_taken}, Return date: {return_date}")

    actual_return_date = input("Enter actual return date (YYYY-MM-DD): ")

    fmt = "%Y-%m-%d"
    diff_days = (datetime.strptime(actual_return_date, fmt) - datetime.strptime(return_date, fmt)).days
    fine = 0
    if diff_days > 0:
        fine = diff_days * 50
        print(f"Late return! Fine to be paid: {fine} rupees.")
    else:
        print("Book returned on time. No fine.")

    # Update book status to available
    cursor.execute("UPDATE book SET status='available' WHERE book_name=?", (book_taken,))

    # Clear student's book_taken and dates
    cursor.execute("""
        UPDATE student SET book_taken=NULL, issue_date=NULL, return_date=NULL WHERE student_id=?
    """, (student_id,))

    conn.commit()
    conn.close()
    print("Book return process completed successfully.")

def main():
    while True:
        print("\nPress 1 for available books")
        print("Press 2 for issuing book")
        print("Press 3 for submission of book")
        print("Press 4 to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_available_books()
        elif choice == '2':
            issue_book()
        elif choice == '3':
            submit_book()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()