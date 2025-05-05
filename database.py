import sqlite3

def init_db():
    conn = sqlite3.connect('job_board.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create Job Listings table
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
            applicant_id INTEGER,
            resume_path TEXT,
            FOREIGN KEY (job_id) REFERENCES JobListings (id),
            FOREIGN KEY (applicant_id) REFERENCES Users (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
