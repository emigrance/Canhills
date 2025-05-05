import sqlite3

def setup_database():
    conn = sqlite3.connect('job_board.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    # Create JobListings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS JobListings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        employer_id INTEGER,
        FOREIGN KEY (employer_id) REFERENCES Users (id)
    )
    ''')

    # Create Applications table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER,
        applicant_name TEXT NOT NULL,
        applicant_email TEXT NOT NULL,
        message TEXT,
        FOREIGN KEY (job_id) REFERENCES JobListings (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
