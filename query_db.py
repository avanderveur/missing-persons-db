import sqlite3

# Connect to the database
conn = sqlite3.connect('missing_persons.db')

# Create a cursor
cursor = conn.cursor()

# Fetch all rows from the missing_persons table
cursor.execute('SELECT * FROM missing_persons')
rows = cursor.fetchall()

# Print out the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
