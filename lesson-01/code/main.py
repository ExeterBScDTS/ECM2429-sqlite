# This example taken from the sqlite3 documentation at https://docs.python.org/3/library/sqlite3.html
#

import sqlite3
from sqlite3.dbapi2 import Connection

# Create a temporary database in memory.
conn : Connection = sqlite3.connect(':memory:')
# More usual is to have a database file, e.g.
# conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
(date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("""INSERT INTO stocks
          VALUES ('2006-01-05','BUY','RHAT',100,35.14)""")


# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()

# Now retreive the data
c = conn.cursor()
c.execute('SELECT * FROM stocks ORDER by price')
for row in c:
    print(row)

c.close()
conn.close()
