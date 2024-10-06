import sqlite3

# Connect to the SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect('missing_persons.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the missing persons table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS missing_persons (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        date_of_disappearance TEXT NOT NULL,
        location TEXT NOT NULL,
        additional_info TEXT
    )
''')

# Insert sample data into the missing_persons table
cursor.execute('''
    INSERT INTO missing_persons (name, date_of_disappearance, location, additional_info)
    VALUES 
    ('Jane Doe', '2023-01-15', 'Los Angeles, CA', 'Last seen at a grocery store'),
    ('John Smith', '2022-12-11', 'San Francisco, CA', 'Reported missing after a hiking trip')
''')

# Commit the changes and close the connection
conn.commit()  # Commits the changes (inserts the data)
conn.close()   # Closes the connection to the database

print("Database and sample data created successfully!")
